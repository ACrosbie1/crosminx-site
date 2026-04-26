import base64,re 
from PIL import Image 
from io import BytesIO 
html=open('index.html','r',encoding='utf-8').read() 
b64=re.search(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)',html).group(1) 
img=Image.open(BytesIO(base64.b64decode(b64))).convert('RGBA') 
w,h=img.size 
print('Size:',w,h) 
img2=img.crop((0,0,w,int(h*0.88))) 
buf=BytesIO() 
img2.save(buf,format='PNG') 
nb=base64.b64encode(buf.getvalue()).decode() 
html2=html.replace(b64,nb) 
open('index.html','w',encoding='utf-8').write(html2) 
print('DONE') 
