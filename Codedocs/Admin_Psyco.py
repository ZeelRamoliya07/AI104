size = int(input())
list1 = input().split()
if (len(list1) != size):
    print('invalid')
else:
    for i in range(0,size):
        list1[i] = int(list1[i])
    
    list_sort = [0]*size
    
    for i in range(0,size):
        list_sort[i] = list1[i]
    
    list_sort.sort()
    
    firstindex = 0
    lastindex = size-1
    
    count = 0
    
    while(list_sort != list1):
        mini = min(list1)
      
        if(mini !=  list1[firstindex]):
            
            index_of_mini = list1.index(mini)
            temp = list1[firstindex]
            list1[firstindex] = list1[index_of_mini]
            list1[index_of_mini] = temp
            
            list1.pop(0)
            list_sort.pop(0)
         
            count += 1
        else:
            pass
            

    print(count)