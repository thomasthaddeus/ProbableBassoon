for i in range(3**9):
     for k in range(9):
         if k % 3 == 0:
             print("")
         print(str(i % 3) + " ", end='')
         i //= 3
     print("")
