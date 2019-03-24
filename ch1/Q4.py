
value_set = [True, False]

for i in value_set:
    for j in value_set:
        for k in value_set:
            if ((i and j) or k) == (i and (j or k)):
                print('yes')
            else:
                print('no')
                print((i and j) or k)
                print(i and (j or k))
                print(i and j or k)
                print('a:' + str(i) + ' ,b:' + str(j) + ' ,k:' + str(k))
