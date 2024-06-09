import base64
pic = open('fdf.jpg','rb')
byteform=base64.b64encode(pic.read())
f=open('output2.bin','wb')
f.write(byteform)  
f.close() 
