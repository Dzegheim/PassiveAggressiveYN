from PassiveAggressive import PAYN as GetYN

print ("To test the function try to insert anything but a boolean.")
A = []
A.append(GetYN("(1) Give a boolean pls", GiveUp = True))
A.append(GetYN("(2) Give a boolean pls", GiveUp = True, K4 = 1, K3 = 2, K2 = 3, K1 = 4, K0 = 5, GiveUpN = 6))
A.append(GetYN("(3) Give a boolean pls", GiveUp = True, K4 = 2, K3 = 4, K2 = 6, K1 = 8, K0 = 10, GiveUpN = 12))
A.append(GetYN("(4) Now I won't give up"))
print (A)
