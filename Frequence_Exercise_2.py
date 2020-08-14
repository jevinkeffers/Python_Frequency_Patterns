# Ex 1 

def some_function(a,b):
    
    for i in a:
        if (i*i) in b:
            pass
        else:    
            return False
    return True

a = [1,2,3,4]
b = [1,4,9,16]
c = [1,4,5,6]
d = [1,4,4,2]
e = [1,16,9,4]
f = [1,2,3,4,5]

print(some_function(a, e))

