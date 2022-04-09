alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_wants = True
while user_wants:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text,shift_amt):
        new_text = ""
        for i in range(0,len(plain_text)):
            index = alphabet.index(text[i])
            pos = index + shift_amt + 5
            while pos >=26:
                pos = pos - 26
            new_text += alphabet[pos]    
                
        print(f"The encoded message is {new_text}")

    def decrypt(plain_text,shift_amt):
        new_text = ""
        for i in range(0,len(plain_text)):
            index = alphabet.index(text[i])
            pos = index - shift_amt - 5
            while pos < 0:
                pos = pos + 26
            new_text += alphabet[pos] 
                
        print(f"The decoded message is {new_text}")    

    if direction == "encode":
        encrypt(text,shift)

    elif direction == "decode": 
        decrypt(text,shift)

    else:
        print("Please enter either encode or decode only.")

    want = input("Type yes if you want to go again. Type no to exit\n")

    if want == "yes":
        user_wants = True
    elif want == "no":
        user_wants = False

print("Until next time!")
