import re

with open('categories/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace all #FFD700 with Silver and Bronze for 2nd and 3rd respectively.
# Since the previous script wrote:
# <div class="text-[10px] font-label-sm text-on-surface-variant mb-1">1ST</div>
# <div class="font-display-lg text-body-md font-bold text-[#FFD700]">...</div>
# 
# We can just do a regex replace to fix the 2nd and 3rd colors.
# For 2ND:
content = re.sub(
    r'(<div class="text-\[10px\] font-label-sm text-on-surface-variant mb-1">2ND</div>\s*<div class="font-display-lg text-body-md font-bold text-)\[#FFD700\](">)',
    r'\g<1>[#C0C0C0]\g<2>',
    content
)

# For 3RD:
content = re.sub(
    r'(<div class="text-\[10px\] font-label-sm text-on-surface-variant mb-1">3RD</div>\s*<div class="font-display-lg text-body-md font-bold text-)\[#FFD700\](">)',
    r'\g<1>[#CD7F32]\g<2>',
    content
)

with open('categories/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
