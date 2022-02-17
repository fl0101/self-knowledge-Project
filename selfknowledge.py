"""
Date: 21/01/2022
Author: Flaviane S. Nascimento
Desc.: Software TBB
Info: Se possível, não gravar informações em arquivos sem retirar espaços
antes para evitar problemas na leitura do arquivo
"""

from os import system
import getpass
from time import sleep


class Register:

    """ Requisitos para cadastro """

    def __init__(self, name, passwd):
        self.dados_user = {}
        self.name = name
        self.passwd = passwd
        self.user = open("users.txt", 'a')
        self.dados_users = f'{name},{passwd}\n'
        self.user.write(self.dados_users)
        self.user.close()


class Menu:

    """ Lista de opções """

    def __init__(self):
        print("""
        [1] Cadastro
        [2] Login
        [3] Sair
        """)


class Imprime:

    """ Imprime informações de cada lista """

    @staticmethod
    def listas():
        print("""
1- Principais informações
2- Valores
3- Networking
4- Análise SWOT
5- Propósito de vida
6- Objetivos
7- Metas
8- Sair

        """)

    @staticmethod
    def lista_principal():
        print("""
Através desta lista vamos descobrir o que queremos para nossa vida
profissional, estudo, relacionamentos sociais, sáude e muito mais.

Não se preocupe com a ordem das informações que irá escrever.

Como fazer:
Pense em como você gostaria de estar no futuro profissional, o que vier
a sua mente, mesmo que pareça bobagem para você agora. Sugiro que anote.

Pense o que você gosta de estudar, o que gosta de pesquisar na internet,
que lugares gostaria de visitar, o que gostaria de fazer, mas ainda não 
fez, o que gosta de ler, que tipo de exercícios gosta ou gostaria de praticar,
que momentos você lembra que lhe deixou muito feliz, sobre que assuntos você
gosta de conversar e etc.

Lembre-se o que vier a sua mente sobre o que o gosta ou gostaria de ter 
ou fazer sugiro que escreva.

        """)

    @staticmethod
    def valores():
        print("""
Escreva em uma nova folha tudo o que você valoriza.

Como fazer:
Ex.: Eu valorizo a fé, valorizo a coragem, a empatia,
a disciplina, a persistência, a perseverança, o estudo e etc.

        """)

    @staticmethod
    def networking():
        print("""
Quem te inspira? Um membro da família? Um amigo? Um professor?
um escritor? Um ator? Um músico?

Como fazer:
Escreva em outra folha o nome daquelas pessoas que te deixam motivado, aqueles
que te deixam inspirado para fazer o que faz ou o que deseja fazer.

        """)

    @staticmethod
    def swot():
        print("""
A análise SWOT é uma ferramenta muito útil que serve para nos auxiliar 
no autoconhecimento. SWOT vem de Strengths, Wekenesses, Opportunities e 
Threats em português: Forças, Fraquezas, Oportunidades e Ameaças.

Como fazer:
Em outra folha desenhe duas linhas grandes de modo que divida a folha em
quatro partes iguais. Para cada quadrado da folha escreva as respostas para
as perguntas a seguir:

Forças: 
    Quais cursos eu fiz?
    Quais as minhas competências?
    Quais são as minhas habilidades?
    O que me destaca das pessoas que fazem o mesmo trabalho que eu?
    Quais emoções e sentimentos as pessoas valorizam em mim?
    Pelo o quê eu sou elogiado?
    O que eu faço muito bem?
    
Fraquezas:
    O que tenho feito que tem prejudicado meu crescimento pessoal e profissional?
    O que me distrai facilmente e me distancia do meu objetivo?
    Por que não me sinto feliz em algumas situações?
    Realmente estou fazendo o que gosto?
    Quantas vezes estive motivado a continuar fazendo o que faço?
    
Oportunidades:
    Tenho chances de crescer no meu atual emprego?
    O meu perfil profissional está adequado às necessidades do mercado?
    Quais as chances de mudar de carreira?
    Quais as oportunidades perto de mim no momento?
   
Ameaças:
    O que pode ser um obstátulo no alcance do meu objetivo?
    O que há no mercado atualmente que pode me impedir?

        """)

    @staticmethod
    def propos_vida():
        print("""
Como descobrir meu propósito de vida?

Passo 1: Pegue a primeira lista que preenchemos, onde escrevemos tudo
de forma aleatória.

Passo 2: Leia toda a lista e coloque ao lado de cada informação a letra relacionada:
T para trabalho, EST para estudo, R para relacionamentos sociais, S para saúde, L para lazer
e ESP para espiritualidade.

Ex.:
R gosto de conversar sobre viajens
T quero abrir uma loja no segmento de tecnologia com foco em venda de produtos de 
alta qualidade.

Passo 3: Comece a ler a lista da seguinte forma, primeiro todas as informações
que começam com a letra T, depois as que começam com EST, depois as que 
começam com a letra R e assim por diante.

Passo 4: Existe algo que liga todas essas informações nesta lista, algo que está
envolvido com sentimentos e emoções. Uma coisa que está por trás de tudo o que
você escreveu. Isso se chama propósito de vida. Que vamos descobrir agora.

IMPORTANTE: Não inicie este passo se não tiver pelo menos 40 minutos ou mais 
disponível, pois você precisará ler e reler a lista para encontrar e entender seu propósito.

Passo 5: Leia e releia a primeira lista como descrito no passo 3 e comece a identificar
seu propósito de vida. Use os exemplos abaixo como auxilio.

Ex.1: Amo trabalhar com tecnologia, amo estudar linguagens de programação, gosto de 
conversar sobre negócios, gosto de me exercitar, amo viajar e praticar meditação.
Quando leio minha lista o sentimento predominante é de: "AJUDAR, MOTIVAR, INSTRUIR 
e ENSINAR qualquer pessoa que precisa de forças e meios para alcançar seus objetivos
e metas. Utilizarei a tecnologia e a programação como meios para tornar real este propósito" 
O meu propósito de vida está entre as aspas.

Ex.2: Quero trabalhar no segmente de saúde, gosto estudar sobre medicamentos e biologia,
amo conversar sobre as descobertas da área da saúde, quero cuidar da minha alimentação
e praticar exercícios físicos, amo visitar lugares que me deixam próximo a natureza e
praticar yoga. Quando leio minha lista sinto que devo: "ABRIR UMA FARMÁCIA para AJUDAR
as pessoas a encontrarem mais rapidamente medicamentos de que precisam, CRIAR UM BLOG
para INSTRUIR e MOTIVAR as pessoas a cuidarem mais de sua saúde e praticar atividades
físicas e ENSINAR como podem melhorar sua alimentação e saúde mental." O meu propósito 
de vida está entre as aspas.

        """)

    @staticmethod
    def objetivos():
        print("""
Como descobrir meus objetivos?

Objetivo é tudo aquilo que você quer alcançar. Sabe onde eles se encontram? É isso aí.
Na primeira lista que criamos tudo de forma aleatória.

Leia a primeira lista e marque tudo o que você deseja alcançar dentro de 1, 3, 5 e 10
anos.

Para cada objetivo é importante estabelecer um prazo e definir os recursos de que 
precisará para torná-los real.

Ex.:
OBJETIVO: Quero abrir uma loja de produtos de farmácia nos próximos 5 anos. 

RECURSOS: Precisarei de RECURSOS FINANCEIROS para comprar ou alugar um ponto estratégico.
UM FORNECEDOR para adquirir os medicamentos. UM OU DOIS COMPUTADORES com um sistema para
controle de estoque, cadastro de novos clientes e EQUIPAMENTO PARA EMITIR NOTAS FISCAIS.
Precisarei CONTRATAR UM CONTADOR, CONTRATAR UM OU DOIS FUNCIONÁRIOS e etc. 

        """)

    @staticmethod
    def meta():
        print("""
Passo fundamental para tornar real um objetivo.

Dica: Não tente iniciar mais de 3 metas ao mesmo tempo.

Passo 1: Leia sua lista de objetivos, priorize dois e confirme o porquê você
quer torná-los real.

Passo 2: Para cada objetivo escreva o passo a passo que você precisará fazer
para alcançá-lo. Este passo a passo são as suas metas.

Algumas vezes a gente não consegue descrever por completo como iremos alcançar
um objetivo, não se preocupe, isso é totalmente normal. Liste quantos passos
conseguir, demilimite-os o máximo que puder, insira um passo na sua agenda de amanhã,
outro na agenda do dia seguite e assim por diante. Conforme for avançando, seu
objetivo e suas metas ficarão cada vez mais claros. 

Ex.:
OBJETIVO: Viajar para Gramados no fim do ano
METAS: Verificar o valor do hotel, verificar o valor da passagem, preço médio de roupas
e alimentação no local, o que levar nas malas, poupar determinada quantia em dinheiro 
mensalmente para conseguir a viajem, comprar a passagem no dia tal e confirmar
no dia tal, alugar o hotel no dia tal e confirmar no dia tal.

IMPORTANTE: As metas são importantes, e mais importante é concluí-las. Portanto, se
você tem o hábito de procrastinar, desenvolva imediatamente o hábito da disciplina.
Acredito que a melhor forma de desenvolver a disciplina e se livrar da procrastinação
é a PNL. Por isso, vou deixar um link disponível com um áudio reprogramador que me 
ajudou muito e acredito que pode lhe ajudar também. Escute durante pelo menos 21 dias
ao dormir ou assim que acordar e verá a diferença logo nos primeiros dias:
https://www.youtube.com/watch?v=AfsfJNAtPF0

LEMBRE-SE CONSTANTEMENTE DO PORQUÊ VOCÊ DEVE PERSEGUIR OS SEUS OBJETIVOS E TORNÁ-OS REAL.
RELEIA PELO MENOS 1 VEZ NA SEMANA TODAS AS LISTAS PARA SE MANTER MOTIVADO.

SUCESSO NA SUA JORNADA! :)
 
        """)


