from collections import Counter
import string
 
fin = open('pdfs.txt','r')
words = fin.read().lower()
out = words.translate(string.maketrans("",""), string.punctuation)
fin.close()
 
wordss = out.split()
 
cnt = Counter(wordss)
 
fout = open('counts.txt','w')
for k, v in cnt.items():
    print k+','+str(v)+'\n'
    fout.write(k + "," + str(v) + '\n')
fout.close()
