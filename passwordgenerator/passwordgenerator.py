import random


print("Boas vindas ao gerador de senhas aleatórias.")
sn = input("Deseja fazer uma senha? ")
sn = sn.lower()

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
    print(password + "\n")
    sn2 = input("Deseja salvar essa senha? ")
    sn2 = sn2.lower()
    if sn2 == "sim":
      passname = input("\nDigite um nome para esta senha: ")
      passwords_file = open("mypasswords.txt", "a")
      passwords_file.write("\n"+ passname + ": " + password)
      passwords_file.close()
    else:
      print("Senha descartada")
    sn = input("Deseja fazer uma nova senha? ")
    sn = sn.lower()
    if sn == "sim": # Se for verdadeiro, segue e faz novamente. - O True pode ser descartado.
      sn = True
      generate()
    else: # Se for QUALQUER outra coisa escrita, cancela.
      print("O programa será fechado.")
      exit
  else:
    print("O programa será fechado.")
    exit
  
if sn == "sim": #Mantendo a informação anterior, pode ser trocado se os inputs anteriores forem jogados aqui para cá.
  generate()
else:
  print("O programa será fechado.")
  exit
