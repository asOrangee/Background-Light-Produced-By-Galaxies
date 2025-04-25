import numpy as np
from scipy.interpolate import interp2d

data=np.loadtxt('./dn_dM.txt',skiprows=1)

# mass outputs per redshift
n=1001

gridx=[]
i=0
while (i*n <len(data[:,0])):
      gridx.append( data[i*n,0])
      i=i+1

gridx=np.array(gridx)

gridy=np.zeros(n)
# use log10(M)
gridy=np.log10(data[0:n,1])


values=data[:,2].reshape(len(gridy),len(gridx),order='F')

interp=interp2d(gridx,gridy,values,kind='cubic')

def mf(M,z):
    aa=interp(z,np.log10(M)) 
    if(len(aa)==1):
      return aa[0]
    else:
      return aa


z=4.13
M=1.2e5

aa=mf(M,z )

print(aa)


