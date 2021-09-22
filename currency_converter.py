def converter(tipe_weight, value_coin):
    weight=float(input(f"enter to {tipe_weight} to convert "))
    tipe_weight+=str(round(weight/value_coin))   
    print(f"you have $ { tipe_weight } ")


def converter1(type_coin, value_coin1):
    weight=float(input(f"enter type coint {type_coin} to convert "))
    type_coin = round(weight * value_coin1)
    print(f"you have  {type_coin}  ")
menu = """
Select option to converter
1) Converter weight to dollar 
2) Converter weight to euro  
3) Converter weight to Bicoin 
4) Converter to dollar in weight 
5) converter euro to weight
6) converter bitcoin to weigh
"""
option=int(input(menu))
if option == 1 :
    converter("dollar",3921)
elif option == 2 :
    converter("Euro",4638)
elif option == 3 :
    converter("bitcoin",150000)
elif option == 4: 
    converter1("dollar",3921)
elif option == 5:
    converter1("Euro",4638)
else :
    converter("bitcoin",150000)
