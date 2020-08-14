def some_function(a,b):
    if len(a)==len(b):
        pass
    else:
        return False

    # dict_a = {}
    # dict_b = {}

    for char in a:
        if char in b:
            pass
        else:
            return False
    return True
    
    # for i in a:
    #     if i in dict_a:
    #         dict_a[i] += 1
    #     else: 
    #         dict_a[i] = 1

    # for j in b:
    #     if j in dict_b:
    #         dict_b[j] += 1
    #     else: 
    #         dict_b[j] = 1

    # for k in dict_a:
    #     if k in dict_b:
    #         if dict_a[k] == dict_b[k]:
    #             pass
    #         else:
    #             return False
    #     else:
    #         return False
    # return True

a = "pie"
b = "eip"
c = "pies"
d = "pwe"

print(some_function(a, d))