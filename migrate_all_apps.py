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


def reset_sequences():

    results = executar_sql("""
        select table_name 
        from information_schema.tables 
        where table_schema='public' 
        and table_name not like 'django_%'
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

    arquivos = os.listdir('sql_tabelas')

    for a in arquivos:

        if '.sql' in a:

            try:

                TXT = ler_arquivo('sql_tabelas/%s' % a)
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
    cadastro_controle_acesso()
    update_tables()
    criar_diretorio_arquivos()

