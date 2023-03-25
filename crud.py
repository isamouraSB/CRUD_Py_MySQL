import mysql.connector
#informações da conta e banco de dados mysql
conexao = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="2511",
    database="bd_crud",
)

cursor = conexao.cursor()

#CRUD - CREATE
Nome_Produto = "BATATA"
Descricao_Produto = "PURE"
Fornecedor_Produto = "AMBEV"
Estoque_Produto = "5"
Valor_Produto = "15,50"

comando = 'INSERT INTO produtos (Nome_Produto, Descricao_Produto, Fornecedor_Produto, Estoque_Produto, Valor_Produto) VALUES ("{Nome_Produto}", "{Descricao_Produto}", "{Fornecedor_Produto}", "{Estoque_Produto}", "{Valor_Produto}")' # Escreve o comando 1
cursor.execute(comando) #Executar o comando 2
conexao.commit() #Edita o banco de dados 
#resultado = cursor.fetchall() #Ler\armazenar o banco de dados 



#Fechando a conexão
cursor.close()
conexao.close()


# READ
# UPDATE
# DELETE
