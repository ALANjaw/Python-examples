
import re

# Read the file and count the occurrences of "terrible"
with open('file_to_read.txt', 'r') as file:
    text = file.read()
    count = len(re.findall(r'\bterrible\b', text))

# Replace even occurrences with "pathetic" and odd occurrences with "marvellous"
replace_text = text.replace('terrible', 'pathetic', count//2)
replace_text = replace_text.replace('terrible', 'marvellous')

# Write the new text to a new file
with open('result.txt', 'w') as file:
    file.write(replace_text)

print(f'Total occurrences of "terrible": {count}')

