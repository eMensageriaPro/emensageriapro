#coding:utf-8
import os
from datetime import datetime
data_inicio = datetime.now()

lista = [
    'mensageiro',
    'efdreinf',
    'esocial',
    'tabelas',
    'controle_de_acesso',
    'r1000',
    'r1070',
    'r2010',
    'r2020',
    'r2030',
    'r2040',
    'r2050',
    'r2060',
    'r2070',
    'r2098',
    'r2099',
    'r3010',
    'r5001',
    'r5011',
    'r9000',
    's1000',
    's1005',
    's1010',
    's1020',
    's1030',
    's1035',
    's1040',
    's1050',
    's1060',
    's1065',
    's1070',
    's1080',
    's1200',
    's1202',
    's1207',
    's1210',
    's1250',
    's1260',
    's1270',
    's1280',
    's1295',
    's1298',
    's1299',
    's1300',
    's2190',
    's2200',
    's2205',
    's2206',
    's2210',
    's2220',
    's2230',
    's2231',
    's2240',
    's2241',
    's2245',
    's2250',
    's2260',
    's2298',
    's2299',
    's2300',
    's2306',
    's2399',
    's2400',
    's2405',
    's2410',
    's2416',
    's2420',
    's3000',
    's5001',
    's5002',
    's5011',
    's5012',
]


os.system('python manage.py migrate auth')
os.system('python manage.py migrate contenttypes')
os.system('python manage.py migrate sessions')

#os.system('python manage.py makemigrations --merge')

for a in lista:
    print ''
    comando = 'python manage.py makemigrations '+a
    print "Executando: "+comando
    os.system(comando)
    print ''
    comando = 'python manage.py migrate '+a
    print "Executando: "+comando
    os.system(comando)


data_fim = datetime.now()
print 'Inicio:', data_inicio
print 'Termino:', data_fim
print 'Tempo decorrido:', data_fim - data_inicio


#CommandError: Conflicting migrations detected (0017_auto_20180819_2200, 0013_merge in mensageiro; 0004_auto_20180820_0502, 0003_merge in s1200).
#To fix them run 'python manage.py makemigrations --merge'