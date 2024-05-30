from flask import render_template, request, redirect, url_for, flash
from openpyxl import Workbook
from .date import obter_data_atual
from .functions import carregar_planilha, wb_ws_total, venda_D, venda_C, troco_dia, troco_mes, calculo_total

def register_routes(app):
    try:
        @app.errorhandler(Exception)
        def erro_pagina(erro):
            mensagem = 'Página não encontrada.'
            return render_template('erro.html', mensagem=mensagem), 404
        
        dia, mes, ano, mesEscrito = obter_data_atual()
        wb, ws, total = wb_ws_total()

        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/planilha_dia')
        def planilha_dia():
            data = []
            for row in ws.iter_rows(values_only=True):
                data.append(row)
            return render_template('planilha_dia.html', data=data, dia=f'{dia}/{mes}/{ano}')

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
                
            return render_template('planilha_mes.html', data=data, mes=f'{mesEscrito}/{ano}')

        @app.route('/troco')
        def troco():
            return render_template('troco.html')

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
            return redirect(url_for('planilha_mes'))
    except Exception as e:
        @app.errorhandler(Exception)
        def erro_carregar(erro):
            mensagem = f"Erro ao carregar dados da planilha. Feche o programa, verifique se a planilha está na pasta junto ao app.exe e tente novamente."
            return render_template('erro.html', mensagem=mensagem), 404