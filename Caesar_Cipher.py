import re

def text_to_numerical_val_list(input_text): # of course we already know what good about this function
    regex = re.compile('[^a-zA-Z]')
    input_text = regex.sub('', input_text)
    input_text = re.sub(r"\s+", "", input_text, flags=re.UNICODE)
    input_text = input_text.lower()
    text_char_to_numerical_value_list = []
    for character in input_text:
        numerical_value = ord(character) - 97
        text_char_to_numerical_value_list.append(numerical_value)
    return text_char_to_numerical_value_list    

def encipher(plaintext,shift): 
    plaintext_numerical_val_list= text_to_numerical_val_list(plaintext)
    print(plaintext_numerical_val_list)
    cipher_values = []
    for i in plaintext_numerical_val_list:
        cipher_val = i+shift
        if(cipher_val>25):
            cipher_val = cipher_val%26
        cipher_values.append(chr(((cipher_val)% 26)+97))
    cipher_text = ''.join(str(char) for char in cipher_values)
    return "Cipher text:  "+cipher_text.upper()

def decipher(ciphertext):
    cipher_text_to_numerical_val_list = text_to_numerical_val_list(ciphertext)
    all_possible_values = []
    possible_values = []
    for i in range(1,25):
        for j in cipher_text_to_numerical_val_list:
            possible_values.append((chr(((i+j)% 26)+97)))
        all_possible_values.append((''.join(str(char) for char in possible_values)).lower())    
        possible_values = []   
    a = []
    for i in range(0,len(all_possible_values)):
        a.append("key: "+str(26-(i+1))+", plaintext: "+ all_possible_values[i])      
    return ("All possible plaintext:  ",a)


print(decipher("EVIRE")) 
print(encipher("river",13))
print(encipher("arena",4))

#Terminal output
"""('All possible plaintext:  ', ['key: 25, plaintext: fwjsf', 'key: 24, plaintext: gxktg', 
'key: 23, plaintext: hyluh', 'key: 22, plaintext: izmvi', 'key: 21, plaintext: janwj', 
'key: 20, plaintext: kboxk', 'key: 19, plaintext: lcpyl', 'key: 18, plaintext: mdqzm', 
'key: 17, plaintext: neran', 'key: 16, plaintext: ofsbo', 'key: 15, plaintext: pgtcp', 
'key: 14, plaintext: qhudq', 'key: 13, plaintext: river', 'key: 12, plaintext: sjwfs', 
'key: 11, plaintext: tkxgt', 'key: 10, plaintext: ulyhu', 'key: 9, plaintext: vmziv', 
'key: 8, plaintext: wnajw', 'key: 7, plaintext: xobkx', 'key: 6, plaintext: ypcly', 
'key: 5, plaintext: zqdmz', 'key: 4, plaintext: arena', 'key: 3, plaintext: bsfob', 'key: 2, plaintext: ctgpc'])
[17, 8, 21, 4, 17]
Cipher text:  EVIRE
[0, 17, 4, 13, 0]
Cipher text:  EVIRE"""
