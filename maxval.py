if x1>= x2 and x1>=x3:
    maxcal =x1
    
elif x2> = x1 and x2> = x3:
    maxval= x2
    
else:
    maxval = x3
    
    
#a better solution
maxval=x1
if x2> maxval:
    maxval =x2
if x3> maxval:
    maxval = x3
    