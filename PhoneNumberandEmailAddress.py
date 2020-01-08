import pyperclip
import re

def phone_regex(matches, text):
    phone_re = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)

    for groups in phone_re.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != ' ':
            phone_num += ' x'+ groups[8]
        matches.append(phone_num)              

def email_regex(matches, text):
    email_re = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2, 4})
        )''', re.VERBOSE)

    for groups in email_re.findall(text):
        matches.append(groups[0])

def url_regex(matches, text):
    url_re = re.compile(r'''(
        (http|https)
       (:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)
        )''', re.VERBOSE)
    for groups in url_re.findall(text):
        matches.append(groups[0])

if __name__ == '__main__':
    
    text = str(pyperclip.paste())
    matches = []
##    phone_regex(matches, text)
##    email_regex(matches, text)
    url_regex(matches, text)
                             
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied in clipboard: ')
        print('\n'.join(matches))
    else:
        print('No phone number, email address, and url')


