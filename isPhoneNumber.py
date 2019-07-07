import re

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return Flase
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

if __name__ == '__main__':
##    print('415-555-4242 is phone number')
##    print(is_phone_number('415-555-4242'))
    
    message = 'Please call me back to this phone number: 415-555-1011 or office number: 415-555-9999'

##    for i in range(len(message)):
##        chunk = message[i:i+12]
##        if is_phone_number(chunk):
##            print('The phone number is found: '+ chunk)
##    print('done')

    phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phone_num_regex.search('My phone number is 415-555-4242')
    print('Your phone number is found: ' + mo.group())

    mo2 = phone_num_regex.findall(message)
    print(mo2)
    
