import matplotlib.pyplot as plt
import numpy as np
import sys

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

filename=sys.argv[1]
f=open(filename, 'r')
code=f.read().strip()


cols=int(sys.argv[2])

codelen=len(code)
chunks=[]
i=cols-1
chunks.append(code[0:cols-1])
while(i<codelen):
    chunks.append(code[i:i+cols-2])
    i+=cols-2
nchunks=len(chunks)
for i in range(nchunks-1):
    if(i%2==0):
        chunks[i]+='rr'
    else:
        chunks[i]+='ll'
while(len(chunks[nchunks-1])!=(cols-1)):
    chunks[nchunks-1]+='0'
appcode=''
for i in range(nchunks):
    appcode+=chunks[i]

rows=len(appcode)/cols
achunks=[]
for i in range(rows):
    if(i%2==0):
        achunks.append(appcode[i*cols:(i+1)*cols])
    else:
        achunks.append(appcode[i*cols:(i+1)*cols][::-1])

dims=(len(achunks), cols, 3)
arr=np.zeros(dims)
for i in range(len(achunks)):
    for j in range(cols):
        arr[i][j][0]=color[achunks[i][j]][0]/255.
        arr[i][j][1]=color[achunks[i][j]][1]/255.
        arr[i][j][2]=color[achunks[i][j]][2]/255.

print(code)
plt.imshow(arr,cmap='jet')
plt.show()
plt.imsave(sys.argv[3], arr)
#print(achunks)

