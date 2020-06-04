from mpi4py import MPI

import random
import time

resultPar = 0

def how_many_max_values_sequential(ar):

    #find max value of the list

    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]

    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1

    return contValue

 

# Complete the how_many_max_values_parallel function below.

#def how_many_max_values_parallel(ar):
    
    #implement your solution'
    
 

if __name__ == '__main__':
    


    ar_count = 40000000

    #Generate ar_count random numbers between 1 and 30
    ar = [random.randrange(1,30) for i in range(ar_count)]
    

    inicioSec = time.time()
    resultSec = how_many_max_values_sequential(ar)
    finSec =  time.time()

    
    

    inicioPar = time.time()  
    
    comm = MPI.COMM_WORLD
    numtasks = comm.size
    rank = comm.Get_rank()
    print(rank)

    numworkers = numtasks-1
    
    if(rank == 0):
        averow = len(ar)//numworkers
        extra = len(ar)%numworkers
        offset = 0
        mtype = 1
        
        for dest in range(numworkers):
            if(dest+1 <= extra):
                rows = averow+1
            else:
                rows = averow
            print("sending %d rows to task %d" %(rows,dest+1));
            comm.send(offset,dest=dest+1,tag=mtype)
            comm.send(rows,dest=dest+1,tag=mtype)
            comm.send(ar[offset:rows+offset],dest=dest+1,tag=mtype)
            #print(a[offset:rows+offset])
            offset = offset + rows
            
        resultPar = 0
        mtype = 2
        for i in range(numworkers):
            source = i
            offset = comm.recv(source=source+1,tag=mtype)
            rows = comm.recv(source=source+1,tag=mtype)
            z = comm.recv(source=source+1,tag=mtype)
            resultPar = resultPar+z
            
    if(rank > 0):
        mtype = 1
        offset = comm.recv(source=0,tag=mtype)
        rows = comm.recv(source=0,tag=mtype)
        ar = comm.recv(source=0,tag=mtype)
        
        maxValue = 0
        for i in range(len(ar)):
            if i == 0:
                maxValue = ar[i]
            else:
                if ar[i] > maxValue:
                    maxValue = ar[i]

        #find how many max values are in the list
        contValue = 0
        for i in range(len(ar)):
            if ar[i] == maxValue:
                contValue += 1
                
        mtype = 2
        comm.send(offset,dest=0,tag=mtype)
        comm.send(rows,dest=0,tag=mtype)
        comm.send(contValue,dest=0,tag=mtype)

    
    
    finPar = time.time()
    

   

    print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))
