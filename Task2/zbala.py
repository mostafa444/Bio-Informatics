# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 03:41:26 2020

@author: Mostafa Hisham
"""
def Kernal (seq1 , seq2,gap_score):
    print(seq1)
    print (Seq2)
    array = np.zeros((len (Seq1)+1,len (Seq2)+1,), dtype=int)
    x = np.zeros(((len (Seq1)+1),1), dtype=int)
    y = np.zeros(((len (Seq2)+1),1), dtype=int)  
    for i in range (len (Seq1)+1):
        x[i]=i*gap_score
    for i in range (len (Seq2)+1):
        y[i]=i*gap_score
    array[(1):(len (Seq1)+1) ,0:1]= x[1:len (Seq1)+1]
    array[0:1,(1):(len (Seq2)+1) ]= np.transpose (y[1:len (Seq1)+1])
    return (array)

    for i in range (1,len(seq1)+1):
        for j in range (1,len(seq2)+1):
            if(Seq1[i-1]== Seq2[j-1]):
                array[i][j]=max( (array[i-1][j-1]+1), (array[i-1][j]-1) ,  (array[i][j-1]-1))    
            elif (Seq1[i-1] != Seq2[j-1]):
                array[i][j]=max( (array[i-1][j-1]-1), (array[i-1][j]-1) ,  (array[i][j-1]-1))                 
    return (array)



