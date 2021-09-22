'''Una empresa se requiere calcular el salario semanal de cada uno de los n 
obreros que laboran en ella. El salario se obtiene de la siguiente forma:
a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
b. Si trabaja mas de 40 horas se le paga $20 por cada una de 
las primeras 40 horas y $25 por cada hora extra'''

print (" Calculate the weekly wage \n")
worker = int(input( "Enter worker numbers \n" ))
for i in range(worker): 
    hours = int(input( "Enter the hours worked \n" ))
    pago = 20 
    if hours <= 40:
        pago = pago * hours
        print(pago)
    else :
        hours_extra = int(input( "Enter hours extras Worked " ))
        pago = (hours - hours_extra) * pago
        partial = hours_extra * 25 
        total = (pago + partial)
        print(pago)
        print(partial)
        print(total)


