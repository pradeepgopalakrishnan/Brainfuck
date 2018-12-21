import PIL
import numpy as np
import matplotlib.pyplot as plt
import sys

filename=sys.argv[1]
img_=np.asarray(PIL.Image.open(filename))
img=img_.copy()
plt.imshow(img)
plt.show()

imgrows=int(sys.argv[2])
imgcols=int(sys.argv[3])
rows=img.shape[0]
cols=img.shape[1]

rw=rows/imgrows
cw=cols/imgcols
values=[]
for i in range(imgrows):
    for j in range(imgcols):
        val=img[int((0.5+i)*rw)][int((0.5+j)*cw)]
        print(val)
        values.append(val[:-1])
#print(values)

color={
    '<':[255,0,0],
    '>':[128,0,0],
    '+':[0,255,0],
    '-':[0,128,0],
    '.':[0,0,255],
    ',':[0,0,128],
    '[':[255,255,0],
    ']':[128,128,0],
    'r':[0,255,255],
    'l':[0,128,128],
    '0':[0,0,0]
}

colorinv=dict((tuple(v),k) for k,v in color.iteritems())

revcode=''
for x in values:
    revcode+=colorinv[tuple(x)]
length=len(revcode)
nchunks=length/imgcols
code=''
for i in range(nchunks):
    if(i%2==0):
        code+=revcode[i*imgcols:(i+1)*imgcols]
        
    else:
        code+=revcode[i*imgcols:(i+1)*imgcols][::-1]
for char in "rl0":
    code=code.replace(char, "")
f=open(sys.argv[4],'w')
f.write(code)
f.close()
