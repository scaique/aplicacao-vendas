from openpyxl import Workbook, load_workbook
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Pegando data atual
dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year

if mes == 1:
    mesEscrito = 'Janeiro'
elif mes == 2:
    mesEscrito = 'Fevereiro'
elif mes == 3:
    mesEscrito = 'Março'
elif mes == 4:
    mesEscrito = 'Abril'
elif mes == 5:
    mesEscrito = 'Maio'
elif mes == 6:
    mesEscrito = 'Junho'
elif mes == 7:
    mesEscrito = 'Julho'
elif mes == 8:
    mesEscrito = 'Agosto'
elif mes == 9:
    mesEscrito = 'Setembro'
elif mes == 10:
    mesEscrito = 'Outubro'
elif mes == 11:
    mesEscrito = 'Novembro'
elif mes == 12:
    mesEscrito = 'Dezembro'

# Carregando planilha
try:
    wb = load_workbook(f'./planilhas/{mesEscrito} {ano}.xlsx')
except FileNotFoundError:
    wb = Workbook()
    ws = wb.active
    ws.title = f'Dia {dia}'
    ws.append(["Dinheiro", "Débito", "Crédito", "Parcelas"])
    # wb = load_workbook(f'Base.xlsx')

# Acessando aba
try:
    ws = wb[f'Dia {dia}']
except:
    ws = wb.create_sheet(f'Dia {dia}')
    ws.append(["Dinheiro", "Débito", "Crédito", "Parcelas"]) #, "", "", "", "Dinheiro", "Débito", "Crédito", "", "Total", "", "Troco", "Retirada", "", "Troco Anterior"])
    # ws['H2'].value = '=SUM(A:A)'
    # ws['I2'].value = '=SUM(B:B)'
    # ws['J2'].value = '=SUM(C:C)'
    # ws['L2'].value = '=SUM(H2:J2)'
    # ws['O2'].value = '=H2+Q2-N2'

def salvar():
    try:
        wb.save(f'./planilhas/{mesEscrito} {ano}.xlsx')
    except PermissionError:
        print('Feche a planilha para salvar!')

def venda_D(valor, metodo):
    for c in range(1, 200):
        if metodo == 'Dinheiro':
            celula = ws[f'A{c}'].value
            if celula is None or celula == '':
                ws[f'A{c}'] = valor
                break
        elif metodo == 'Debito':
            celula = ws[f'B{c}'].value
            if celula is None or celula == '':
                ws[f'B{c}'] = valor
                break

    # Salvando arquivo
    wb.save(f'planilhas/{mesEscrito} {ano}.xlsx')

def venda_C(valor, parcelas):
    for c in range(1, 200):
        celula = ws[f'C{c}'].value
        if celula is None or celula == '':
            ws[f'C{c}'] = valor
            ws[f'D{c}'] = parcelas
            break
    
    # Salvando arquivo
    wb.save(f'planilhas/{mesEscrito} {ano}.xlsx')

@app.route('/')
def index():
    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(row)

    return render_template('index.html', data=data)

@app.route('/planilha')
def planilha():
    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(row)

    return render_template('planilha.html', data=data)

@app.route('/registro', methods=['POST'])
def registro():
    valor = request.form['valor']
    metodo = request.form['metodo']

    venda_D(valor, metodo)

    if metodo == 'Credito':
        parcelas = request.form['parcelas']
        venda_C(valor, parcelas)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