def welcome():
    print(5 * " ", 48 * "*", 5 * " ")
    print(6 * " ", "Bem vindo ao projeto Descobrindo meu Propósito", 6 * " ")
    print(5 * " ", 48 * "*", 5 * " ")
    print()


def menu_one():
    system("clear")
    print(Menu())
    option = input("Digite o número da opção desejada: ")

    if option == '1':
        register()

    elif option == '2':
        login()

    elif option == '3':
        print("Até logo!")
        quit()

    else:
        if option.isdigit() != ['1', '2', '3']:
            print("Inválido")
            sleep(1)
            menu_one()


def register():
    system("clear")
    welcome()
    name = input("Como gostaria de ser chamado(a)? ")
    passwd = getpass.getpass(prompt='Senha: ')
    passwd_conf = getpass.getpass(prompt='Confirme sua senha: ')

    if passwd == name:
        while True:
            print("""
            Para sua segurança, NÃO crie uma senha com:
            - Seu nome
            - Datas de nascimento
            - Animal de estimação
            - Sequência de números

            Uma senha segura contém:
            - Pelo menos 8 caracteres
            - Números
            - Letras maiúsculas
            - Letras minúsculas
            - Símbolos
                    """)
            menu_one()

    while passwd != passwd_conf:
        passwd_conf = getpass.getpass(prompt="\nSenhas não coincidem"
                                             "\nConfirme sua senha novamente: ")

    verify = verify_registration_user(name=name)

    if verify is True:
        print("Nome de usuário já existente")
        sleep(2)
        system('clear')
        menu_one()

    else:
        system('clear')
        print("Olá,", name)
        Register(name=name, passwd=passwd)
        to_introduce()


