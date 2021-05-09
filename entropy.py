import math

A = 0.1433
B = 0.8948
E = -1.0854
entropy = 0
print(math.log(8, 2))
for i in range(1, 100001):
    p = A*((i + B)**E)
    entropy += p * math.log(1 / p, 2)
print("entropy per character is", entropy)


Fre_l = [0.1202, 0.091, 0.0812, 0.0768, 0.0731, 0.0695, 
         0.0628, 0.0602, 0.0592, 0.0432, 0.0398, 0.0288,
         0.0271, 0.0261, 0.023, 0.0211, 0.0209, 0.0203,
         0.0182, 0.0149, 0.0111, 0.0069, 0.0017, 0.0011,
         0.001, 0.007]
etrp = 0
for i in range(len(Fre_l)):
    p = Fre_l[i]
    etrp += p * math.log(1 / p, 2)
print("entropy per word is", etrp)
