# wap to convert upper case to lower case and lower to upper case
char = input("Enter charecter : ")

# for lower case
# n = ord(char)+32

# for upper case
n= ord(char)-32
char1 = chr(n)
print(char, char1)
print(f'''
      entered char : {char}
      converted char : {char1}
      ''')

