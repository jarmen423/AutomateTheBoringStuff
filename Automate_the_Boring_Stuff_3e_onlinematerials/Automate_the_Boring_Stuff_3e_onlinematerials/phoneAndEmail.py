import pyperclip, re

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First 3 digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # username
    @  # @ symbol
    [a-zA-Z0-9.-]+  # domain name
    (\.[a-zA-Z]{2,4}){1,2}  # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_re.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
