import re

text = 'some text around text'

# re.search()
# re.findall()
# re.finditer()
# re.sub()
# re.split()

patterns = {
    'simple term': r'around',
    'not number': r'\D+',
    'words': r'\b(\w+)\b'    # 'hello my friends'
}

print(re.search(patterns['simple term'], text))

print(re.search(patterns['not number'], '23875632fhbadkjhbs')[0])

