import re

phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_num_regex.search('Cell: 415-555-4242 Work: 212-555-0000')
print(mo.group())

mo1 = phone_num_regex.findall('Cell: 415-555-4242 Work: 212-555-0000')
print(mo1)

phone_num_regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo2 = phone_num_regex.findall('Cell: 415-555-4242 Work: 212-555-0000')
print(mo2)
