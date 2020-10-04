def multiples():
    my_list = [i for i in range(1000)]
    x = 0
    new_list = []
    while(x<len(my_list)):
        if(my_list[x] % 3 == 0 or my_list[x] % 5 == 0):
            # print(my_list)
            new_list.append(my_list[x])
        else:
            pass
        x = x + 1
    print(sum(new_list))


multiples()

