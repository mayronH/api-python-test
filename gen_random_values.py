#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte2.html
import random
import rstr
import datetime

#Gera data entre 10 - 80 anos
def gen_age():
    return random.randint(10, 80)

#Gera CPF com os digitos 1234567890, 11 digitos
def gen_cpf():
    return rstr.rstr('1234567890', 11)

#Gera telefone no formato (00) 90000 - 0000
def gen_phone():
    return '({0}) 9{1} - {2}'.format(rstr.rstr('1234567890', 2),
                                    rstr.rstr('1234567890', 4),
                                    rstr.rstr('1234567890', 4))

def gen_timestamp():
    year = random.randint(1980, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    #Retorna no formato yyyy-mm-ddThh:mm:ss.000000 isoformat retira o T
    date = datetime.datetime(year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date

def gen_city():
    list_city = [
        [u'Timóteo', 'MG'],
        [u'Coronel Fabriciano', 'MG'],
        [u'Ipatinga', 'MG'],
        [u'Belo Horizonte', 'MG'],
    ]
    #Pega um valor aleatório dentro da lista
    return random.choice(list_city)