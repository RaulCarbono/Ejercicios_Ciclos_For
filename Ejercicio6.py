'''Cinco miembros de un club contra la obesidad desean saber cuanto han 
bajado o subido de peso desde la última vez que se reunieron. Para esto se 
debe realizar un ritual de pesaje en donde cada uno se pesa en diez 
básculas distintas para así tener el pormedio mas exacto de su peso. Si 
existe diferencia positiva entre este promedio de peso y el peso de la última 
vez que se reunieron, significa que subieron de peso. Pero si la diferencia 
es negativa, significa que bajaron. Lo que el problema requere es que por 
cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la 
cantidad de kilos que subió o bajó de peso.'''
member = 0 
actual_weight_1 = float(input("Please member one enter to actual weight \n"))
actual_weight_2 = float(input("Please member two enter to actual weight \n"))
actual_weight_3 = float(input("Please member three enter to actual weight \n"))
actual_weight_4 = float(input("Please member four enter to actual weight \n"))
actual_weight_5 = float(input("Please member five enter to actual weight \n"))

list_weight1 =[]
list_weight2 =[]
list_weight3 =[]
list_weight4 =[]
list_weight5 =[]
for j in range(2): 
    member +=1
    for i in range(2):
        weihing_machine = float(input(f" {member} bascula # {i+1}\n"))
        list_weight1.append(weihing_machine)
print(list_weight1)