#!/usr/bin/python3
'''Module 0-validate_utf8
Contains functions validUTF8(data) and decimalToBinary(num)'''


def decimalToBinary(n):
    '''Converts an integer decimal to its binary representation.'''
    return bin(n).replace("0b", "")


def validUTF8(data):
    '''Returns True if data is a valid UTF-8 encoding, else return False
    data is a list of integers, each integer representing a byte'''
    # print("Checking", data, '...')

    i = 0
    while i < len(data):
        # print("Checking", data[i])
        # For 1 byte characters
        if len(decimalToBinary(data[i])) < 8:
            i += 1
            continue

        # Test if the byte is represents a 2 byte UTF-8 character
        elif decimalToBinary(data[i])[0:3] == '110' and i + 1 < len(data):
            # Check if the next bytes are valid bytes for a 2 byte UTF-8
            # character
            secondChar = decimalToBinary(data[i + 1])

            # If the byte's length is less than 8,
            # it means their binary representation starts with 0.
            # Hence, it's invalid
            if len(secondChar) < 8:
                return False
            elif secondChar[0:2] == '10':
                # UTF-8 char is valid, continue to the next character
                i += 2
                continue

        # Test if the byte is represents a 3 byte UTF-8 character
        elif decimalToBinary(data[i])[0:4] == '1110' and i + 2 < len(data):
            # Check if the next bytes are valid bytes for a 2 byte UTF-8
            # character
            secondChar = decimalToBinary(data[i + 1])
            thirdChar = decimalToBinary(data[i + 2])

            # If one of the bytes' length is less than 8,
            # it means their binary representation starts with 0.
            # Hence, it's invalid
            if len(secondChar) < 8 or len(thirdChar) < 8:
                return False
            elif secondChar[0:2] == '10' and thirdChar[0:2] == '10':
                # UTF-8 char is valid, continue to the next character
                i += 3
                continue

        # Test if the byte is represents a 4 byte UTF-8 character
        elif decimalToBinary(data[i])[0:5] == '11110' and i + 3 < len(data):
            # Check if the next bytes are valid bytes for a 2 byte UTF-8
            # character
            secondChar = decimalToBinary(data[i + 1])
            thirdChar = decimalToBinary(data[i + 2])
            fourthChar = decimalToBinary(data[i + 3])

            # If one of the bytes' length is less than 8,
            # it means their binary representation starts with 0.
            # Hence, it's invalid
            if (len(secondChar) < 8 or len(thirdChar) < 8 or
                    len(fourthChar) < 8):
                return False
            elif (secondChar[0:2] == '10' and thirdChar[0:2] == '10' and
                  fourthChar[0:2] == '10'):
                # UTF-8 char is valid, continue to the next character
                i += 4
                continue
        else:
            return False
    # When all checks pass, return True
    return True
	