# La empresa Encuestas S.A desea crear una función que les permita 
# conocer de los 50.000 votos obtenidos por 3 candidatos, cual de estos fue 
# el ganador o indicar si hubo empate y la cantidad de votos obtenidos

candidato1= 0
candidato2= 0 
candidato3= 0 
for i in range(5): 
    menu = """
    Select option to candidato 
    1) Candidato 1  
    2) Candidato 2 
    3) Candidato 3  
    """
    option=int(input(menu))
    if option == 1: 
        candidato1 +=1 
    elif option == 3: 
        candidato2 +=1
    else:
        candidato3 +=1 
print(f" the votes for candidate 1 him are {candidato1} ")
print(f" the votes for candidate 2 him are {candidato2} ")
print(f" the votes for candidate 3 him are {candidato3} ")
  


