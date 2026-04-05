import art as at
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(at.logo)
running = True

while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(original_text, shift_amount, encode_or_decode):
        new_text = ""
        for letter in original_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if encode_or_decode == "encode":
                    new_position = (position + shift_amount) % 26
                else:
                    new_position = (position - shift_amount) % 26
                new_text += alphabet[new_position]
            else:
                new_text += letter
        print(new_text)

    if direction == "encode" or direction == "decode":
        caesar(original_text = text, shift_amount = shift, encode_or_decode = direction)
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")

    should_continue = input("Would you like to continue yes or no?\n").lower()
    if should_continue != "yes":
        running = False
        print("Goodbye!")

