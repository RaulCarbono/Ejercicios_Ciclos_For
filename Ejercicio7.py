# En un supermercado una ama de casa pone en su carrito los artículos que 
# va tomando de los estantes. La señora quiere asegurarse de que el cajero 
# le cobre bien lo que ella ha comprado, por lo que cada vez que toma un 
# artículo anota su precio junto con la cantidad de artículos iguales que ha 
# tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo 
# que irá gastando en los demás artículos, hasta que decide que ya tomó 
# todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su 
# compra
articles_total = int(input( " Enter total to articles the shooping car \n"))
price_total= 0 
articles = 0 
for i in range(articles_total):
    articles_1 = int(input(" Enter to amount the articles \n"))
    price = int(input(" Enter to price the article \n"))
    price_total = articles_1 * price 
    articles += price_total     
print(f" Price total the shop is {articles} ")



