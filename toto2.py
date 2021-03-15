import random

# T = []
# for i in range(50): T.append(0)
T = [0 for i in range(50)] #list comprehension, wyrażenie listowe

N = 10000
K=49

for j in range(N):
    for i in range(6):
        kula = int(random.random()*K) + 1
        print("kula: ", kula)
        # tu zliczamy krotnosc kul
        print(T[kula])
        T[kula] = T[kula] + 1
        print(T[kula])
        print("i", i, "j", j)

print("tablica: ",T)

spr = 0
for i in range(1, len(T)):
    print("ile razy", i, ":", T[i])
    spr += T[i]
print("spr", spr)
