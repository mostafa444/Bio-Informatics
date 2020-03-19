"""
@author: Mostafa Hisham
"""
import numpy as np
import pandas

Seq2 =np.asarray( pandas.read_excel('xx.xlsx'))
Seq1 =np.asarray(pandas.read_excel('xxx.xlsx'))

def dynamic (s1 ,s2, gap , match , missmatch):
    #intialization array
    array = np.zeros((len (s2)+2,len (s1)+2,), dtype=int)
    #intialization with gab score
    for i in range (len (s1)+1):
        array[1,i+1]=i*gap
    for j in range (len (s2)+1):
        array[j+1,1]=j*gap
    #trace back intialization
    trace_back_counter = 0 
    trace_back_array=np.zeros((len(s2),len(s1),), dtype=int)
    # main loop
    for l in range (2 ,len(s2)+2):
        for k in range (2,len(s1)+2):
            # check if the the two chracters are matching
            if(s1[k-2]== s2[l-2]):
                if ( max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k-1]+match)) :
                    array[l][k]=(array[l-1][k-1]+match)
                    print ("diagonal_MATCH")
                    # set this pixel in trace back array to 1
                    trace_back_counter = trace_back_counter +1
                if ( max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k]+gap)) : 
                    array[l][k]=(array[l-1][k]+gap)
                    print ("top")
                    #trace_back_counter = trace_back_counter +3
                    # set this pixel in trace back array to 1
                    trace_back_counter = 3


                if ( max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l][k-1]+gap)) : 
                    array[l][k]=(array[l][k-1]+gap)
                    trace_back_counter = trace_back_counter +5
                    trace_back_counter = 5

                    print ("left")
                    
                    
                #array[l][k]=max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))
            elif(s1[k-2]!= s2[l-2]):
                array[l][k]=max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))
  
                if ( max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k-1]+missmatch)) :
                    array[l][k]=(array[l-1][k-1]+missmatch)
                    #trace_back_counter = trace_back_counter-1
                    trace_back_counter = 7

                    print ("diagonal_MISS")
                if ( max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k]+gap)) : 
                    array[l][k]=(array[l-1][k]+gap)
                    #trace_back_counter = trace_back_counter+3
                    trace_back_counter = 3

                    print ("top")
                if ( max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l][k-1]+gap)) : 
                    array[l][k]=(array[l][k-1]+gap)
                    trace_back_counter = 5
                    #trace_back_counter = trace_back_counter+5
                    print ("left")
            print (trace_back_counter)
            trace_back_array [l-2][k-2]= trace_back_counter 
            print (l-1)
            print (k-1)        
            trace_back_counter = 0 
            
            

                
    
    return (array , trace_back_array)
        



    #return array 

x1,y1 = dynamic (Seq2 ,Seq1, -3 , 4 , -1 )
print (x1)
print (y1)


counter=0



for k in reversed ( range (len(Seq1))):
    for l in reversed (range (len(Seq2))):
        if (y1[k][l] == 1 ):
            y1[k][l] =10
            y1[0 : k  ,  l ]= 0
            y1[k , 0:l ] =0
            k=k-1
            l=l-1 
            counter = counter +4
        elif (y1[k][l] == 3 ):
            y1[k , 0:l ] =0
            y1[k][l] =20
            k=k-1
            l=l
            counter = counter -3
        elif (y1[k][l] == 5 ):
            y1[0 : k  ,  l ]= 0
            y1[k][l] =30
            k=k
            l=l-1
            counter = counter -3

        else:
            pass
        #elif 
            #y1[0 : k  ,  l : l+1 ]= 0
print (y1)
print (counter)



