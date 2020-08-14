# Ex 1 

def some_function(a,b):
    dict_a = {}
    dict_b = {}
    
    for i in a:
        if i in dict_a:
            dict_a[i] += 1
        else: 
            dict_a[i] = 1

    for j in b:
        if j in dict_b:
            dict_b[j] += 1
        else: 
            dict_b[j] = 1

    for k in dict_a:
        if k in dict_b:
            if dict_a[k] == dict_b[k]:
                pass
            else:
                return False
        else:
            return False
    return True

a = [1,2,3,4]
b = [1,4,5,6]
c = [1,4,4,2]
d = [1,4,3,2]
e = [1,2,3,4,5]

print(some_function(b, e))

