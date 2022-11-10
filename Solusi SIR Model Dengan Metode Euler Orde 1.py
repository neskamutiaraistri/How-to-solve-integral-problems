import numpy as neska
import matplotlib.pyplot as nsk

to = 0
tn = 300
ndata = 1000

t = neska.linspace(to,tn,ndata)
h = t[2]-t[1]


N = 1000 #rakyat
I0 = 1
R0 = 0
S0 = N - I0 - R0

I = neska.zeros(ndata)
S = neska.zeros(ndata)
R = neska.zeros(ndata)

I[0] = I0
R[0] = R0
S[0] = S0

beta = 0.2
gamma = 0.1

for i in range (0,ndata-1):
    S[i+1] = S[i] - h*beta/N*S[i]*I[i]
    I[i+1] = I[i] + h*beta/N*S[i]*I[i] - h*gamma*I[i]
    R[i+1] = R[i] + h*gamma*I[i]

nsk.plot(t,S,label ='S')
nsk.plot(t,I,label = 'I')
nsk.plot(t,R,label = 'R')

nsk.legend()
nsk.show()
