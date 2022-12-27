from include import gerador
from config import System
Loop = True

if __name__ == '__main__':
    System.cls()
    System.main()
    while Loop:
        
        try:
            r = System.Cursor()
            if r == '!help' or r == '!h':
                print (System.cmds)
            elif r == '!clear' or r == '!c':
                System.cls()
                System.main()
            elif r == '!gerar' or r == '!g':
                site, login, senha = System.getpass()
                s = gerador.play(senha)
                result = f'Senha Criada:'+s
                print (result)
                System.singupDb(site, login, s)
            elif r == '!psave' or r == '!ps':
                site, login = System.getsite()
                s = System.readDb(site, login)
                print (f'Senha: '+s)
            elif r == '!exit' or r == '!quit':
                Loop = False
                exit()
            else:
                print (f'\033[0;33mComando: \033[0;31m',r ,f'\033[0;33m, Invalido!\033[0;m')
        except:
            print (f'\033[0;31mExit...\033[0;m')
            
