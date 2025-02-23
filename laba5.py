import math
b=[]
a= list(range(0,1000000))
for i in range(len(a)):
   c=math.sqrt((a[i]**2)+5)
   if c.is_integer():
           b.append(c)
   if a[i]>=3:
       d=math.sqrt((a[i]**2)-5)
       if d.is_integer():
           b.append(d)
print (b)
