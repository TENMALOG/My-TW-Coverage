import sys
sys.path.insert(0,'.')
from q083_chk import load
import re
t,p=sys.argv[1],int(sys.argv[2])
d,pages=load(t)
s=pages[p]
s=re.sub(r'[ \t]+',' ',s)
s=re.sub(r'\n(?=[^\n]{0,12}\n)',' ',s)
print(s[:int(sys.argv[3]) if len(sys.argv)>3 else 3500])
