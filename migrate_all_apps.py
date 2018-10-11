#coding:utf-8
import os
from datetime import datetime
from emensageriapro.padrao import ler_arquivo
from emensageriapro.settings import INSTALLED_APPS




def executar_sql(select, array):
    import psycopg2
    from emensageriapro.settings import DATABASES
    database = DATABASES['default']
    try:
        conn = psycopg2.connect("user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s' dbname='%(NAME)s'" % database)
        conn.autocommit = True
    except:
        print "I am unable to connect to the database"
    if select:
        cur = conn.cursor()
        select = select.replace("'Null'", 'Null')
        # print select
        cur.execute(select)
        if array: lista = cur.fetchall()
        else: lista = None
        cur.close()
        return lista
    else:
        return None


def cadastro_controle_acesso():
    texto = ler_arquivo('paginas.txt')
    texto = texto.replace('\n\n', '\n')
    lista = texto.split('\n')
    lista_paginas = []
    for l in lista:
        if len(l.strip()):
            d = l.split('|')
            dados = {}
            dados['modulo'] = d[0]
            dados['modulo_slug'] = d[1]
            dados['pagina'] = d[2]
            dados['pagina_slug'] = d[3]
            verif_modulo = executar_sql("""
            
            SELECT id, titulo, slug, ordem, criado_em, modificado_em, excluido, 
                   criado_por_id, modificado_por_id, modulo_pai_id
              FROM public.config_modulos WHERE slug='%(modulo_slug)s';
      
            """ % dados, True)
            if not verif_modulo:
                verif_modulo = executar_sql("""

                        INSERT INTO public.config_modulos(
                                    titulo, slug, ordem, criado_em, modificado_em, excluido, 
                                    criado_por_id, modificado_por_id, modulo_pai_id)
                            VALUES ('%(modulo)s', '%(modulo_slug)s', 0, now(), now(), False, 
                                    1, 2, Null) RETURNING id;

                        """ % dados, True)
            dados['modulo_id'] = verif_modulo[0][0]

            verif_pagina = executar_sql("""
            
            SELECT id, titulo, endereco, exibe_menu, tipo, ordem, criado_em, modificado_em, 
                   excluido, config_modulos_id, criado_por_id, modificado_por_id
              FROM public.config_paginas WHERE endereco='%(pagina_slug)s';

                    """ % dados, True)
            if not verif_pagina:
                verif_pagina = executar_sql("""

                    INSERT INTO public.config_paginas(
                                titulo, endereco, exibe_menu, tipo, ordem, criado_em, modificado_em, 
                                excluido, config_modulos_id, criado_por_id, modificado_por_id)
                        VALUES ('%(pagina)s', '%(pagina_slug)s', 0, 0, 0, now(), now(), 
                                False, %(modulo_id)s, 1, 1);

                                """ % dados, False)
            lista_paginas.append("'"+dados['pagina_slug']+"'")

    executar_sql("""
    DELETE FROM config_permissoes 
    WHERE config_paginas_id IN (
    SELECT id FROM config_paginas WHERE endereco NOT IN (%s)
        );""" % ','.join(lista_paginas), False)

    executar_sql("""
    DELETE FROM config_paginas WHERE endereco NOT IN (%s);
        """ % ','.join(lista_paginas), False)

    print "Controle de acesso atualizado com sucesso!"



lista = [
    'mensageiro',
    'efdreinf',
    'esocial',
    'tabelas',
    'controle_de_acesso',
    's1000',
    's2200',
    's1030',
    's1202',
    's2240',
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
    's1005',
    's1010',
    's1020',
    's1035',
    's1040',
    's1050',
    's1060',
    's1065',
    's1070',
    's1080',
    's1200',
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
    's2205',
    's2206',
    's2210',
    's2220',
    's2221',
    's2230',
    's2231',
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

def migrates():

    data_inicio = datetime.now()

    os.system('python manage.py migrate auth')
    os.system('python manage.py migrate contenttypes')
    os.system('python manage.py migrate sessions')
    os.system('python manage.py makemigrations --merge')

    for a in INSTALLED_APPS:

        if 'emensageriapro' in a:
            a = a.replace('emensageriapro.', '')

            for c in ['makemigrations','migrate']:
                print ''
                comando = 'python manage.py %s %s' % (c, a)
                print "Executando: "+comando
                os.system(comando)


    data_fim = datetime.now()
    print 'Inicio:', data_inicio
    print 'Termino:', data_fim
    print 'Tempo decorrido:', data_fim - data_inicio


if __name__ == "__main__":
    cadastro_controle_acesso()
    migrates()

