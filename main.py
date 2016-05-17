#!/usr/local/bin/python

import csv
f = open('sequence.txt','r').read()

import matplotlib.pyplot as plt

class TOOLS:
    def __init__(self):
        pass

    def polymerization(self,base):
        if base == 'a': return 't'
        if base == 't': return 'a'
        if base == 'g': return 'c'
        if base == 'c': return 'g'

    def GC_content(self,replicated,GCC):
        GCC.append(((replicated.count('g')+replicated.count('c'))/float((replicated.count('a')+replicated.count('t')+replicated.count('g')+replicated.count('c'))))*100)
        return GCC

    def GC_skew(self,replicated,GCS,point):
        GCS.append((replicated.count('c')-replicated.count('g'))/float((replicated.count('c')+replicated.count('g'))))

    def cum_GC_skew(self,GCS,cum):
        cum.append(sum(GCS))

window = 10000
replicated,GCC,GCS,point,cum = [],[],[],[],[]
i = 1
for base in f:
    replicated.append(TOOLS().polymerization(base))
    #TOOLS().GC_content(replicated,GCC)
    if i % window == 0:
        target = f[i-window/2:i+window/2]
        TOOLS().GC_skew(target,GCS,point) #GCskew
        TOOLS().cum_GC_skew(GCS,cum) #cum_GCskew
        point.append(i)
    i += 1

plt.subplot(1,2,1)
plt.plot(point,GCS,'r')
plt.title("GCskew")
plt.xlabel("bp")
plt.ylabel("GCskew")
plt.subplot(1,2,2)
plt.plot(point,cum,'r')
plt.title("Cumulative GCskew")
plt.xlabel("bp")
plt.ylabel("Cumulative GCskew")
plt.show()
#plt.savefig("GCskew.png")
