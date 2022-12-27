import os
import time
import sqlite3

banco = sqlite3.connect('config/.DataBase/Banco.db',check_same_thread=False)
cursor = banco.cursor()
sql = 'SELECT * FROM dados WHERE site = ? and login = ? '

def getsite():
    print ('\033[0;32Digite o Site que Voce Criou a conta!\033[0;m')
    site = Cursor()
    print ('\033[0;32mDigite o Login!\033[0;m')
    login = Cursor()
    return site, login



def singupDb(site, login, senha):
    cursor.execute("CREATE TABLE IF NOT EXISTS dados (id integer PRIMARY KEY AUTOINCREMENT, site text, login text,  senha text) ")
    cursor.execute(f"INSERT INTO dados (site, login, senha) VALUES(?, ?, ?)", (site, login, senha))
    banco.commit()
 
def readDb(site,login):
    for row in cursor.execute(sql, (site, login)):
        id = row[0]
        site = row[1]
        login = row[2]
        senha = row[3]
        return  senha
    

cmds = '''
\033[0;32mComandos:\033[0;33m
        \033[0;31m!\033[0;33mclear
        \033[0;31m!\033[0;33mgerar
        \033[0;31m!\033[0;33mpsave
        \033[0;31m!\033[0;33mhelp
        \033[0;31m!\033[0;33mexit\033[0;m
        '''
def getpass():
    
    print ('\033[0;32mDigite o site que deseja criar a conta!\033[0;m')
    r = Cursor()
    print ('\033[0;32mDigite o login que deseja!\033[0;m')
    l = Cursor()
    print ('\033[0;32mDigite uma senha!\033[0;m')
    s = Cursor()
    return r, l, s

def cls():
    os.system('clear')

def Cursor():
    c = input(str('\033[0;31m[\033[0;33mPasswordSecuryt\033[0;31m]\033[0;m'))
    return c
    
def main():
    text = '''\033[0;32m
Esta Ferramenta Gera Uma Senha Encima De Outra Senha
 As Senhas Criadas Ficarão Salvas
Em Caso De Duvidas Digite \033[0;33m!help
\033[0;m
    '''
    print (text)
    
    
if __name__ == '__main__':
    singupDb('test.com','loocktst', 'loock')