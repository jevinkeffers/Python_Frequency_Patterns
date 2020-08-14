def some_function(a):
    dict_a={}
    max_val = 0

    for i in a:
        if i in dict_a:
            dict_a[i] += 1
        else: 
            dict_a[i] = 1

    for j in dict_a:
        if dict_a[j] > max_val:
            max_val = dict_a[j]
            return_val = j
        

    return return_val

a = "hello"
b = "sprinkle slurps"
c = "car cat cuts crinckles"

print(some_function(c))
