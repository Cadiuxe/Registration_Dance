import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

prizes = {
    'Junior Solo': ('₹10,000', '₹7,500', '₹5,000'),
    'Senior Solo': ('₹15,000', '₹10,000', '₹7,500'),
    'Duet': ('₹25,000', '₹15,000', '₹10,000'),
    'Group Junior': ('₹50,000', '₹30,000', '₹20,000'),
    'Group Senior': ('₹1,00,000', '₹50,000', '₹30,000')
}

html_template = """</a>
            <div class="category-card-v2__prize-pool" style="margin-top: 1.5rem; margin-bottom: 1rem;">
              <div style="font-family: 'Space Grotesk', sans-serif; font-size: 10px; letter-spacing: 0.1em; color: var(--on-surface, #e3e2e2); margin-bottom: 12px; text-transform: uppercase;">Prize Pool Breakdown</div>
              <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;">
                <div style="background: var(--surface-container-lowest, #0d0e0f); padding: 12px; border-radius: 4px; text-align: center; border: 1px solid rgba(170, 137, 135, 0.2);">
                  <div style="font-family: 'Space Grotesk', sans-serif; font-size: 10px; color: var(--on-surface-variant, #e3bebb); margin-bottom: 4px;">1ST</div>
                  <div style="font-family: 'Anybody', sans-serif; font-size: 16px; font-weight: 700; color: #FFD700;">{p1}</div>
                </div>
                <div style="background: var(--surface-container-lowest, #0d0e0f); padding: 12px; border-radius: 4px; text-align: center; border: 1px solid rgba(170, 137, 135, 0.2);">
                  <div style="font-family: 'Space Grotesk', sans-serif; font-size: 10px; color: var(--on-surface-variant, #e3bebb); margin-bottom: 4px;">2ND</div>
                  <div style="font-family: 'Anybody', sans-serif; font-size: 16px; font-weight: 700; color: #C0C0C0;">{p2}</div>
                </div>
                <div style="background: var(--surface-container-lowest, #0d0e0f); padding: 12px; border-radius: 4px; text-align: center; border: 1px solid rgba(170, 137, 135, 0.2);">
                  <div style="font-family: 'Space Grotesk', sans-serif; font-size: 10px; color: var(--on-surface-variant, #e3bebb); margin-bottom: 4px;">3RD</div>
                  <div style="font-family: 'Anybody', sans-serif; font-size: 16px; font-weight: 700; color: #CD7F32;">{p3}</div>
                </div>
              </div>
            </div>
            <div class="category-card-v2__contact">"""

for cat, (p1, p2, p3) in prizes.items():
    # Find the block for this category. We'll split by the title
    parts = content.split(f'<h3 class="category-card-v2__title">{cat}</h3>')
    if len(parts) > 1:
        # Looking for the end of the Register Now button and the start of the contact div
        # Regex to match </a> followed by <div class="category-card-v2__contact"> with any whitespace
        pattern = re.compile(r'</a>\s*<div class="category-card-v2__contact">')
        replacement = html_template.format(p1=p1, p2=p2, p3=p3)
        parts[1] = pattern.sub(replacement, parts[1], count=1)
        content = f'<h3 class="category-card-v2__title">{cat}</h3>'.join(parts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
