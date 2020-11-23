import unicodedata
import random

# Unicode codepoints are divided into categories. We
# generate codepoints in the first 16 bit range, but
# skip those in unassigned, internal, and control ranges.
def randchar(category_blacklist=['Cs', 'Co', 'Cn']):
    while True:
        c = chr(random.randint(1, 2**16))
        if unicodedata.category(c) not in category_blacklist:
            return c

def randstr(length):
    return ''.join(randchar() for _ in range(length))