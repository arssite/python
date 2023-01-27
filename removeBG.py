#pip install rembg
from rembg import remove
with open('1.png','rb') as inp:
  with open('2.png','wb') as out:
    input=inp.read()
    output=remove(input)
    out.write(output)
