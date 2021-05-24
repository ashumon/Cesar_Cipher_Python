def encryptstr(message):
    #declare variables
    newstring = str()
    ascii_letter_value = int()
    one_letter = str()
    new_ascii_value = int()
    #loop to assign new ASCII value
    for index in range(0, len(message)):
        one_letter = message[index]
        ascii_letter_value = ord(one_letter)
        #checking if the letter is Z or z
        if ascii_letter_value == 122:
            new_ascii_value = 97
        elif ascii_letter_value == 90:
            new_ascii_value = 65
        #assigning a new ascii value if not Z or z
        else:
            new_ascii_value = ascii_letter_value + 1
        newstring = newstring + chr(new_ascii_value)
    return newstring

def decryptstr(message):
    #declare variables
    newstring = str()
    ascii_letter_value = int()
    one_letter = str()
    new_ascii_value = int()
    #loop to assign new ASCII value
    for index in range(0, len(message)):
        one_letter = message[index]
        ascii_letter_value = ord(one_letter)
        #checking if the letter is Z or z
        if ascii_letter_value == 97:
            new_ascii_value = 122
        elif ascii_letter_value == 65:
            new_ascii_value = 90
        #assigning a new ASCII value if not Z or z
        else:
            new_ascii_value = ascii_letter_value - 1
        newstring = newstring + chr(new_ascii_value)
    return newstring

def main():
    message = input("Enter text: ")
    prompt = input("Would you like to (E)ncrypt or (D)ecrypt this message?  ")
    
    while prompt != 'Q':
        if prompt == 'E':
           result = encryptstr(message)
           print(result)
        elif prompt =='D':
            result = decryptstr(message)
            print(result)
        else:
            print("Invalid Selection")
        message = input("Enter text: ")
        prompt = input("Would you like to (E)ncrypt, (D)ecrypt this message, or (Q)uit  ")

    

main()
