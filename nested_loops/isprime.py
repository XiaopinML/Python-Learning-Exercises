import math
#outer loop , from 2 to 99
for numb in range(2,100):
    #it assumes the number is prime
    is_prime = True
    #it iterates over potentional factor from 2 up to the square root of current number 
    for factor in range(2,int(math.sqrt(numb)+1)):
        if numb % factor == 0:
         is_prime = False
         break
    if is_prime:
        print (numb)     

