import datetime
import time
import sympy as sym

primelist = []
print('\n')
print("Namastey! This is a Prime Number Generator Engine.\n")
try:
    L = int(input("Enter the Starting point: "))
    U = int(input("Enter the Ending point: "))
    
    #---> If User enters number in reverse order
    if L>U:
        temp = L
        L=U
        U=temp
    else:
        L=L
        U=U
    print("\n")
    algo1 = 1
    algo2 = 2
    algo3 = 3
    print ('''Algo1: Generates lower range Prime numbers\nAlgo2: Generates middle range Prime numbers\nAlgo3: Generates higher range Prime numbers''')
    print("\n")
    print("Select algorithms for generating prime numbers within the selected range.\nfor algo1 type '1'\nfor algo 2 type '2'\nfor algo 3 type '3' " )
    print("\n")
    sel_algo = int(input("Select algorithms: "))
    
    #----> ALGORITHM 01---------------------------------------------------------------------------------------------------------------------
    ti1 = time.time()                           #---> Initializing run time for algo 1
    if sel_algo==1:
        for i in range(L,U+1):                  #---> Selecting the range to generate prime numbers within range
            if i>1:                             #---> Checking conditions for prime numbers
                for j in range (2,i):           #--->Iterating through all the numbers to check divisors
                    if(i%j==0):
                        break
                else:
                    primelist.append(i)
        print(f"Prime Numbers between {L} & {U} are\n{primelist}")
    tf1 = time.time()                           #---> Ending run time
    
    #----> ALGORITHM 02---------------------------------------------------------------------------------------------------------------------
    ti2 = time.time()                           #---> Initializing run time for algo 2
    if sel_algo==2:
        for i in range(L,U):
            if i>1:                                  
                for j in range (2,int(i**(1/2))+1):   #---> Minimising the number of iterations by taking square of each value of i 
                    if(i%j==0):
                        break
                else:
                    primelist.append(i)
        print(f"Prime Numbers between {L} & {U} are\n{primelist}")
    tf2 = time.time()                           #--->Ending run time
    
    #----> ALGORITHM 03---------------------------------------------------------------------------------------------------------------------
    ti3 = time.time()                           #---> Initializing run time for algo 3
    if sel_algo==3:
       eratos = ([i for i in sym.sieve.primerange(L,U)]) #---> 
       primelist.append(eratos)
       print(f"Prime Numbers between {L} & {U} are\n{primelist}")
    tf3=time.time()                             #---> Ending run time
#-------------------------------------------------------------------------------------------------------------------------------------------
# Checking conditions for the choosen algorithm --->
    if sel_algo==1:
        print("Algorithm: Lower Range Algorithm was Choosen")
        print("Time elapsed: ", (tf1-ti1))
    if sel_algo ==2:
        print("Algorithm: Mid Range Algorithm was Choosen")
        print("Time elapsed: ", (tf2-ti2))
    if sel_algo ==3:
        print("Algorithm: Sieve Range Algorithm was Choosen")
        print("Time elapsed: ", (tf3-ti3))
    if (sel_algo<1) or (sel_algo>3):
        print("The algorithm isn't available. Try selecting algos in between 1,2 and 3")
    
    datet = datetime.datetime.now() #Time stamp to record the user's time and date of use of the algorithm
    print("Timestamp: ",datet)

except:
    print("Oops! You may have entered something wrong. Please Check and try again!")
    
finally:
    print("Close all the resources")