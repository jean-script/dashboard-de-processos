from time import time
from django.db import models
from datetime import datetime
from Empresas.models import Empresa
from django.contrib.auth.models import User
import mysql.connector

# Create your models here.
agora = datetime.now()

data_hoje = agora.strftime('%Y-%m-%d')

class Processos(models.Model):

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # campo de texto
    nome_processo = models.CharField(max_length=200)
    # textarea campo com mais caracteres
    descrisao = models.TextField(max_length=200)
    status = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=True)
    # deixar já o processo no dashboard
    publicado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_processo

  
class LogsDoProcesso(models.Model):

    processo_nome = models.ForeignKey(Processos, on_delete=models.CASCADE)
    transaction_Number = models.CharField(max_length=200, blank=True)
    transaction_Item = models.CharField(max_length=200, blank=True)
    transaction_status = models.CharField(max_length=200, blank=True)
    data_execucao = models.CharField(max_length=200, default=data_hoje, blank=True)
    tempo_execucao = models.CharField(max_length=200, blank=True)
    # inicio_execucao
    # resultado
    # 

    def __str__(self):
        return str(self.processo_nome)

def criando_tabela_log(id_processo, nome_processo):

    try:
        # gereando a coneção
        conexao = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            password = 'Iw7twjsPtk',
            database ='practiapap'
        )

        cursor = conexao.cursor()
        print("Conexao feita")
        print(nome_processo)
        # executando comando
        comando_insert = 'CREATE TABLE {} (ID INT NOT NULL AUTO_INCREMENT, transaction_number VARCHAR(100), transaction_item VARCHAR(100),transaction_status VARCHAR(100),PRIMARY KEY (ID))'.format(nome_processo)
        cursor.execute(comando_insert)
        conexao.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexao.close()

# tabela valida, parei aqui

# processos.brasil@practia.global
