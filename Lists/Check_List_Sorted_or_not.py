a = [1,2,3,2,3,2,5]
flag=0;

for i in a:
    if(i>i+1):
        flag=1
        break;

if(flag==1):
    print("false")
else:
    print("true")
