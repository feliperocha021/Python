"""
O Python possui o módulo datetime, que fornece classes e funções para manipular datas, horários e intervalos de tempo. Com ele, você pode:

Criar objetos de data (date), hora (time) e data+hora (datetime).

Obter a data e hora atuais.

Fazer operações com intervalos de tempo usando timedelta.

Formatar datas em diferentes padrões (strftime).

Converter strings em datas (strptime).

Trabalhar com fusos horários (com timezone ou bibliotecas externas como pytz e zoneinfo).
"""

import datetime

now = datetime.datetime.now()
print("Now:", now)

today = datetime.date.today()
print("Today:", today)

d = datetime.date(2025, 10, 8)  # year, month, day
t = datetime.time(14, 30, 0)    # hour, minute, second
dt = datetime.datetime(2025, 10, 8, 14, 30, 0)

print("Date:", d)
print("Time:", t)
print("Datetime:", dt)

print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%A, %B %d, %Y"))

today = datetime.date.today()
future = today + datetime.timedelta(days=10)
past = today - datetime.timedelta(days=5)

print("Today:", today)
print("10 days later:", future)
print("5 days ago:", past)

utc_now = datetime.datetime.now(datetime.timezone.utc)
br_time = utc_now.astimezone(datetime.timezone(datetime.timedelta(hours=-3)))

print("UTC:", utc_now)
print("Brasília:", br_time)
