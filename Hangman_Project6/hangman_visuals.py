# Raw strings (r"") tell Python to ignore escape sequences.
stages = [r'''
    +---+
    |   |
        |
        |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
        |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========
''']


print(r'''      
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''')