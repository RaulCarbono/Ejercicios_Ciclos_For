'''Un proveedor de estéreos ofrece un descuento del 10% sobre el 
precio sin IVA, de algún aparato si este cuesta $2000 o más. Además, 
independientemente de esto, ofrece un 5% de descuento si la marca 
es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente 
cualquiera por la compra de su aparato. IVA es del 16%'''
partial_value=20000
brand = ("nosy")
brandstereo =str(input("enter brand of stereo\n"))
stereo =float(input("enter value of stereo \n" ))

if stereo >= partial_value:
   discount = stereo *0.10 
   total_p = stereo - discount
   total = total_p * 0.16+ total_p
   print("discount is", discount) 
   print("partial total is", total_p)
   print("total is", total)
else: 
    
    total = stereo * 0.16 + stereo
    print("total is\n", total)
if brandstereo == brand :
       total1 = total - (total * 0.05) 
       print("discount apply is\n", total *0.05)
       print("total is", total1)
