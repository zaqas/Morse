morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
         'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
         'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
         'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',

         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
         ',': '--..--', '.': '.-.-.-', '?': '..--..', '"': '.-..-.', ':': '---...', "'": '.----.',
         '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '_': '..--.-', '+': '.-.-.', ';': '-.-.-.'
         }

reversed_morse = {value: key for key, value in morse.items()}

choice = int(input('1. Text to Morse\n2. Morse to Text\nPlease choose a mode: '))
user_input = input('Please enter text:\n').lower()

def txt2morse():
    my_list = []
    for letter in user_input:
        my_list.append(morse[letter])
    print(" ".join(my_list))


def morse2text():
    morse_list = []
    for input in user_input.split():
        for items in reversed_morse.keys():
            if input == items:
                morse_list.append(reversed_morse[input])
    print("".join(morse_list))



if choice == 1:
    txt2morse()

elif choice == 2:
    morse2text()

else:
    print('Invalid option. Please choose again.')





