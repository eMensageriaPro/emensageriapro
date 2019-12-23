#coding:utf-8
import os

def ler_arquivo(arquivo):
    file = open(arquivo, 'r')
    texto = file.read()
    file.close()
    return texto

pastas = [
    'esocial/v02_04_02/', 
    'esocial/v02_05_00/', 
    'efdreinf/v1_04_00/',
    'efdreinf/v1_03_02/'
]


def get_xmlns(arquivo):

    texto = ler_arquivo(p + a)
    b = texto.split('xmlns="')
    c = b[1].split('"')
    return c[0]


def get_name(arquivo):

    texto = ler_arquivo(p + a)
    if 'name="evt' in texto:
        b = texto.split('name="evt')
        c = b[1].split('"')
        return 'evt' + c[0]
    elif 'name="retorno' in texto:
        b = texto.split('name="retorno')
        c = b[1].split('"')
        return 'retorno' + c[0]
    elif 'name="lote' in texto:
        b = texto.split('name="lote')
        c = b[1].split('"')
        return 'lote' + c[0]

for p in pastas:
    
    arquivos = os.listdir(p)
    
    for a in arquivos:

        if '.xsd' in a and ('xmldsig' not in a) and a[0] != '.':

            #print a
        
            xmlns = get_xmlns(p + a)
            name = get_name(p + a)

            file_old = p + a
            file = p + name + '.xsd'

            print 'mv %s %s' % (file_old, file)

            os.system('mv %s %s' % (file_old, file))
        

