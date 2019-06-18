import re

xmas_regex = re.compile(r'\d+\s\w+')
print(xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 pertridge'))

vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('RoboCop eats baby food. BABY FOOD'))

begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello world'))
print(begins_with_hello.search('He said Hello.'))

ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('your number is 42'))
print(ends_with_number.search('you are 42 years old.')==None)

whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('123456789'))
print(whole_string_is_num.search('12345xy6789')==None)
print(whole_string_is_num.search('12345 6789')==None)

at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'))

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

nongreedy_regex = re.compile(r'<.*?>')
mo1 = nongreedy_regex.search('<To serve man> for dinner.>')
print(mo1.group())
greedy_regex = re.compile(r'<.*>')
mo2 = greedy_regex.search('<To serve man> for dinner.>')
print(mo2.group())

no_newline_regex = re.compile(r'.*')
print(no_newline_regex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.').group())
newline_regex = re.compile(r'.*', re.DOTALL)
print(newline_regex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.').group())

