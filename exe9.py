import datetime as dt
dt = dt.datetime.now()

i = int(input('Idade: '))
i = dt.year - i
print('Ano de nascimento:',i)