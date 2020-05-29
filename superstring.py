def stringapp():
    a = input()
    b = input()
    k = int(input())
    count = 0
    op = 0
    a_list = [str(i) for i in a]
    b_list = [str(i) for i in b]
    print (a_list)
    print (b_list)
    for i in b_list:
        if i not in a_list:
            a_list.append(i)
            op+=1
    print ("append")
    print (a_list)
    for j in a_list:
        if j not in b_list:
            a_list.remove(j)
            op+=1
    print ("delete")
    print (a_list)
    print (op)
stringapp()
