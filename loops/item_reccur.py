l=["a","b","c","v","b","c"]
b={}
for item in l:
    if item in b:
        b[item]+=1
    else:
        b[item]=1
print(b)