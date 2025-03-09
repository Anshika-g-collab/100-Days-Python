alphabet = ['a' , 'b' ,'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo = r"""
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                   

"""


print(logo)

def ceaser(start_text,shift_amount,cipher_direction):
    if cipher_direction == 'decode':
        shift_amount*=-1
    end_text=""
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

    

should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt ,\nType 'decode' to decrypt: \n").lower()

    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%26
    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        should_end = True
        print('Goodbye!👋')
