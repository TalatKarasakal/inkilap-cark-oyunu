import re
import json
import gzip
import base64

desktop_file = r'C:\Users\M.ATA\Desktop\LGS Cark Oyunu (standalone).html'

with open(desktop_file, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find JSON script blocks
pattern = r'\{"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}":\{"mime":.*?\}\}'
matches = re.findall(pattern, text)
print(f'Found {len(matches)} bundled assets in file.')

for i, m in enumerate(matches):
    try:
        obj = json.loads(m)
        for key, val in obj.items():
            mime = val.get('mime', '')
            compressed = val.get('compressed', False)
            b64_data = val.get('data', '')
            raw_bytes = base64.b64decode(b64_data)
            if compressed:
                raw_bytes = gzip.decompress(raw_bytes)
            content = raw_bytes.decode('utf-8', errors='ignore')
            print(f"Asset #{i+1} [{key}] (Type: {mime}, Length: {len(content)})")
            if 'text/jsx' in mime or 'text/html' in mime or len(content) < 5000:
                print(content[:300].encode('ascii', 'ignore').decode('ascii'))
    except Exception as e:
        print(f"Error parsing asset {i}: {e}")
