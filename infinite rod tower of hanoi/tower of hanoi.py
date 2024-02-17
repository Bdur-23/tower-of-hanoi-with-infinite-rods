
def th3(n , from_rod, to_rod, aux1):
    if n==1:
        print("Move disk 1 from source",from_rod,"to destination",to_rod)
        return
    th3(n-1, from_rod, aux1, to_rod)
    count.append(2)
    print("Move disk",n,"from source",from_rod,"to destination",to_rod)
    th3(n-1, aux1, to_rod, from_rod)

'''
while True:
    count = []
    n = int(input("enter a disk number: "))
    th3(n,'A','C','B')
    print(sum(count)+1)
'''




def th4(n, from_rod, to_rod, aux1, aux2):
    if (n == 0):
        return
    if (n == 1):       
        print("Move disk", n, "from rod",from_rod, " to rod", to_rod)
        return

    th4(n-2, from_rod, aux1, aux2, to_rod)
    count.append(3)
    print("Move disk", n-1, "from rod", from_rod," to rod", aux2)

    print("Move disk", n, "from rod", from_rod," to rod", to_rod)

    print("Move disk", n-1, "from rod", aux2," to rod", to_rod)

    th4(n-2, aux1, to_rod, from_rod, aux2)

"""
while True:
    count = []
    n = int(input("enter a disk number: "))
    th4(n, "A", "D", "B", "C")
    print(sum(count) if n%2==0 else sum(count) + 2**(n//2))
"""





def th5(n, from_rod, to_rod, aux1, aux2, aux3):
    if n < 1:
        return
    if n == 1:       
        print("Move disk", n, "from rod",from_rod, " to rod", to_rod)
        count.append([n,from_rod,to_rod])
        return
    
    if n == 2:
        print("Move disk", n-1, "from rod",from_rod, " to rod", aux3)
        count.append([n-1,from_rod,aux3])
        
        print("Move disk", n, "from rod",from_rod, " to rod", to_rod)
        count.append([n,from_rod,to_rod])
        
        print("Move disk", n-1, "from rod",aux3, " to rod", to_rod)
        count.append([n-1,aux3,to_rod])
        
        return

    th5(n-3, from_rod, aux1, aux2, aux3, to_rod)
    print("Move disk", n-2, "from rod", from_rod," to rod", aux3)
    count.append([n-2,from_rod,aux3])

    print("Move disk", n-1, "from rod", from_rod," to rod", aux2)
    count.append([n-1,from_rod,aux2])

    print("Move disk", n, "from rod", from_rod," to rod", to_rod)
    count.append([n,from_rod,to_rod])

    print("Move disk", n-1, "from rod", aux2," to rod", to_rod)
    count.append([n-1,aux2,to_rod])

    print("Move disk", n-2, "from rod", aux3," to rod", to_rod)
    count.append([n-2,aux3,to_rod])

    th5(n-3, aux1, to_rod, from_rod, aux2, aux3)


'''
while True:
    count = []
    n = int(input("enter a disk number: "))
    th5(n, "A", "E", "B", "C", "D")
    print(len(count))
'''





def th6(n, from_rod, to_rod, aux1, aux2, aux3, aux4):
    if n < 1:
        return
    if n == 1:       
        print("Move disk", n, "from rod",from_rod, " to rod", to_rod)
        count.append([n,from_rod,to_rod])
        return

    
    if n == 2:
        print("Move disk", n-1, "from rod",from_rod, " to rod", aux3)
        count.append([n-1,from_rod,aux3])
        
        print("Move disk", n, "from rod",from_rod, " to rod", to_rod)
        count.append([n,from_rod,to_rod])
        
        print("Move disk", n-1, "from rod",aux3, " to rod", to_rod)
        count.append([n-1,aux3,to_rod])
        
        return


    if n == 3:
        print("Move disk", n-2, "from rod", from_rod," to rod", aux4)
        count.append([n-2,from_rod,aux4])

        print("Move disk", n-1, "from rod", from_rod," to rod", aux3)
        count.append([n-1,from_rod,aux3])

        print("Move disk", n, "from rod", from_rod," to rod", to_rod)
        count.append([n,from_rod,to_rod])

        print("Move disk", n-1, "from rod", aux3," to rod", to_rod)
        count.append([n-1,aux3,to_rod])

        print("Move disk", n-2, "from rod", aux4," to rod", to_rod)
        count.append([n-2,aux4,to_rod])
        
        return


    th6(n-4, from_rod, aux1, aux2, aux3, aux4, to_rod)
    print("Move disk", n-3, "from rod", from_rod," to rod", aux4)
    count.append([n-3,from_rod,aux4])
    
    print("Move disk", n-2, "from rod", from_rod," to rod", aux3)
    count.append([n-2,from_rod,aux3])

    print("Move disk", n-1, "from rod", from_rod," to rod", aux2)
    count.append([n-1,from_rod,aux2])

    print("Move disk", n, "from rod", from_rod," to rod", to_rod)
    count.append([n,from_rod,to_rod])

    print("Move disk", n-1, "from rod", aux2," to rod", to_rod)
    count.append([n-1,aux2,to_rod])

    print("Move disk", n-2, "from rod", aux3," to rod", to_rod)
    count.append([n-2,aux3,to_rod])

    print("Move disk", n-3, "from rod", aux4," to rod", to_rod)
    count.append([n-3,aux4,to_rod])

    th6(n-4, aux1, to_rod, from_rod, aux2, aux3, aux4)



while True:
    count = []
    n = int(input("enter a disk number: "))
    th6(n, "A", "F", "B", "C", "D", 'E')
    print(len(count))
