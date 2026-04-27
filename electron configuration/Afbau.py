
name = { 0 : 's' , 1 : 'p' , 2 : 'd' , 3 : 'f' , 4 : 'g' , 5 : 'h' , 6 : 'i' , 7 : 'k' , 8 : 'l' , 9 : 'm' , 10 : 'n' , 11 : 'o'  , 12 : 'q' , 13 : 'r' , 14 : 't' , 15 : 'u' , 16 : 'v' , 17 : 'w' , 18 : 'x' , 19 : 'y' , 20 : 'z'}
num = len(name)
def func(num,list):
    for n in range(num + 1):
        for i in range(0,n):
            list.append(str(n) + name[i])

orbitals = []

func(num,orbitals)


n_list = []
def n_listm(arr, name):
    for i in range(len(arr)):
        q = arr[i]
        if len(q) == 2:
            n_list.append(int(q[0]))
        if len(q) == 3:
            n_list.append(int(q[0:-1]))
    
    return n_list

n_listm(orbitals,name)



nl_list = []
def nl_listm(arr,name):
    for i in range(len(arr)):
        q = arr[i]
        for j in range(len(name)):
            if name[j] == q[-1]:
                if len(q) == 3:
                    nl_list.append(int(q[0:-1]) + j)
                if len(q) == 2:
                    nl_list.append(int(q[0]) + j)
                    
                
                    
                
    return nl_list

nl_listm(orbitals,name)


def supersort(arr,n_list,nl_list):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if nl_list[j] > nl_list[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                n_list[j] , n_list[j+1] = n_list[j+1] , n_list[j]
                nl_list[j] , nl_list[j+1] = nl_list[j+1] , nl_list[j]
            
            elif nl_list[j] == nl_list[j+1]:
                if n_list[j] > n_list[j+1]:
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
                    n_list[j] , n_list[j+1] = n_list[j+1] , n_list[j]
                    nl_list[j] , nl_list[j+1] = nl_list[j+1] , nl_list[j]
    return arr,n_list,nl_list

supersort(orbitals,n_list,nl_list)




