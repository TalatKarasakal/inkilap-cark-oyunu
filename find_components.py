import re

text = open(r'C:\Users\M.ATA\Desktop\LGS Cark Oyunu (standalone).html', 'r', encoding='utf-8', errors='ignore').read()
matches = re.findall(r'"id":"([^"]+)"', text)
print(f'Found {len(matches)} component IDs:')
for m in matches:
    print(' -', m)
