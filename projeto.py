import pandas as pd
import sqlite3

# Criando a conexão com o banco de dados
conn = sqlite3.connect('dev_network.db')

# Inserindo dados das empresas
empresas_data = {
    'nome': ['Amplifi Toon', 'Wayne Enterprises'],
    'email': ['amplifitoon@gmail.com', 'contato@wayneent.com'],
    'senha': ['123456amplifiers', 'batmanrules'],
    'descricao': ['Nós somos uma empresa com o objetivo de trazer as melhores soluções para os clientes desde 1999.', 'Empresa multinacional de tecnologia e investimentos fundada por Thomas Wayne.'],
    'titulo': ['Empresa de Software', 'Indústria de Tecnologia'],
    'localizacao': ['Rio de Janeiro, Brasil', 'Gotham City, EUA']
}

empresas_df = pd.DataFrame(empresas_data)
empresas_df.to_sql('tbl_empresa', conn, if_exists='append', index=False)

# Inserindo dados dos usuários
usuarios_data = {
    'nome': ['Maria Fernanda'],
    'email': ['mariafernanda@hotmail.com'],
    'senha': ['senha123'],
    'descricao': ['Sou formada em Design Gráfico e trabalho com UI/UX há 5 anos.'],
    'titulo': ['Designer de UI/UX'],
    'stacks': ['Figma, Sketch, Adobe Creative Suite'],
    'telefone': ['+5511987654321'],
    'mora_em': ['São Paulo, Brasil'],
    'id_empresa': [2]
}

usuarios_df = pd.DataFrame(usuarios_data)
usuarios_df.to_sql('tbl_usuario', conn, if_exists='append', index=False)

# Inserindo vagas
oportunidades_data = {
    'titulo': ['Vaga de Desenvolvedor Pleno PHP'],
    'descricao': ['Vaga para devs proficientes e que trabalhem em times.'],
    'salario': [2000.00],
    'modo_de_trabalho': ['híbrido'],
    'id_empresa': [2]
}

oportunidades_df = pd.DataFrame(oportunidades_data)
oportunidades_df.to_sql('tbl_oportunidade', conn, if_exists='append', index=False)

# Inserindo aplicações
aplicacoes_data = {
    'id_usuario': [2],
    'id_oportunidade': [1]
}

aplicacoes_df = pd.DataFrame(aplicacoes_data)
aplicacoes_df.to_sql('tbl_aplicacao', conn, if_exists='append', index=False)

# Executando as consultas
consulta1 = '''
    SELECT tbl_usuario.nome, tbl_usuario.titulo, tbl_empresa.nome AS 'Nome da Empresa'
    FROM tbl_usuario
    INNER JOIN tbl_empresa ON tbl_usuario.id_empresa = tbl_empresa.id
'''

consulta2 = '''
    SELECT tbl_aplicacao.id AS 'Id da Aplicação', tbl_usuario.nome AS 'Quem se Aplicou para a Vaga', tbl_oportunidade.titulo AS 'Titulo da Vaga', tbl_oportunidade.salario AS 'Salario da Vaga'
    FROM tbl_aplicacao
    INNER JOIN tbl_usuario ON tbl_usuario.id = tbl_aplicacao.id_usuario
    JOIN tbl_oportunidade ON tbl_oportunidade.id = tbl_aplicacao.id_oportunidade
'''

resultado1 = pd.read_sql_query(consulta1, conn)
print(resultado1)

resultado2 = pd.read_sql_query(consulta2, conn)
print(resultado2)

# Fechando a conexão com o banco de dados
conn.commit()
conn.close()