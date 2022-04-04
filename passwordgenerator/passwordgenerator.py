import random
from string import octdigits

# Ainda falta determinar o total de caracteres que deseja na senha.

def generate():
  while True: # Aqui vai dar o input de quantos caracteres vai ter a senha.
    try:
      ltnum = int(input("Insira o total de caracteres que deseja em sua senha: "))
      break
    except: # e o usuário não der um número, ele pergunta novamente.
      print("O valor inserido não é um número inteiro.")
  password = ""
  sn = True # Confirma os dados anteriores e segue
  if sn == True:
    for letter in range(ltnum):
      letnum = random.randrange(2) # Decide se será 1 ou 2.
      if letnum == 1: # 1 é letra.
        character = random.randrange(97, 122)
        character = chr(character)
        upplow = random.randrange(2) # Decide se será 1 ou 2.
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
  snop = input("\nDeseja fazer uma nova senha (sim/não)? ") # Entrega o input para as escolhar, sim ou não. 
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
    passwords_file.write("• " + passname + ": " + password + "\n")
    passwords_file.close()
  elif sn2 == "não": # Descarta a senha.
    print("Senha descartada.")
  else: # Retorna a pergunta se for digitado outro valor para o input.
    print("Este não é um comando válido.")
    salvar(password) # É preciso especificar o argumento novamente para iniciar sem erros.

def verifysaves():
  passwords_file = open("mypasswords.txt", "r")
  print(passwords_file.readlines())
  passwords_file.close()
  op2 = input("Deseja trocar de opção (op) ou fechar o programa (fechar)? ")
  op2 = op2.lower()
  if op2 == "op": # Retorna para opções.
    options()
  elif op2 == "fechar": # Fecha o programa.
    print("O programa será fechado.")
    exit
  else:
    print("Este não é um comando válido.")
    verifysaves()

def options():
  op = input("Deseja fazer uma nova senha (nova), ver suas senhas salvas (salvas) ou fechar o programa (fechar)? ")
  op = op.lower()
  if op == "nova": # Gera senhas.
    generate()
  elif op == "salvas": # Abre o arquivo e mostra o conteúdo na linha do terminal - DEVE EXISTIR JUNTO DA PASTA.
    verifysaves()
  elif op == "fechar": # Fecha o programa.
    print("O programa será fechado.")
    exit
  else: # Se algo for escrito errado ou não for um comando válido, retorna as perguntas.
    print("Este não é um comando válido.")
    options()

print("Boas vindas ao gerador de senhas aleatórias.\nOs comandos válidos serão mostrados entre parênteses")
options()