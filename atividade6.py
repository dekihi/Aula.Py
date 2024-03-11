import  os 
os.system('cls')
import math
print('Calculadora hipotenusa')
cateto_oposto = float(input("Digite o cateto oposto; "))
cateto_adjacente = float(input("digite o cateto adjacente: "))
hipotenusa = math.sqrt(cateto_oposto**2 + pow(cateto_adjacente, 2))
print(f"A hipotenusa é igual a: {hipotenusa}")