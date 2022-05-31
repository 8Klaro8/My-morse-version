

abc_morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.',
                  'd': '-..', 'e': '.', 'f': '..-.',
                  'g': '--.', 'h': '....', 'i': '..',
                  'j': '.---', 'k': '-.-', 'l': '.-..',
                  'm': '--', 'n': '-.', 'o': '---',
                  'p': '.--.', 'q': '--.-', 'r': '.-.',
                  's': '...', 't': '-', 'u': '..-',
                  'v': '...-', 'w': '.--', 'x': '-..-',
                  'y': '-.--', 'z': '--..'}

def to_morse_converter(my_input):
    # This is where I will store the morse text that has been translated.
    morse_text = ''

    # Iterate over in "my_input", aka the message, letter by letter.
    for letter in my_input:

        # if the current letter is not a space then execute, otherwise do nothing.
        if letter != ' ':

            # using the current letter, I get the corresponding morse sign from the list and add it to the
            # "morse_text". Add space at the end so that the decoding will work.
            morse_text += abc_morse_dict[letter] + ' '

    return morse_text

def from_morse_converter(my_input):
    # First I split the "my_input" so that when I iterate over, it will not check per
    # each letter/ character, but it will check after each sign, using space as the indicator
    my_input = my_input.split(' ')

    # I will store the translated letters
    morse_code = ''

    # Loop thru in the message("my_input")
    for code in my_input:


        for (key,value) in abc_morse_dict.items():

            # If the value(sign) is equal to the iterated
            # code/sign then add the corresponding letter to "morse_code"
            if code == value:

                # Adding a dot at the end to make the reading easier
                morse_code += key + '.'

    return morse_code



choice = input('Translate morse(M) or ABC(A)?').lower()
my_input = input('Enter your message to convert:\n')
if choice == 'm':
    print(from_morse_converter(my_input))

elif choice == 'a':
    print(to_morse_converter(my_input))

