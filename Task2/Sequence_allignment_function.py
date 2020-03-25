"""
Created on Tue Mar 24 22:39:29 2020

@author: Mostafa Hisham
"""
import numpy as np
#in case we read the seq 
#this fuction has 3 inputs ( Sequence1 , sequence2 , gap_score)
#this function has 1 output (intialized matrix)
def Inzialization (seq1 ,seq2, gap):
    Intialized_array = np.zeros((len (seq2)+2,len (seq1)+2,), dtype=int)
    #intialization with gab score
    for i in range (len (seq1)+1):
        Intialized_array[1,i+1]=i*gap
    for j in range (len (seq2)+1):
        Intialized_array[j+1,1]=j*gap
    return Intialized_array
'''
for semplicty i mapped the directions of the pixels by numbers
    diagonal =1
    top =3
    left =5
    diagonal/top =4
    diagonal/left =6
    top/left =8
    diagonal/top/left=9
to calculate the value of the direction we apply the equation of the maximum 
save the values of the dircetions in array called direction_array
'''    
#this fuction has 4 inputs ( Sequence1 , sequence2 , gap_score,Match_score,Missmatch_score)
#this function has 2 outputs (filled matrix , directions matrix)
def Matrix_Filling (seq1 ,seq2, gap , match , missmatch):
    # Calling of inzialization
    Filling_array = Inzialization(seq1 , seq2 , gap)
    # intialization of the array direction
    direction_counter = 0 
    direction_array=np.zeros((len(seq2),len(seq1),), dtype=int)
    # Matrix filling
    for l in range (2 ,len(seq2)+2):
        for k in range (2,len(seq1)+2):
            # check if the the two chracters are matching
            if(seq1[k-2]== seq2[l-2]):
                #applying Max equation to deternmine the the max value and the direction  
                if ( max( (Filling_array[l-1][k-1]+match), (Filling_array[l-1][k]+gap) ,  (Filling_array[l][k-1]+gap))==(Filling_array[l-1][k-1]+match)) :
                    Filling_array[l][k]=(Filling_array[l-1][k-1]+match)
                    #if the max value from the diagonal , counter =1
                    direction_counter = direction_counter +1
                if ( max( (Filling_array[l-1][k-1]+match), (Filling_array[l-1][k]+gap) ,  (Filling_array[l][k-1]+gap))==(Filling_array[l-1][k]+gap)) : 
                    Filling_array[l][k]=(Filling_array[l-1][k]+gap)
                    #if the max value from the top , counter =3
                    #if the max value from the top and diagonal , counter = 1+3 =4
                    direction_counter = direction_counter +3
                if ( max( (Filling_array[l-1][k-1]+match), (Filling_array[l-1][k]+gap) ,  (Filling_array[l][k-1]+gap))==(Filling_array[l][k-1]+gap)) : 
                    Filling_array[l][k]=(Filling_array[l][k-1]+gap)
                    #if the max value from the left , counter =5
                    #if the max value from the diagonal and left , counter = 1+5 =6 ..... etc
                    direction_counter = direction_counter +5

            # check if the the two chracters are missmatching  
            elif(seq1[k-2]!= seq2[l-2]):
                Filling_array[l][k]=max( (Filling_array[l-1][k-1]+missmatch), (Filling_array[l-1][k]+gap) ,  (Filling_array[l][k-1]+gap))
  
                if ( max( (Filling_array[l-1][k-1]+missmatch), (Filling_array[l-1][k]+gap) ,  (Filling_array[l][k-1]+gap))==(Filling_array[l-1][k-1]+missmatch)) :
                    Filling_array[l][k]=(Filling_array[l-1][k-1]+missmatch)
                    direction_counter = direction_counter+1
                if ( max( (Filling_array[l-1][k-1]+missmatch), (Filling_array[l-1][k]+gap) ,  (Filling_array[l][k-1]+gap))==(Filling_array[l-1][k]+gap)) : 
                    Filling_array[l][k]=(Filling_array[l-1][k]+gap)
                    direction_counter = direction_counter+3
                if ( max( (Filling_array[l-1][k-1]+missmatch), (Filling_array[l-1][k]+gap) ,  (Filling_array[l][k-1]+gap))==(Filling_array[l][k-1]+gap)) : 
                    Filling_array[l][k]=(Filling_array[l][k-1]+gap)
                    direction_counter = direction_counter+5
            #set the value of the direction at the same index of the pixel in the direction array
            direction_array [l-2][k-2]= direction_counter         
            direction_counter = 0 
    return (Filling_array , direction_array)




