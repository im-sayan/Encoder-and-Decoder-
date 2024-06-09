import base64
file = open('output2.bin','rb') #enter binary file path of encoded img
b=file.read()
file.close()
cre = open('fdf2.ico','wb')#enter the new created img name with extaintion
cre.write(base64.b64decode(b))
cre.close()

