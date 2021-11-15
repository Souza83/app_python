# Data, horário e relacionar datas diferentes

from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime (2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=10, seconds=12)
    print(nova_data)

def trabalhando_com_data():
    data_atual = date.today()
    print(data_atual)
    print(type(data_atual))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_hora():
    horario = time(hour=15, minute=30, second=45)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))


if __name__ == '__main__':
    #trabalhando_com_data()
    #print('\n')
    #trabalhando_com_hora()
    #print('\n')
    trabalhando_com_datetime()