import re

text = open('standalone_body.html', 'r', encoding='utf-8').read()

themes = re.findall(r'data-theme="([^"]+)"', text)
print("Data themes found:", set(themes))

classes = re.findall(r'class="([^"]+)"', text)
print(f"Total class attributes: {len(classes)}")

unique_classes = set(classes)
print("\nKey UI Classes:")
for c in sorted(unique_classes):
    if any(k in c for k in ['theme', 'wood', 'card', 'wheel', 'btn', 'panel', 'nav', 'header', 'parchment']):
        print(" -", c)
