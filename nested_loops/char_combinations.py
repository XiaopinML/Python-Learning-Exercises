# this app will print all combinations of characters from a to c
char = ['a','b','c','d'] , ['e','f','g','h'] 
# Outer loop iterates over each character in the first list
for char1 in char[0]:
 # Inner loop iterates over each character in the second list
    for char2 in char[1]:
        #print the combinarion of char1 and char 2
        print(char1 + char2, end=' \n')
#print newline after each combination set
print()        