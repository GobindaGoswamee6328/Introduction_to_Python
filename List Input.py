
n = input("Enter a text of Numbers : ")

list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)

print(sum)


#Finding number of words,letters and digit:

numofwords = 0
numofletters = 0
numofdigits = 0

text = input("Enter a text of Numbers : ")

for x in text:
    x = x.lower()

    if x >= "a" and x <= "z":
        numofletters = numofletters + 1

    elif x >= "0" and x <= "9":
        numofdigits  = numofdigits + 1

    if x == ' ':
        numofwords = numofwords + 1

print("Number of letters :",numofletters)
print("Number of digits :",numofdigits)
print("Number of words :",numofwords)
