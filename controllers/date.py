from datetime import datetime, timedelta

def obter_data_atual():
    brasil_agora = datetime.utcnow() - timedelta(hours=3)
    dia = brasil_agora.day
    mes = brasil_agora.month
    ano = brasil_agora.year

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

    return dia, mes, ano, mesEscrito
