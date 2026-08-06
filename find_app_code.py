import re

text = open(r'C:\Users\M.ATA\Desktop\LGS Cark Oyunu (standalone).html', 'r', encoding='utf-8', errors='ignore').read()

# Print any readable script block or code strings
scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', text)
print(f'Total script tags: {len(scripts)}')

for i, s in enumerate(scripts):
    print(f'Script #{i} length: {len(s)}')
    if 'cark' in s.lower() or 'lgs' in s.lower() or 'unite' in s.lower() or 'soru' in s.lower():
        print(f'>>> Match in script #{i}:')
        print(s[:1000].encode('ascii', 'ignore').decode('ascii'))
