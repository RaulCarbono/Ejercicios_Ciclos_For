'''Un Zoólogo pretende determinar el porcentaje de animales que hay en las 
siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y 
de 3 o mas años. El zoológico todavía no está seguro del animal que va 
estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos; 
si se decide por jirafas, tomara 15 de muestras y si son chimpancés tomará 
40'''

chimpanzees = 3
giraffes = 5
elephant = 6
age_zeroandone = 0 
age_oneandthree = 0 
age_threeandplus = 0 

menu = """
Select option to animals 
1) Elephant 
2) Giraffes 
3) chimpanzees
"""
option = int(input(menu))
if option == 1 :
  for i in range(elephant):
    age = int(input("enter to age to animal "))
    if age == 0 or age == 1:
      age_zeroandone = age_zeroandone + 1
    elif  age > 1 and age < 3:
      age_oneandthree = age_oneandthree + 1 
    else :
      age_threeandplus = age_threeandplus + 1 

elif option == 2 :
 for i in range(giraffes):
    age = int(input("enter to age to animal "))
    if age == 0 or age == 1:
      age_zeroandone = age_zeroandone + 1
    elif  age > 1 and age < 3:
      age_oneandthree = age_oneandthree + 1 
    else :
      age_threeandplus = age_threeandplus + 1 
else:
  for i in range(chimpanzees):
    age = int(input("enter to age to animal "))
    if age == 0 or age == 1:
      age_zeroandone = age_zeroandone + 1
    elif  age > 1 and age < 3:
      age_oneandthree = age_oneandthree + 1 
    else :
      age_threeandplus = age_threeandplus + 1 
      
print(f"los animales de la edad de 0 a un año son {age_zeroandone}")
print(f"los animales mayores a 1 pero menores de 3 años son {age_oneandthree}")
print(f"los animales de la edad de 3 o mas son {age_threeandplus}")