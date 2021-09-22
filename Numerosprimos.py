#Imprimir los numeros primos del 1 al 20
def is_prime(num):
    divisors_count = 0
   
    for i in range(1, num + 1):
        if i==1 or i == num:
            continue
        if num % i == 0: 
            divisors_count+=1
    if divisors_count == 0:
        return True
    else:
        return False
        
def run(): 
    num = int(input(" Enter to number "))
    if is_prime(num):
        print(" Is prime ")
    else: 
        print(" No is prime ")

if __name__ == "__main__":
    run()