'''
To know all the probabilities of  sequences allignment
I started form the last pixel of the (direction array)
if the pixel =1 set the indices k-1 , l-1....and same with  with 3 , 5
if the pixel = 6 which means (diagonal and left) , let k=k l=l-1"move left" and set the value of the direction array =1 so at the iteration will it will be diagonal.
to know that all probabilities done :there is a flag called --- i set it zero at the beggining of each iteration and set it =1 if entered the condition of 6 , 8 ,9 so when the flag still 0 that's mean all probabilities done.



'''
#this function has 3 inputs (Direction_array , seq1 , seq2 , gap , match , missmatch)
#this function has 2 outputs (alligned sequences , score )
def Trace_back (direction_array , seq1 , seq2 , gap , match , missmatch):

    #intialization of the array that contains the two alligned seq's
    Alligned_seq= np.zeros((2 ,len(seq1) ,),dtype=str)
    #intialization of the indices
    l =len(seq1)-1
    k =len(seq2)-1
    #intialization of the number of the alligned seq
    seq_no =0
    #intialization of the prob_flag 
    prob_flag=1
    #intialization of the score var 
    score=0
    #if prob_flag=1 means there is still probablilties 
    while prob_flag == 1:
        #let prob_flag=0 to know if we enter the contion of more that one direction
        prob_flag =0 
        while l > -1 and k > -1 :
            if (direction_array[k][l] == 1 ):
                #if the value =1 one means diagonal so the the value of seq1 is alligend with  value of seq2
                Alligned_seq[0][l] = seq1[l][0]
                Alligned_seq[1][l] = seq2[k][0]
                
                if (seq1[l]== seq2[k]):
                    
                    score = score+ match
                else :
                    score = score +missmatch

                #move the indicies into the diagonal direction
                k=k-1
                l=l-1
            elif (direction_array[k][l] == 3 ):
                #if the value =3 one means there is a gap 
                Alligned_seq[0][l] = "_"
                Alligned_seq[1][l] = seq2[k][0]
                
                score = score + gap 

                k=k-1
                l=l
        
            elif (direction_array[k][l] == 5 ):
                #if the value =3 one means there is a gap 
                Alligned_seq[0][l] = seq1[l][0]
                Alligned_seq[1][l] = "_" 
                
                score = score + gap 

                k=k
                l=l-1
            elif (direction_array[k][l] == 6 ):
                #if the value =6 one means there are 2 direction left and diagonal 
                #set the value of the direction_array=1 
                direction_array[k][l]=1 
                #move the indices into the left
                Alligned_seq[0][l] = seq1[l][0]
                Alligned_seq[1][l] = "_"  
                
                score = score + gap 
                
                k=k
                l=l-1
                #set the value of the prob_flag = 1 which means there is one more probability so one more iteration is nedded
                prob_flag = 1

            elif (direction_array[k][l] == 4 ):
                #if the value =4 one means there are 2 direction top and diagonal 
                #set the value of the direction_array=1 
                direction_array[k][l]=1 
                #move the indices into the top
                Alligned_seq[0][l] = "_"
                Alligned_seq[1][l] = seq2[k][0]
                score = score + gap 

                k=k-1
                l=l
                #set the value of the prob_flag = 1 which means there is one more probability so one more iteration is nedded
                prob_flag =1
            elif (direction_array[k][l] == 8 ):
                direction_array[k][l]=3 
                Alligned_seq[0][l] = seq1[l][0]
                Alligned_seq[1][l] = "_"
                score = score + gap 

                k=k
                l=l-1
                prob_flag =1

            elif (direction_array[k][l] == 9 ):
                direction_array[k][l]=4 
                Alligned_seq[0][l] = seq1[l][0]
                Alligned_seq[1][l] = "_"  
                score = score + gap 

                k=k
                l=l-1
                prob_flag =1
            else:
                pass
        #set the value of indices at the last pixel 
        l =len(seq1)-1
        k =len(seq2)-1
        seq_no=seq_no+1
        print ("The score of seq " + str( seq_no ) + " = " + str( score))
        print ("Seq  " + str( seq_no ) + "  is equal to:" )        
        print (Alligned_seq)
        score =0
'''
#Final Function
'''      
        
#this function has 5 inputs 
#this function print Filled_matrix and alligned sequences
def seq_allignment(First_seq ,Second_seq, Gab_score , Match_score , MissMatch_score):
    if (len(First_seq)<len(Second_seq)):
        x= First_seq
        First_seq=Second_seq
        Second_seq=x
    matrix_fill,direction_array = Matrix_Filling (First_seq ,Second_seq, Gab_score , Match_score , MissMatch_score )  
    print ("THe filled Matrix")
    print (matrix_fill)
    print ("Direction Matrix")
    print ("Note that the mapping of the directions ")
    print ("1 --> Diagonal")
    print ("3 --> Top")
    print ("5 --> Left")
    print ("4 --> Diagonal , Top")
    print ("6 --> Diagonal , Left")
    print ("8 --> Top , Left ")
    print ("9 --> Diagonal,Top , Left  ")
    print (direction_array)
    print ("Alligned_sequences")
    Trace_back(direction_array ,First_seq ,Second_seq , Gab_score , Match_score , MissMatch_score )
    


