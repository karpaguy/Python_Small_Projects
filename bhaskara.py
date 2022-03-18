print("Fórmula de Bhaskara\n")

while True:
  a = float(input("Insira o valor de a: "))
  b = float(input("Insira o valor de b: "))
  c = float(input("Insira o valor de c: "))
  delta = (b ** 2) - 4 * a * c
  delta = pow(delta, 1/2)
  print("\n********************\n")
  if a == 0:
      print("O valor de a não pode ser equivalente a 0.")
  elif delta < 0:
      print("Delta não possui raíz quadrada.")
  else:
      x1 = str(-b + delta) / 2 * a
      x2 = (-b - delta) / 2 * a
      x2 = str(x2)
      print("O primeiro valor é " + x1)  # O primeiro resultado
      print("O segundo valor é " + x2)  # O segundo resultado.
      print("\n********************\n")