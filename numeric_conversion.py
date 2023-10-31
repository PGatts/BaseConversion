# Param Gattupalli
# COP 3502C Project 4: Numeric Conversion
# 10/1/23
import math

# Print menu and receive user input
def print_menu():
    print("Decoding Menu")
    print('-------------')
    print('1. Decode hexadecimal')
    print('2. Decode binary')
    print('3. Convert binary to hexadecimal')
    print("4. Quit")

    return int(input("\nPlease enter an option: "))

# Convert hexadecimal character to decimal value
def hex_char_decode(digit):
    # Return the value if it is already a digit
    if digit.isdigit():
        return int(digit)

    # Return the value if it is not a digit
    return ord(digit.upper()) - 55

# Convert hexadecimal string to decimal value
def hex_string_decode(hex):
    # Remove '0x' from string if it at the start
    if hex[0:2] == '0x':
        hex = hex[2:]

    # Convert each digit starting from the right
    power, result = 0,0
    for i in hex[::-1]:
        result += hex_char_decode(i) * math.pow(16, power)
        power += 1

    return int(result)

# Convert binary string to decimal value
def binary_string_decode(binary):
    # Remove '0b' from string if it is at the start
    if binary[0:2] == '0b':
        binary = binary[2:]

    # Convert each digit starting from the right
    power, result = 0, 0
    for i in binary[::-1]:
        result += int(i) * math.pow(2,power)
        power += 1
    return int(result)

# Convert binary string to hexadecimal string
def binary_to_hex(binary):
    # Remove '0b' from string if it is at the start
    if binary[0:2] == '0b':
        binary = binary[2:]

    # Iterate through and convert of four binary digits to 1 hexadecimal digit
    result_string, start_index = '', len(binary) % 4
    print(start_index)
    for i in range(int(len(binary)/4)):
        sect = binary[4 * i + start_index: 4 * i + 4 + start_index]
        print(sect)
        sect_value = binary_string_decode(sect)
        print(sect_value)
        if sect_value < 10:
            result_string += str(sect_value)
        else:
            result_string += chr(sect_value + 55)
        print(result_string)

    # Convert the start of the binary string to 1 hexadecimal digit
    start = binary[:start_index]
    start_value = 0
    while 0 < len(start) < 4:
        start = '0' + start
        start_value = binary_string_decode(start)


    if start_value == 0:
        return result_string
    elif start_value < 10:
        return str(start_value) + result_string
    else:
        return chr(start_value + 55) + result_string


def main():
    choice = 0
    # Display menu until user selects exit option
    while choice != 4:
        choice = print_menu()
        # Perform appropriate function based on user input
        match choice:
            case 1:
                print("Result:", hex_string_decode(input("Please enter the numeric string to convert: ")))
                print()
            case 2:
                print("Result:", binary_string_decode(input("Please enter the numeric string to convert: ")))
                print()
            case 3:
                print("Result:", binary_to_hex(input("Please enter the numeric string to convert: ")))
                print()
            case 4:
                print("Goodbye!")
                exit()


if __name__ == '__main__':
    main()