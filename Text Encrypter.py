#Decrypting Function
def decipher(b):
    DecryptedString = "" #Will hold combined character values
    ConvertString = "" #
    x = 0
    key = ord(b[x])  #Holds the ord value of first character
    key = int(key/2) #Halves the ord value of key
    
    #Loop through string 'b' depending on the length of it 
    for i in range(len(b)):
        ConvertString = chr(ord(b[i]) - key)  #ord value of character at index is subtracted by key, then made into character
        DecryptedString = DecryptedString + ConvertString  #Combines and stores character values
    return DecryptedString  #Returns decrypted string


#Encrypting Function
def cipher(a):
    EncryptedString = ""
    ConvertString = ""
    x = 0
    key = ord(a[x])  #Holds the ord value of first character
    #Loops through string 'a' depending on the length of it 
    for i in range(len(a)):
        ConvertString = chr(ord(a[i]) + key) #ord value of character at index is subtracted by key, then made into character
        EncryptedString = EncryptedString + ConvertString #Combines and stored encrypted character values
    return EncryptedString #Returns encrypted string

#Main Function
def main():
    UserInput = str(input("Please input any sentence: ")) #Takes user string input
    TheCipher = cipher(UserInput) #Passes UserInput to cipher function
    print(TheCipher) #Prints return value from function
    TheDecipher = decipher(TheCipher) #Passes TheCipher value to decipher function
    print(TheDecipher) #Prints reutnr value from function

main()