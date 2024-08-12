import math
m=int(input())
h=m/60
hm=m%60
print(math.floor(h),end=" Hour(s) ")
print(math.floor(hm),end=" Minute(s)")