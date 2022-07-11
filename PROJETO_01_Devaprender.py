from datetime import date, datetime
from colorama import Fore, Back, Style
import random
import sys, os




''' Funcionalidades do módulo 1

        1. Obtenha o nome do usuário

        2. Obtenha a idade do usuário

        3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

        4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:

        5. cartoes = ['R$50,00','R$250,00','R$120,00']
        
        6. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa) '''


class Funcionarios:
    'Classe de cadastro de funcionários'
    def __init__(self):
        self.cartoes = ['R$50,00','R$250,00','R$120,00']
        self.numero_registro = []
        self.lista_nomes = []
        self.lista_idade = []
        self.lista_aniversario = []
        self.banco_de_dados = {} 

    def start(self):
        os.system('cls')
        print(Fore.WHITE)
        print('------------------------------------------------------------------------')
        print(Style.RESET_ALL)
        print(Fore.YELLOW)
        print('\n----------Bem Vindo ao Registrador de Novos Funcionários!!!----------\n')
        print(Style.RESET_ALL)
        print(Fore.WHITE)
        print('-------------------------------------------------------------------------')
        print(Style.RESET_ALL)

    def recebe_dados_do_usuario(self):     
        self.nome_usuario = input('Por favor digite o primeiro nome do funcionário:\n')
        if self.nome_usuario in self.lista_nomes:
            continue_cadastro = input('Nome do Funcionário já existente, gostaria de continuar mesmo assim? s/n: ')
            if continue_cadastro.lower()[0] == 's':             
                self.idade = int(input('Por favor digite quantos anos o funcionário tem?\n'))
                self.data_aniversario = datetime.strptime(input('Digite a data de Aniversário do Funcionário: dd/mm/aaaa\n'), '%d/%m/%Y')
                funcionarios.banco_de_dados_usuario()
            elif continue_cadastro.lower()[0] == 'n':
                print('Saindo!!!')
                sys.exit()
            else:
                print('Opção inválida!!!')
        else:
            self.idade = int(input('Por favor digite quantos anos o funcionário tem:?\n'))
            self.data_aniversario = datetime.strptime(input('Digite data de Aniversário: dd/mm/aaaa\n'), '%d/%m/%Y')
            funcionarios.banco_de_dados_usuario()
            
    def banco_de_dados_usuario(self):
        print('banco de dados')
        while True:
            self.banco_de_dados = {'Nº de Registro': self.numero_registro, 'Nome': self.lista_nomes, 'Idade': self.lista_idade, 'Data de Aniversário': self.lista_aniversario}
            self.numero_registro.append(date.today().strftime('%d/%m/%Y'))
            self.lista_nomes.append(self.nome_usuario)
            self.lista_idade.append(self.idade)
            self.lista_aniversario.append(self.data_aniversario.strftime('%d/%m/%Y'))
            print('Dados cadastrados com sucesso!!!\n')
            cadastrar_novamente = input('Gostaria de continuar cadastrando? s/n\n')
            if cadastrar_novamente.lower()[0] == 's':
                funcionarios.recebe_dados_do_usuario()
            elif cadastrar_novamente.lower()[0] == 'n':
                ver_dados_gravados = input('Gostaria de ver dados cadastrados? s/n\n')
                if ver_dados_gravados.lower()[0]== 's':
                    print(Back.RED + Fore.WHITE)
                    print(self.banco_de_dados)
                    print(Back.RESET + Style.DIM)
                    funcionarios.apresentacao()
                    sys.exit()
                else:
                    print('Saindo do Programa!!!')
                    sys.exit()       
            else:
                sys.exit()

    def apresentacao(self):
        for nome in self.lista_nomes:
            print(Fore.LIGHTYELLOW_EX)
            print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {funcionarios.sorteio()}')
            for valor in random.choices(self.cartoes):
                print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {valor}')
                print(Style.RESET_ALL)
    def sorteio(self):
        x = self.numero_registro
        for numero in x:
            return numero
      
funcionarios =  Funcionarios()
funcionarios.start()
funcionarios.recebe_dados_do_usuario()



    


