# Ex 1 


# #ERIC'S SOLUTION
# def some_function(a,b):
    
#     for i in a:
#         if (i*i) in b:
#             pass
#         else:    
#             return False
#     return True

# print(some_function(a, e))


#DAVID'S SOLUTION
# def power_of(a,b):
#     dict_a = {}
#     dict_b = {}
#     if len(a) == len(b):
#         for i in range(len(a)):
#             base[index] = a[index]
#         for index in range(len(b)):
#             base[index] = b[index]
#         for key in base.keys():
#             for k in compare.keys():
#                 if (base[key] * base[key]) == compare[k]:
#                     num_of_matches += 1
#     else:
#         return print("ERROR: The lengths of lists do not match, cannot")

#COMPROMISE
def some_function(a,b):
    dict_a = {}
    dict_b = {}
    boolean_stop = False
    if len(a) == len(b):
        for i in a:
            dict_a[i] = i
        for k in b:
            dict_b[k] = k
        for x in dict_a:
            for y in dict_b:
                if (dict_a[x]**2) == dict_b[y]:
                    boolean_return = True
                    break
                else:
                    boolean_return = False
                    boolean_stop = boolean_return
        return boolean_stop
        
#outside the function
a = [1,2,3,4]
b = [1,4,9,16]
c = [1,4,5,6]
d = [1,4,4,2]
e = [1,16,9,4]
f = [1,2,3,4,5]

print(some_function(a,e))