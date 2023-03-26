import mysql.connector
#informações da conta e banco de dados mysql
conexao = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="2511",
    database="bd_crud",
)
cursor = conexao.cursor()

#CRUD ALTERAÇÕES


#Fechando a conexão
cursor.close()
conexao.close()

# CREATE\ CRIAR
Nome_produtos = "Banana"
Descr_produtos = "Pure de batata preparada com muito amor"
Fornecedor_produtos = "AMBEV"
Estoque_produtos = 5
Valor_produtos = 15
comando = f'INSERT INTO produtos (Nome_produtos, Descr_produtos, Fornecedor_produtos, Estoque_produtos, Valor_produtos) VALUES ("{Nome_produtos}", "{Descr_produtos}", "{Fornecedor_produtos}", "{Estoque_produtos}", "{Valor_produtos}")'
cursor.execute(comando) #Executar o comando 2
conexao.commit() #Edita o banco de dados 


# READ
comando = f'SELECT * FROM produtos' # Solicitar exibição dos resultados 
cursor.execute(comando) #Executar o comando 2
resultado = cursor.fetchall() #Ler\armazenar o banco de dados 
print(resultado) #Exibir o resultado


# UPDATE
Cod_produtos = 2
Valor_produtos = 12
comando = f'UPDATE produtos SET Valor_produtos = {Valor_produtos} WHERE Cod_produtos = "{Cod_produtos}"' # Alterar valores da tabela
cursor.execute(comando) #Executar o comando 2
conexao.commit() #Edita o banco de dados 


# DELETE
Cod_produtos = 3
comando = f'DELETE FROM produtos WHERE Cod_produtos = "{Cod_produtos}"' # Deletar linha de tabela
cursor.execute(comando) #Executar o comando 2
conexao.commit() #Edita o banco de dados 
