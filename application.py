#Trabalho Cloud (Aplicação Simples que busca um "Movie Quote no MySQL e apresenta na Tela")


#Importanto das Bibliotecas
from mysql import connector
from flask import Flask
from random import randint

application = Flask(__name__)


@application.route("/")
def index():
    
    #Conexão com o BD MySQL na Nuvem
    cnx = connector.connect(user='admin', password='TaTxMe123', host='dbmovies.cthpl6d1wkbm.us-east-1.rds.amazonaws.com', database='dbmovies')
    cursor = cnx.cursor()
    
    rand_id = randint(1, 33)
    
    query = ("SELECT * FROM movie_quotes WHERE ID= %s")
    cursor.execute(query, (rand_id,))

    row = cursor.fetchone()
    cursor.close()
    cnx.close()
    
    page = ("<html><title>49BDT Fiap Trabalho Cloud</title><body align=center>" + 
            "<br><br><br><br><br><br><br><br>" +
            "<h1>" + row[1] + 
            "</h1><br><h3><i>" + row[2] + "</i></h3>" +
            "<br><br><button onClick='window.location.href=window.location.href'>Mais um!</button>"
            "</body></html>")

    return page
    

if __name__ == '__main__':
    application.run()


