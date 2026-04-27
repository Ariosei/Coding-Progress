elec = [4*x-2 for x in range(1,5)]

name = {0: 's' , 1 : 'p' , 2 : 'd' , 3 : 'f'}   

afbau = ['1s' , '2s' , '2p' , '3s' , '3p' , '4s' , '3d' , '4p' , '5s' , '4d' , '5p' , '6s' , '4f' , '5d' , '6p']

atomic_number = int(input('Atomic Number?'))

config = []
n = 0

while atomic_number != 0 :
    orbital = afbau[n]
    for l in range(0,4):
        if orbital[-1] == name[l]:
            if atomic_number < elec[l]:
                config.append(afbau[n] + str(atomic_number))
                atomic_number = 0

            else:
                config.append(afbau[n] + str(elec[l]))
                atomic_number = atomic_number - elec[l]
        
    n = n + 1
        
print(config)

    

    
    
    
    
    

