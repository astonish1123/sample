
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

print('Phone number is 415-555-4242')
print(is_phone_number('415-555-4242'))
print('Phone number is moshi moshi')
print(is_phone_number('moshi moshi'))
message = "Please call 415-555-1011. To office, 415-555-9999"
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('The phone number is found: ' + chunk)
print('Complete!')

