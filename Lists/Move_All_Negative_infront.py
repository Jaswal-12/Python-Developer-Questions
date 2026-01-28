a = [1, -2, 3, -4, -1, 5]
neg=[]
pos=[]
for i in range(len(a)):
    if(a[i]<0):
        neg.append(a[i])
        
for i in range(len(a)):
    if(a[i]>0):
        pos.append(a[i]);
        
print(neg+pos)
