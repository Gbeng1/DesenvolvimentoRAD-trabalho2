import os

class Alunos:
    
    #------------- iniciador-----------------------------
    
    def __init__(self):
        self.lista = []
        
        if os.path.exists("dados.txt"):
            with open("dados.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    self.lista.append(linha.strip())
                    
                    
    #-------------salvar-----------------------------------
                    
                    
    def salvar(self):
        with open("dados.txt", "w", encoding="utf-8") as arquivo:
            for aluno in self.lista:
                arquivo.write(aluno + "\n")
             
        
    #-------------inserir aluno--------------------------

    def inserir(self):
        nome = input("Digite o nome: ")
        self.lista.append(nome)
        self.salvar()
        print("Aluno cadastrado!")
        
    #--------------exibir lista de alunos ---------------
    
    def exibir(self):
        if len(self.lista) == 0:
            print("Lista vazia!")
        else:
            for i, aluno in enumerate(self.lista):
                print(f"{i+1}) aluno {aluno}")
    
    #--------------alterar nome de aluno-----------------
    
    def alterarnome(self):
        if len(self.lista) == 0:
            print("Lista Vazia!")
            return
        else:
            for i, aluno in enumerate(self.lista):
                print(f"{i+1}) aluno {aluno}")
            
        try:
            selecionen = int(input("Digite o número do aluno que deseja modificar: "))
            
            if selecionen > len(self.lista) or selecionen < 1:
                print("Invalido!")
                print(f"Digite de 1 a {len(self.lista)}")
                
            else:
                novonome = input("Digite o novo nome: ")
                self.lista[selecionen - 1] = novonome
                self.salvar()
                print("Cadastro alterado!")
                
        except ValueError:
            print("Invalido!")
            print(f"Digite de 1 a {len(self.lista)}")
    
    #----------------apagar lista--------------------------
            
    def excluir(self):
        if len(self.lista) == 0:
            print("Lista vazia!")
        else:
            resposta = str(input("Deseja apagar todos os alunos ? (s/n): ")).lower()
            if resposta == "s":
                self.lista.clear()
                self.salvar()
                print("Lista apagada!")
            else:
                if resposta == "n":
                    return 
                else:
                    if resposta != "s" and resposta != "n":
                        print("Invalido!")
                        print("Digite s para sim e n para não")
                        
    #-------------------excluir cadastro----------------------
                        
    def excluir_nome(self):
        try:
            if len(self.lista) == 0:
                print("Lista vazia!")
            else:
                for i, aluno in enumerate(self.lista):
                    print(f"{i+1}) aluno {aluno}")
                selecioneex = int(input(f"Digite de 1 a {len(self.lista)}: "))
                if selecioneex < 1 or selecioneex > len(self.lista):
                    print("Inválido!")
                    print(f"Digite de 1 a {len(self.lista)} ")
                else:
                    self.lista.pop(selecioneex - 1)
                    self.salvar()
                    print("Cadastro apagado!")
        except ValueError:
            print("Digite apenas números")   
                
                
                
        

sistema = Alunos()


#--------------------menu------------------------------


def menu():

    while True:

        try:

            selecione = int(input("""
1) Inserir aluno
2) Exibir todos alunos
3) Alterar nome do aluno
4) Excluir todos os alunos
5) Excluir aluno pelo número
6) Sair

Digite: """))

            if selecione > 6 or selecione < 1:
                print("Inválido!")
                print("Digite de 1 a 6")

            elif selecione == 1:
                sistema.inserir()

            elif selecione == 2:
                sistema.exibir()
                
            elif selecione == 3:
                sistema.alterarnome()
                
            elif selecione == 4:
                sistema.excluir()
                
            elif selecione == 5:
                sistema.excluir_nome()

            elif selecione == 6:
                break

        except ValueError:
            print("Inválido!")
            print("Digite apenas números.")


if __name__ == '__main__':
    menu()