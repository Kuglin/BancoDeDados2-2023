import mysql.connector
import time

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='cidade_estado_pais'
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Armazenar o tempo de início
tempo_inicio = time.time()

# Executar a consulta SQL e criar a nova tabela
consulta_criar_tabela = '''
CREATE TABLE empresas_acima_media AS
SELECT * FROM companies_sorted WHERE `total employee estimate` > (SELECT AVG(`total employee estimate`) FROM companies_sorted);
'''

cursor.execute(consulta_criar_tabela)

# Commit para efetivar as alterações no banco de dados
conexao.commit()

# Armazenar o tempo de término
tempo_fim = time.time()

# Calcular e imprimir o tempo de execução
tempo_execucao = tempo_fim - tempo_inicio
print(f"Tempo de execução: {tempo_execucao} segundos")

# Fechar o cursor e a conexão
cursor.close()
conexao.close()