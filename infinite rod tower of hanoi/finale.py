def th(d,p):
     rods,moves = [str(chr(65+i)) for i in range(p)],[]
     #rod1,rod2 = [i for i in rods],[i for i in rods]
     #rod1[1],rod1[-1],rod2[0],rod2[2] = rod1[-1],rod1[1],rod2[2],rod2[0]
     def tht(n,pegs):
          rod1,rod2 = [i for i in pegs],[i for i in pegs]
          rod1[1],rod1[-1],rod2[0],rod2[2] = rod1[-1],rod1[1],rod2[2],rod2[0]
          if n<1:return
          if n>0 and n<len(pegs)-2:
               order_n = [i for i in range(n-1,0,-1)]+[i for i in range(n)]
               print(order_n)
               from_n = [0 for i in range(n)]+[-i for i in range(n,1,-1)]
               print(from_n)
               to_n = [i for i in range(-2,-n-1,-1)]+[-1 for i in range(n)]
               print(to_n)
               for i in range((n-1)*2+1):
                    moves.append([n-order_n[i],pegs[from_n[i]],pegs[to_n[i]]])
               


          tht(n+2-len(pegs),pegs)
          
          order_n = [i for i in range(n-1,0,-1)]+[i for i in range(n)]
          print(order_n)
          from_n = [0 for i in range(n)]+[-i for i in range(n,1,-1)]
          print(from_n)
          to_n = [i for i in range(-2,-n-1,-1)]+[-1 for i in range(n)]
          print(to_n)
          print(order_n,from_n,to_n,pegs)
          
          for i in range((n-1)*2+1):
               moves.append([n-order_n[i],pegs[from_n[i]],pegs[to_n[i]]])

          tht(n+2-len(pegs),pegs[::-1])
          
     tht(d,rods)
     return moves


while True:
     d = int(input("disk "))
     p = int(input("rod "))
     km = th(d,p)
     print(len(km))
     for i in km:
          print(f"Move disk {i[0]} from source {i[1]} to destination {i[2]}")


