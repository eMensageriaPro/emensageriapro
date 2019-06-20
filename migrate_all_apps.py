#coding:utf-8
import os
from datetime import datetime
from emensageriapro.padrao import ler_arquivo
from emensageriapro.settings import INSTALLED_APPS, BASE_DIR

# Função para MAC OS X  não estrar em repouso
# pmset noidle


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



def reset_sequences():

    results = executar_sql("""
        select table_name 
        from information_schema.tables 
        where table_schema='public' 
        and table_name not like 'django_%' 
        and table_name != 'authtoken_token'
        and table_name != 'usuarios';
        """, True)

    for row in results:

        nome_tabela = row[0]
        results_1 = executar_sql("""SELECT max(id)+1 FROM %s;""" % (nome_tabela), True)
        quant = results_1[0][0] or 1
        try:
            executar_sql("""ALTER SEQUENCE %s_id_seq RESTART WITH %s;""" % (nome_tabela, quant), False)
        except:
            pass


def migrates():

    data_inicio = datetime.now()

    os.system('python manage.py migrate auth')
    os.system('python manage.py migrate contenttypes')
    os.system('python manage.py migrate sessions')
    os.system('python manage.py migrate authtoken')
    os.system('python manage.py migrate django_cron')
    os.system('python manage.py makemigrations --merge')

    for a in INSTALLED_APPS:

        if 'emensageriapro' in a:
            a = a.replace('emensageriapro.', '')

            for c in ['migrate']:
                print ''
                comando = 'python manage.py %s %s' % (c, a)
                print "Executando: "+comando
                os.system(comando)


    data_fim = datetime.now()
    print 'Inicio:', data_inicio
    print 'Termino:', data_fim
    print 'Tempo decorrido:', data_fim - data_inicio


def criar_diretorio_arquivos():

    from emensageriapro.settings import BASE_DIR
    lista = [
        'arquivos/Comunicacao/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/header/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/request/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/response/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/header/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/request/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/response/',
        'arquivos/Comunicacao/RecepcaoLoteReinf/',
        'arquivos/Comunicacao/ConsultasReinf/',
        'arquivos/Comunicacao/RecepcaoLoteReinf/header/',
        'arquivos/Comunicacao/RecepcaoLoteReinf/request/',
        'arquivos/Comunicacao/RecepcaoLoteReinf/response/',
        'arquivos/Comunicacao/ConsultasReinf/header/',
        'arquivos/Comunicacao/ConsultasReinf/request/',
        'arquivos/Comunicacao/ConsultasReinf/response/',
    ]
    for a in lista:
        if not os.path.isdir(a):
            os.system('mkdir -p %s/%s' % (BASE_DIR,a ) )

def update_tables():

    arquivos = os.listdir('%s/database/sql' % BASE_DIR)

    for a in arquivos:
        if '.sql' in a:
            try:
                TXT = ler_arquivo('database/sql/%s' % (a))
                executar_sql(TXT, False)
                print ('Arquivo %s executado com sucesso!' % a)

            except:
                print ('Erro ao executar o arquivo %s!' % a)

    arquivos = os.listdir('%s/database/views' % BASE_DIR)

    for a in arquivos:
        if '.sql' in a:
            
            try:
                TXT = ler_arquivo('database/views/%s' % (a))
                executar_sql(TXT, False)
                print ('Arquivo %s executado com sucesso!' % a)

            except:
                print ('Erro ao executar o arquivo %s!' % a)


def collect_static():

    print ''
    comando = 'python manage.py collectstatic'
    print "Executando: " + comando
    os.system(comando)


if __name__ == "__main__":

    collect_static()
    migrates()
    reset_sequences()
    update_tables()
    criar_diretorio_arquivos()

