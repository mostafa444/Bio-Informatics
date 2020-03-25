"""
@author: Mostafa Hisham
"""
import numpy as np
import pandas
Seq2 =np.asarray( pandas.read_excel('xxx.xlsx'))
Seq1 =np.asarray(pandas.read_excel('xx.xlsx'))

def Inzialization (s1 ,s2, gap):
     #intialization array
    array = np.zeros((len (s2)+2,len (s1)+2,), dtype=int)
    #intialization with gab score
    for i in range (len (s1)+1):
        array[1,i+1]=i*gap
    for j in range (len (s2)+1):
        array[j+1,1]=j*gap
    return array
'''
for semplicty i mapped the direction of the pixels by numbers
    diagonal =1
    top =3
    left =5
    diagonal/top =4
    diagonal/left =6
    top/left =8
    diagonal/top/left=9
to calculate the value of the direction we apply the equation of the maximum 
save the values of the dircetions in array array called direction_array
'''    
def Matrix_Filling (s1 ,s2, gap , match , missmatch):
    # Calling of inzialization
    array = Inzialization(s1 , s2 , gap)
    # intialization of the array direction
    direction_counter = 0 
    direction_array=np.zeros((len(s2),len(s1),), dtype=int)
    # main loop
    for l in range (2 ,len(s2)+2):
        for k in range (2,len(s1)+2):
            # check if the the two chracters are matching
            if(s1[k-2]== s2[l-2]):
                if ( max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k-1]+match)) :
                    array[l][k]=(array[l-1][k-1]+match)
                    ##print ("diagonal_MATCH")
                    # set this pixel in trace back array to 1
                    #direction_counter=1
                    direction_counter = direction_counter +1
                if ( max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k]+gap)) : 
                    array[l][k]=(array[l-1][k]+gap)
                    ##print ("top")
                    direction_counter = direction_counter +3
                    # set this pixel in trace back array to 1
                    #direction_counter = 3


                if ( max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l][k-1]+gap)) : 
                    array[l][k]=(array[l][k-1]+gap)
                    direction_counter = direction_counter +5
                    #direction_counter = 5

                   # print ("left")
                    
                    
                #array[l][k]=max( (array[l-1][k-1]+match), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))
            elif(s1[k-2]!= s2[l-2]):
                array[l][k]=max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))
  
                if ( max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k-1]+missmatch)) :
                    array[l][k]=(array[l-1][k-1]+missmatch)
                    direction_counter = direction_counter+1
                    #direction_counter = 1

                    ##print ("diagonal_MISS")
                if ( max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l-1][k]+gap)) : 
                    array[l][k]=(array[l-1][k]+gap)
                    direction_counter = direction_counter+3
                    #direction_counter = 3

                    ##print ("top")
                if ( max( (array[l-1][k-1]+missmatch), (array[l-1][k]+gap) ,  (array[l][k-1]+gap))==(array[l][k-1]+gap)) : 
                    array[l][k]=(array[l][k-1]+gap)
                    #direction_counter = 5
                    direction_counter = direction_counter+5
                    ##print ("left")
            ##print (direction_counter)
            direction_array [l-2][k-2]= direction_counter 
            ##print (l-1)
            ##print (k-1)        
            direction_counter = 0 
            
            

                
    
    return (array , direction_array)



def Trace_back (y1 , s1 , s2):
    a , b =np.shape(y1)
    mat= np.zeros((2 ,b+a ,),dtype=str)
    prop  = np.ones ((a , b,),dtype=int)
    #print (mat)
    counter=1
    l =b-1
    k =a-1
    i =0
    while counter == 1:
        counter =0 
        while l > -1 and k > -1 :
            if (y1[k][l] == 1 ):
                #y1[0 : k  ,  l ]= 0
                #y1[k , 0:l ] =0
                
                mat[0][l] = s1[l][0]
                mat[1][l] = s2[k][0]
                
                k=k-1
                l=l-1
            elif (y1[k][l] == 3 ):
                #y1[k , 0:l ] =0
                
                mat[0][l] = "_"
                mat[1][l] = s2[k][0]
                
                k=k-1
                l=l
        
                counter =0 
            elif (y1[k][l] == 5 ):
                #y1[0 : k  ,  l ]= 0
                
                mat[0][l] = s1[l][0]
                mat[1][l] = "_"            
                
                k=k
                l=l-1
            elif (y1[k][l] == 6 ):
                #y1[0 : k  ,  l ]= 0
                y1[k][l]=1 
                prop [k][l]=10
                
                mat[0][l] = s1[l][0]
                mat[1][l] = "_"  
                k=k
                l=l-1
                counter = 1

            elif (y1[k][l] == 4 ):
                #y1[0 : k  ,  l ]= 0
                y1[k][l]=1 
                prop [k][l]=10
                
                mat[0][l] = "_"
                mat[1][l] = s2[k][0]
                
                k=k-1
                l=l
                counter =1
            elif (y1[k][l] == 8 ):
                #y1[0 : k  ,  l ]= 0
                y1[k][l]=3 
                prop [k][l]=10
                
                mat[0][l] = s1[l][0]
                mat[1][l] = "_"  
                
                k=k
                l=l-1
                
            elif (y1[k][l] == 9 ):
                #y1[0 : k  ,  l ]= 0
                y1[k][l]=4 
                prop [k][l]=10
                
                mat[0][l] = s1[l][0]
                mat[1][l] = "_"  
                
                k=k
                l=l-1
                counter =1 
            else:
                pass
        #if (np.all(prop == 0)):
         #   i=0
        l =b-1
        k =a-1
        #print (prop)
        i=i+1
        print ("Seq  " + str( i ) + "  is equal to:" )
        print (mat)

  

                #y1[0 : k  ,  l : l+1 ]= 0
        #return (y1 ,prop)
        
        #print (counter)
        
        
        
        
        #return array 
        #print (i)

x1,y1 = Matrix_Filling (Seq2 ,Seq1, -3 , 4 , -1 )

print (x1)
print (y1)
Trace_back(y1 ,Seq2 ,Seq1)
'''
print (x1)
print (y1)
'''
'''
z , z1=Trace_back(y1 ,Seq2 ,Seq1)
print (z)
print (z1)
z2 , z1=Trace_back(z ,Seq2 ,Seq1)
print (z)
print (z1)
z3 , z1=Trace_back(z2 ,Seq2 ,Seq1)
print (z3)
print (z1)
z3 , z1=Trace_back(z2 ,Seq2 ,Seq1)
print (z3)
print (z1)
'''


'''
y1[y1==4]=1
y1[y1==6]=5 
y1[y1==8]=5
y1[y1==4]=5
y1[y1==6]=5
'''
'''
y1[y1==6]=1
y1[y1==4]=1
y1[y1==8]=3
y1[y1==4]=1
y1[y1==2]=-1
'''




