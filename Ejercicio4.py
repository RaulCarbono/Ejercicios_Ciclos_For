''' Calcular el promedio de edades de hombres, mujeres y de todo un grupo 
de alumnos. '''
age = 0
age_men = 0 
age_women = 0
age_alumnos = 0 
cont_men = age
cont_women = age
cont_alumnos = age  
average = 0

numbers_people = int(input(" Enter to number the people \n "))
for i in range (numbers_people):
    menu = """
    Select option 
    1) Men
    2) Women 
    3) Alumno
    """
    option = int(input(menu))
    if option == 1: 
        age_men+=1 
        age = int(input(" Enter you age \n"))
        cont_men+=age
        average_men = cont_men / age_men
    elif option == 2:
        age_women+=1
        age = int(input(" Enter you age \n"))
        cont_women+=age
        average_women = cont_women / age_women
    else :
        age_alumnos+=1
        age = int(input(" Enter you age \n"))
        cont_alumnos = age
        average = cont_alumnos / age_alumnos
print( age_men , average_men )
print( age_women, average_women)
print( age_alumnos, average)