import math

A = 0.1433
B = 0.8948
E = -1.0854
entropy = 0
for i in range(1, 100001):
    p = A*((i + B)**E)
    entropy += p * math.log(1 / p, 2)
print("entropy per word is", entropy)


Fre_l = [0.1799, 0.0986, 0.0746, 0.0666, 0.063,
         0.0599, 0.057, 0.0515, 0.0494, 0.0486,
         0.0354, 0.0326, 0.0236, 0.02224, 0.0214,
         0.0189, 0.0173, 0.0172, 0.0166, 0.0149,
         0.0122, 0.0091, 0.00565, 0.00142, 0.00092,
         0.00085, 0.00058]
etrp = 0
for i in range(len(Fre_l)):
    p = Fre_l[i]
    etrp += p * math.log(1 / p, 2)
print("entropy per char is", etrp)
