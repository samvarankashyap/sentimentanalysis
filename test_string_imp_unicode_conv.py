# -*- coding: utf-8 -*-
import re
import unicodedata

s = u"‘Then I was right.’"

print unicodedata.normalize("NFKD",s).encode('ascii','ignore')
#chars_to_remove = ['‘']
#s.translate(None,''.join(chars_to_remove))
#rx = '['+re.escape(''.join(chars_to_remove))+']'
#s=re.sub(rx,"\'",s)
#print s 
