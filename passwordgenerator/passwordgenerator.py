import random

password = ""

while True:
  need = input("Deseja fazer uma senha? ")
  if need == "Sim":
    for letter in range(10):
      letnum = random.randrange(2)
      if letnum == 1:
        character = random.randrange(97, 122)
        character = chr(character)
        upplow = random.randrange(2)
        if upplow == 1:
          character = character.upper()
          password = password + str(character)
        else:
          password = password + str(character)
      else:
        character = random.randrange(48, 57)
        character = chr(character)
        password = password + str(character)
  
print(password)
