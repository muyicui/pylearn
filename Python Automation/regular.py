import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 123-242-2123, your number is 123-123-1241')
print(type(phoneNumRegex))
print(type(mo))
print('Phone number found:'+mo.group(0))
print(mo.groups())
