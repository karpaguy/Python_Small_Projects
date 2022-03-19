import random
from string import octdigits

def generate():
  password = ""
  sn = True # Confirma os dados anteriores e segue
  if sn == True:
    for letter in range(10):
      letnum = random.randrange(1) # Decide se será 1 ou 2.
      if letnum == 1: # 1 é letra.
        character = random.randrange(97, 122)
        character = chr(character)
        upplow = random.randrange(1) # Decide se será 1 ou 2.
        if upplow == 1: # Se for 1 será maiúsculo
          character = character.upper()
          password = password + str(character)
        else: # Se for 0 será minúsculo
          password = password + str(character)
      else: # Se for 0 será número.
        character = random.randrange(48, 57)
        character = chr(character)
        password = password + str(character)
    print("Senha gerada: " + password + "\n")
    salvar(password) # Função que dá a chance de salvar a senha, com o argumento sendo a varíavel password.
    opgen() # Função que pergunta ao usuário se deseja criar outra senha.
  else:
    print("O programa será fechado.")
    exit

def opgen(): # Ao ter trocado de sn para snop deu certo, mas porque?
  snop = input("Deseja fazer uma nova senha (sim/não)? ") # Entrega o input para as escolhar, sim ou não. 
  snop = snop.lower()
  if snop == "sim": # Se for verdadeiro, segue e faz novamente. - O True pode ser descartado.
    sn = True
    generate()
  elif snop == "não" or "nao": # Código empaca aqui, mesmo se for uma outra coisa.
    print("Retornando para as opções.\n")
    options()
  else:
    print("Este não é um comando válido.")
    opgen()

def salvar(password): # Listei o parâmetro sendo a varíavel password, existente na função anterior.
  sn2 = input("Deseja salvar essa senha (sim/não)? ") # Entrega o input para as escolhar, sim ou não.
  sn2 = sn2.lower()
  if sn2 == "sim":
    passname = input("\nDigite um nome para esta senha: ")
    passwords_file = open("mypasswords.txt", "a")
    passwords_file.write("\n"+ passname + ": " + password)
    passwords_file.close()
  elif sn2 == "não": # Código empaca aqui, mesmo se for uma outra coisa.
    print("Senha descartada")
  else: # Retorna a pergunta se for digitado outro valor para o input.
    print("Este não é um comando válido.")
    salvar()

def options():
  op = input("Deseja fazer uma nova senha (nova), ver suas senhas salvas (salvas) ou fechar o programa (fechar)? ")
  op = op.lower()
  if op == "nova": # Gera senhas.
    generate()
  elif op == "salvas": # Abre o arquivo e mostra ele na linha de código - DEVE EXISTIR JUNTO DA PASTA.
    passwords_file = open("mypasswords.txt", "r")
    passwords_file.read() # Falta ajustes para ficar correto.
    passwords_file.close()
    op2 = input("Deseja trocar de opção (op) ou fechar o programa (fechar)? ")
    if op2 == "op": # Retorna para opções.
      options()
    elif op2 == "fechar": # Fecha o programa.
      print("O programa será fechado.")
      exit
  elif op == "fechar": # Fecha o programa.
    print("O programa será fechado.")
    exit
  else: # Se algo for escrito errado ou não for um comando válido, retorna as perguntas.
    print("Este não é um comando válido.")
    options()

print("Boas vindas ao gerador de senhas aleatórias.\nOs comandos válidos serão mostrados entre parênteses")
options()

# Se Options falhar, usar o while True.