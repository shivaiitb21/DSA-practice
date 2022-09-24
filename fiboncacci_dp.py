# Memoization - dynamic programming

def fibdp(m,d):
    if m in d:
        return d[m]

    else:
        d[m] = fibdp(m-1,d)+fibdp(m-2,d)
        return d[m]
    
d = {0:1,1:1}

print(fibdp(9,d))


