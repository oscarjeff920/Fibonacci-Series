def Fib(Term1 = 0, Term2 = 1, MaxTerm = 20):
    if MaxTerm > 100:
        MaxTerm = 100
    elif MaxTerm < 1:
        MaxTerm = 1
        
    global L
    L = [Term1, Term2]
    for n in range(MaxTerm):
        if n != 0:
            L.append(L[n] + L[n-1])
    return L
print(Fib())