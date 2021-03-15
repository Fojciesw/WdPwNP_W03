#Napisz program, który wstawia do tablicy 20 liczb losowych, wykorzystując wyrażenia listowe.
#Dopisz w tym celu odpowiednie instrukcje w linii 4 w edytorze poniżej:

from random import random
losowa_lista = [int(100*random()) for i in range(0,20)]
print(losowa_lista, "; length =", len(losowa_lista))
