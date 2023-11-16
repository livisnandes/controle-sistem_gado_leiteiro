# Importar bibliotecas necessárias
import datetime
import random
import sqlite3

# Conectar ao banco de dados (substitua 'nome_do_banco.db' pelo nome do seu banco de dados)
conn = sqlite3.connect('nome_do_banco.db')
c = conn.cursor()

# Função para adicionar um novo registro de produção de leite
def adicionar_registro_producao(id_gado, quantidade_leite):
    data_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO producao_leite (id_gado, data_registro, quantidade_leite) VALUES (?, ?, ?)",
              (id_gado, data_registro, quantidade_leite))
    conn.commit()
    print(f"Registro de produção de leite adicionado para o gado {id_gado}.")

# Função para consultar a produção de leite por período
def consultar_producao_por_periodo(data_inicial, data_final):
    c.execute("SELECT * FROM producao_leite WHERE data_registro BETWEEN ? AND ?",
              (data_inicial, data_final))
    rows = c.fetchall()
    for row in rows:
        print(row)

# Exemplo de uso das funções
id_gado = 1  # Substitua pelo ID do seu gado
quantidade_leite = random.uniform(10, 30)  # Quantidade de leite produzida (um exemplo aleatório)
adicionar_registro_producao(id_gado, quantidade_leite)

# Consultar produção de leite para o último mês
data_atual = datetime.datetime.now()
data_inicial = (data_atual - datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
data_final = data_atual.strftime("%Y-%m-%d %H:%M:%S")
consultar_producao_por_periodo(data_inicial, data_final)

# Fechar a conexão com o banco de dados
conn.close()
