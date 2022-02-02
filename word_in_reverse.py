# Write a Python program that accepts a word from the user and reverse it. 

# Create a program 
# Accept a word from the user
# Displays the word in reverse order 
# range()

var1 = input("Type a word to be displayed in reverse ")
var2 = len(var1) -1 
var3 = "" 

for i in range(var2, -1, -1): 
    var3 = var3 + var1[i]
print(var3)