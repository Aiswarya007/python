text = input("Enter a text: ")
shift_value = input("Enter shift value: ")
cipher = ''
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            code = ord(ch) + int(shift_value)
            if code > 90:
                code = code - 90
                code = 64 + code
            cipher += chr(code)

        if ch.islower():

            code = ord(ch) + int(shift_value)
            if code > 122:
                code = code - 122
                code = 96 + code
            cipher += chr(code)
    else:
        cipher += ch


print(cipher)
