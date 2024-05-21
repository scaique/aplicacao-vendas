from flask import render_template, request, redirect, url_for
from .date import obter_data_atual
from .functions import carregar_planilha, salvar, venda_D, venda_C, troco_dia, troco_mes, calculo_total

def register_routes(app):
    dia, mes, ano, mesEscrito = obter_data_atual()
    wb = carregar_planilha()
    
    try:
        ws = wb[f'Soma']
        total = {
            'Dinheiro': ws[f'B{dia+1}'], 
            'Debito': ws[f'C{dia+1}'], 
            'Credito': ws[f'D{dia+1}'], 
            'Total': ws[f'F{dia+1}']
        }
    except:
        print('Erro ao carregar a planilha "Soma".')

    try:
        ws = wb[f'Dia {dia}']
    except:
        ws = wb.create_sheet(f'Dia {dia}')
        ws.append(["Dinheiro", "Débito", "Crédito", "Parcelas"])

    @app.route('/')
    def index():
        return render_template('index.html', name='Registro de Vendas')

    @app.route('/planilha_dia')
    def planilha_dia():
        data = []
        for row in ws.iter_rows(values_only=True):
            data.append(row)
        return render_template('planilha_dia.html', name='Planilha do dia', data=data, dia=f'{dia}/{mes}/{ano}')

    @app.route('/planilha_mes')
    def planilha_mes():
        data = []
        ws = wb['Soma']
        for row in ws.iter_rows(values_only=True):
            data.append(row)

        try:
            calculo_total(ws, wb)
        except Exception as e:
            print(f'Erro ao calcular o total. {e}')
            
        return render_template('planilha_mes.html', name='Planilha do mês', data=data, mes=f'{mesEscrito}/{ano}')

    @app.route('/troco')
    def troco():
        return render_template('troco.html', name='Registro de Troco')

    @app.route('/registro', methods=['POST'])
    def registro():
        valor = request.form['valor']
        metodo = request.form['metodo']
        if metodo == 'Credito':
            parcelas = request.form['parcelas']
            venda_C(ws, wb, total, valor, parcelas)
        else:
            venda_D(ws, wb, total, valor, metodo)
        return redirect(url_for('index'))

    @app.route('/registro_troco', methods=['POST'])
    def registro_troco():
        troco_dia_valor = request.form['troco']
        troco_mes_valor = request.form['troco_mes']
        if troco_mes_valor:
            troco_mes(ws, wb, troco_mes_valor,)
        if troco_dia_valor:
            troco_dia(ws, wb, troco_dia_valor, dia)
        return redirect(url_for('troco'))
