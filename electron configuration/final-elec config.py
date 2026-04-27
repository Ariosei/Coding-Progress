name = { 0 : 's' , 1 : 'p' , 2 : 'd' , 3 : 'f' , 4 : 'g' , 5 : 'h' , 6 : 'i' , 7 : 'k' , 8 : 'l' , 9 : 'm' , 10 : 'n' , 11 : 'o'  , 12 : 'q' , 13 : 'r' , 14 : 't' , 15 : 'u' , 16 : 'v' , 17 : 'w' , 18 : 'x' , 19 : 'y' , 20 : 'z'}

num = len(name)

orbitals = []
n_list = []
nl_list = []
config = []

elec = [4*x-2 for x in range(1,22)]

def func(num,list):
    for n in range(num + 1):
        for i in range(0,n):
            list.append(str(n) + name[i])
def n_listm(arr, name):
    for i in range(len(arr)):
        q = arr[i]
        if len(q) == 2:
            n_list.append(int(q[0]))
        if len(q) == 3:
            n_list.append(int(q[0:-1]))
    
    return n_list
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

func(num,orbitals)
n_listm(orbitals,name)
nl_listm(orbitals,name)
supersort(orbitals,n_list,nl_list)

atomic_number = int(input('Atomic Number?'))

n = 0

while atomic_number != 0 :
    orbital = orbitals[n]
    for l in range(0,21):
        if orbital[-1] == name[l]:
            if atomic_number < elec[l]:
                config.append(orbitals[n] + str(atomic_number))
                atomic_number = 0

            else:
                config.append(orbitals[n] + str(elec[l]))
                atomic_number = atomic_number - elec[l]
        
    n = n + 1


str_config = ''
for w in range(len(config)):
    str_config = str_config + config[w] + ' '

print(str_config)

#it works 