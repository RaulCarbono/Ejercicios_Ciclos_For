# Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la 
# siguiente tabla: 
# Valor vendido Comisión
# Menor o igual que 20 Millones 10%
# Mayor de 20 Millones y menor de 40 Millones 15%
# Mayor o igual de 40 Millones y menor de 80 Millones 20%
# Mayor o igual de 80 millones y menor de 160 Millones 25%
# De 160 Millones en adelante 30%
# Realice un método que diga cuanto vendió y la comisión de los 100 
# vendedores que tiene la empresa.

value_comision_s1=0
value_comision_s2=0
value_comision_s3=0
value_comision_s4=0
value_comision_s5=0

for i in range(2):
    seller = float(input(" ! Enter the sold value in the year  !\n"))
    if seller <=20000000 :
        comision = seller * 0.10
        value_comision_s1 +=  comision
    elif seller >2000000 and seller <40000000 :
        comision = seller * 0.15
        value_comision_s2 +=  comision
    elif seller >= 40000000 and seller <80000000 : 
        comision = seller * 0.20
        value_comision_s3 +=  comision
    elif seller >= 80000000 and seller <160000000 : 
        comision = seller * 0.25
        value_comision_s4 +=  comision
    else :
        comision = seller * 0.30
        value_comision_s5 +=  comision
                
print (f"! The commission for sale is {value_comision_s1} !\n")
print (f"! The commission for sale is {value_comision_s2} !\n")
print (f"! The commission for sale is {value_comision_s3} !\n")
print (f"! The commission for sale is {value_comision_s4} !\n")
print (f"! The commission for sale is {value_comision_s5} !\n")

