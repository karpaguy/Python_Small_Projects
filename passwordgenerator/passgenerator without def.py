from ast import expr_context
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
    while True: # Equivalente a função salvar()
      sn2 = input("Deseja salvar essa senha (sim/não)? ") # Entrega o input para as escolhar, sim ou não.
      sn2 = sn2.lower()
      if sn2 == "sim":
        passname = input("\nDigite um nome para esta senha: ")
        passwords_file = open("mypasswords.txt", "a")
        passwords_file.write("• " + passname + ": " + password + "\n")
        passwords_file.close()
        break
      elif sn2 == "não": # Descarta a senha.
        print("Senha descartada.")
        break
      else:
        print("Este não é um comando válido")
    while True: # Equivalente a função opgen()
      snop = input("\nDeseja fazer uma nova senha (sim/não)? ") # Entrega o input para as escolhar, sim ou não. 
      snop = snop.lower()
      if snop == "sim": # Se for verdadeiro, segue e faz novamente. - O True pode ser descartado.
        generate()
        break
      elif snop == "não": # Código empaca aqui, mesmo se for uma outra coisa.
        print("Retornando para as opções.\n")
        options()
        break
      else:
        print("Este não é um comando válido.")
  else:
    print("O programa será fechado.")
    exit  

def options():
  op = input("Deseja fazer uma nova senha (nova), ver suas senhas salvas (salvas) ou fechar o programa (fechar)? ")
  op = op.lower()
  if op == "nova": # Gera senhas.
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
        while True: # Equivalente a função salvar()
            sn2 = input("Deseja salvar essa senha (sim/não)? ")
            sn2 = sn2.lower()
            if sn2 == "sim":
                passname = input("\nDigite um nome para esta senha: ")
                passwords_file = open("mypasswords.txt", "a")
                passwords_file.write("• " + passname + ": " + password + "\n")
                passwords_file.close()
                break
            elif sn2 == "não": # Descarta a senha.
                print("Senha descartada.")
                break
            else:
                print("Este não é um comando válido")
        while True: # Equivalente a função opgen()
            snop = input("\nDeseja fazer uma nova senha (sim/não)? ") 
            snop = snop.lower()
            if snop == "sim":
                generate() # Tire isso e boa sorte.
                break
            elif snop == "não":
                print("Retornando para as opções.\n")
                break
        else:
            print("Este não é um comando válido.")
  elif op == "salvas": # Abre o arquivo e mostra o conteúdo na linha do terminal - DEVE EXISTIR JUNTO DA PASTA.
    passwords_file = open("mypasswords.txt", "r")
    print(passwords_file.readlines())
    passwords_file.close()
    while True:
        op2 = input("Deseja trocar de opção (op) ou fechar o programa (fechar)? ")
        op2 = op2.lower()
        if op2 == "op": # Retorna para opções.
            options()
            break
        elif op2 == "fechar": # Fecha o programa.
            print("O programa será fechado.")
            exit
            break
        else:
            print("Este não é um comando válido.")
  elif op == "fechar": # Fecha o programa.
    print("O programa será fechado.")
    exit
  else: # Se algo for escrito errado ou não for um comando válido, retorna as perguntas.
    print("Este não é um comando válido.")
    options()

print("Boas vindas ao gerador de senhas aleatórias.\nOs comandos válidos serão mostrados entre parênteses.")
options()