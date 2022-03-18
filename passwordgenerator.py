import random

senha = ""

for letter in range(10):
  letra = random.randrange(97, 122)
  letra = chr(letra)
  senha = senha + str(letra)
  
print(senha)
