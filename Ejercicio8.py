# Un teatro otorga descuentos según la edad del cliente, determinar la 
# cantidad del dinero que el teatro deja de percibir por cada ua de las 
# categorias. Tomar en cuenta que los niños menores de 5 años no pueden 
# entrar al teatro y que existe un precio único en los asientos. Los descuentos 
# se hacen tomando en cuenta el siguiente cuadro:
# Edad % Descuento
# 5 – 14 35%
# 15-19 25%
# 20 – 45 10%
# 46 – 65 25%
# 66 en Adelante 35%
discount = 0  
discount_cat1 = 0
discount_cat2 = 0
discount_cat3 = 0
discount_cat4 = 0
discount_cat5 = 0
peaple = int(input(" Enter the number of  who will enter \n"))
price_ticket = int(input(" Enter value the ticket \n"))
for i in range(peaple): 
    discount_range = 0
    age = int(input(" Enter age please "))
    if age == 0 and age <= 4: 
        print("Error cannot enter children under 5 years")
    elif age >= 5 and age <= 14: 
        discount_age = price_ticket * 0.35 
        discount += discount_age
        discount_range = discount_age
        discount_cat1 += discount_age 
        print(F"The discount for age the range 5-14 [{discount_range}]")
    elif age >= 15 and age <=19 and age:
        discount_age = price_ticket * 0.25
        discount += discount_age
        discount_range = discount_age
        discount_cat2 += discount_age 
        print(F"The discount for age the range 15-19 [{discount_range}]")
    elif age >= 20 and age <=45 : 
        discount_age = price_ticket * 0.10
        discount += discount_age
        discount_range = discount_age
        discount_cat3 += discount_age 
        print(F"The discount for age the range 20-45 [{discount_range}]")
    elif age >= 46 and age <=65 : 
        discount_age = price_ticket * 0.25
        discount += discount_age
        discount_range = discount_age
        discount_cat4 += discount_age 
        print(F"The discount for age the range 46-65 [{discount_range}]")
    else :  
        discount_age = price_ticket * 0.35
        discount += discount_age
        discount_range = discount_age
        discount_cat5 += discount_age 
        print(F"The discount for age the range 66 [{discount_range}]\n ")
print (f"! The discount total is [{discount}]       !\n")
print (f"! discount category one is {discount_cat1}   !\n")
print (f"! discount category two is {discount_cat2}   !\n")
print (f"! discount category three is {discount_cat3} !\n")
print (f"! discount category four is {discount_cat4}  !\n")
print (f"! discount category five is {discount_cat5}  !\n")