def verify_registration_user(name):

    """ Verifica o nome do usuario antes de registrar """

    users = []

    try:
        with open('users.txt', 'r+') as archive:
            for line in archive:
                line = line.strip()
                users.append(line.split(","))

            for user in users[:]:
                if name == user[0]:
                    return True

    except (Exception, ):
        pass


def to_introduce():

    """ Apresentação do projeto. Exibição apenas para novos usuarios """

    print("""
    Nesta aplicação vamos juntos descobrir nosso propósito de vida, nossos valores, 
    objetivos e muito mais. Além de traçar metas para alcançar cada objetivo,
    vamos descobrir nossas forças e qualidades. Vamos nessa? ;)
        """)

    sleep(6)
    input("Pressione Enter ")
    system('clear')

    print("""
    O que vamos precisar:
    | Canetas
    | Folhas de papel

    Essas são as informações que vamos aprender sobre nós ao longo da nossa jornada, 
    sugiro que anote em uma folha de papel:

    1- Principais informações
    2- Valores
    3- Networking
    4- Análise SWOT
    5- Propósito de vida
    6- Objetivos
    7- Metas
        """)

    sleep(6)
    input("\nPressione enter para fazer login ")
    system('clear')
    login()


def login():
    system("clear")
    name = input("Login: ")
    passwd = getpass.getpass("Senha: ")

    check = check_login_user(name=name, passwd=passwd)

    if check is True:
        print("Que bom de te ver,", name, ";)")
        sleep(1)
        general_lists()

    else:
        print("Usuário ou senha incorreto")
        sleep(1)
        menu_one()


def check_login_user(name, passwd):

    """ Verifica se o usuario e senha estão registrados """

    to_check = []

    try:
        with open('users.txt', 'r+', newline='') as arquivo:
            for separate in arquivo:
                separate = separate.strip()
                to_check.append(separate.split(","))

            for verify in to_check:
                verify_name = verify[0]
                verify_passwd = verify[1]
                if name == verify_name and passwd == verify_passwd:
                    return True

    except (Exception, ):
        pass


def general_lists():

    """ Acesso à leitura de todas as listas """

    Imprime.listas()
    choice = input("Digite o número correspondente a lista que iremos ler agora: ")

    def get_out():

        """ Trativa interna para as condições de leitura """

        sair = input("Digite 's' para sair da leitura: ")

        if sair.upper() == 'S':
            new_list()

        else:
            if sair.upper() != 'S':
                get_out()

    def new_list():
        new = input("Vamos continuar aprendendo? S/N ")
        if new.upper() == 'S':
            system('clear')
            general_lists()

        elif new.upper() == 'N':
            print("Até logo!")
            quit()

        else:

            if new.upper() != 'S' and new.upper() != 'N':
                print("Inválido")
                new_list()

    if choice == '1':
        system('clear')
        Imprime.lista_principal()
        get_out()

    elif choice == '2':
        system('clear')
        Imprime.valores()
        get_out()

    elif choice == '3':
        system('clear')
        Imprime.networking()
        get_out()

    elif choice == '4':
        system('clear')
        Imprime.swot()
        get_out()

    elif choice == '5':
        system('clear')
        Imprime.propos_vida()
        get_out()

    elif choice == '6':
        system('clear')
        Imprime.objetivos()
        get_out()

    elif choice == '7':
        system('clear')
        Imprime.meta()
        get_out()

    elif choice == '8':
        print("Até logo!")
        quit()

    else:

        if choice != ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("\nInválido")
            sleep(1)
            system('clear')
            general_lists()


def main():
    system('clear')
    menu_one()


main()
