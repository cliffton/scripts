

# import pdb; pdb.set_trace()
import requests
from bs4 import BeautifulSoup

don = "https://www.cs.rit.edu/~ark/bcbd_2/java2html.php?file="

for i in range(1,81):
    urt = don + str(i)
    req = requests.get(urt)
    thehtml = BeautifulSoup(req.content, 'html.parser')

    pres = thehtml.find_all('pre')
    c = thehtml.find('h2').text.find('Class')
    na = thehtml.find('h2').text[c+6:]
    f = open( "sourceFiles/"+str(na)+".java", 'w')
    f.write(pres[0].text)
    f.close()