from enum import Enum

class candidato(Enum):

    x = 889
    y = 847
    z = 515
    branco_nulo = 0

voto_x = 0
voto_y = 0
voto_z = 0
voto_branco_nulo = 0

while (True):
    try: 
       voto = int(input("Digite seu voto: "))

    except:
        print("Voto inválido. Tente novamente")
        continue

    if (voto == candidato.x.value):
        voto_x = voto_x + 1
    elif (voto == candidato.y.value):
        voto_y = voto_y + 1
    elif (voto == candidato.z.value):
        voto_z = voto_z + 1
    else:
        voto_branco_nulo = voto_branco_nulo + 1

    resposta = input("Deseja finalizar a votação? S/N: ")
    if (resposta == "s") or (resposta == "S"):
      break

maior_numero_votos = max(voto_x, voto_y, voto_z)
    
if (maior_numero_votos == voto_x):
    vencedor = candidato.x.name
elif(maior_numero_votos == voto_y):
    vencedor = candidato.y.name
elif(maior_numero_votos == voto_z):
    vencedor = candidato.z.name


print("Vencedor: " + vencedor)
print("Candidato X: " + str (voto_x) + " votos")
print("Candidato Y: " + str (voto_y) + " votos")
print("Candidato Z: " + str (voto_z) + " votos")
print("Brancos e Nulos: " + str (voto_branco_nulo) + " votos")











        


  










       


    
        







    







    

