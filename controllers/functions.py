from openpyxl import load_workbook
from .date import obter_data_atual

mesEscrito = obter_data_atual()[3]
ano = obter_data_atual()[2]

def carregar_planilha():
    try:
        wb = load_workbook(f'./planilhas/{mesEscrito} {ano}.xlsx', data_only=True)
    except FileNotFoundError:
        wb = load_workbook(f'Base.xlsx', data_only=True)
    return wb

def salvar(wb):
    try:
        wb.save(f'./planilhas/{mesEscrito} {ano}.xlsx')
    except PermissionError:
        print('Feche a planilha para salvar!')

def venda_D(ws, wb, total, valor, metodo):
    valor = int(valor)
    for c in range(1, 200):
        if metodo == 'Dinheiro':
            celula = ws[f'A{c}'].value
            if celula is None or celula == '':
                ws[f'A{c}'] = valor
                total['Dinheiro'].value += valor
                total['Total'].value += valor
                break
        elif metodo == 'Debito':
            celula = ws[f'B{c}'].value
            if celula is None or celula == '':
                ws[f'B{c}'] = valor
                total['Debito'].value += valor
                total['Total'].value += valor
                break
    salvar(wb)

def venda_C(ws, wb, total, valor, parcelas):
    valor = int(valor)
    for c in range(1, 200):
        celula = ws[f'C{c}'].value
        if celula is None or celula == '':
            ws[f'C{c}'] = valor
            ws[f'D{c}'] = parcelas
            total['Credito'].value += valor
            total['Total'].value += valor
            break
    salvar(wb)

def troco_dia(ws, wb, valor, dia):
    ws = wb['Soma']
    ws[f'H{dia+1}'] = valor
    ws[f'H{dia+2}'] = valor
    salvar(wb)

def troco_mes(ws, wb, valor):
    valor = int(valor)
    ws = wb['Soma']
    ws['K2'] = valor
    ws['H2'] = valor
    salvar(wb)

def calculo_total(ws, wb):
    ws = wb['Soma']
    if ws['B2'].value is not None and ws['H2'].value is not None and ws['K2'].value is not None:
        total_dia1 = ws['B2'].value + ws['H2'].value - ws['K2'].value
        ws['I2'] = total_dia1

    for c in range(3, 33):
        if ws[f'B{c}'].value is not None and ws[f'H{c-1}'].value is not None and ws[f'H{c}'].value is not None:
            retirada = int(ws[f'B{c}'].value) + int(ws[f'H{c-1}'].value) - int(ws[f'H{c}'].value)
            ws[f'I{c}'] = retirada
    
    total_mes = 0
    
    for c in range(2, 33):
        if ws[f'I{c}'].value is not None:
            total_mes += int(ws[f'I{c}'].value)
            ws['I33'].value = total_mes

    salvar(wb)
