import mysql.connector

def conectar():
    return mysql.connector.connect(
    host='localhost',
    user='root',
    password='****',
    database="ecommerce"
)

def inserir_venda(produto,categoria,valor,data_venda,cliente):
    conexao=conectar()
    cursor = conexao.cursor()
    comando ='INSERT INTO vendas(produto,categoria,valor,data_venda,cliente)VALUES(%s,%s,%s,%s,%s)'
    valores=(produto,categoria,valor,data_venda,cliente)
    cursor.execute(comando,valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_vendas():
    conexao = conectar()
    cursor= conexao.cursor()
    cursor.execute('SELECT* FROM vendas')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def deletar_venda(id):
    conexao= conectar()
    cursor= conexao.cursor()
    cursor.execute ("DELETE FROM vendas WHERE ID= %s",(id,))
    conexao.commit()
    cursor.close()
    conexao.close()

def editar_venda(id,produto,categoria, valor, data_venda,cliente):
    conexao=conectar()
    cursor=conexao.cursor()
    comando='''UPDATE vendas SET produto = %s,
    categoria= %s,
    valor= %s,
    data_venda= %s,
    cliente= %s
    WHERE id= %s
      '''

    valores=(produto,categoria,valor,data_venda,cliente,id)
    cursor.execute(comando,valores)
    conexao.commit()
    cursor.close()
    conexao.close
