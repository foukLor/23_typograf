import re

PATTERNS = [
#unnessary line breaks
(r'\r\n', r'\n'),
#hyphens for dashes 
(r'(?<= )-(?= )', r'—'),
#quotes
(r'([\'"])(.*)(\1)', r'«\2»'),
]

def typograf(text):
    for old_pattern, new_pattern in PATTERNS:
        text = re.sub(old_pattern, new_pattern, text)
    return text