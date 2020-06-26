#!/usr/bin/env python3

import os
path=os.getcwd()
l=os.listdir(path)
ctr=0

for x in l:
    if x[:-4]+".srt" in l and ".srt" not in x:
        if not os.path.isdir(x[:-4]):
            os.mkdir(x[:-4])
        os.rename(path+"/"+x,path+"/"+x[:-4]+"/"+x)
        os.rename(path+"/"+x[:-4]+".srt",path+"/"+x[:-4]+"/"+x[:-4]+".srt")
        ctr+=1

print(str(ctr)+" folder(s) created.")