# -*- coding: utf-8 -*-
"""
@author: Mostafa Hisham
"""
import numpy as np
DNA_Sequence = ["A","C","A","G","T","C","G","A","C","T","A","G","C","T","T","G","C","A","C","G","T","A","C"]
DNA_Sequence= np.asarray (DNA_Sequence)


def cg_content (seq):
    seq= np.asarray (seq)
    C_number = number_of_elements_in_seq("C" ,DNA_Sequence )
    G_number = number_of_elements_in_seq("G" ,DNA_Sequence )
    total_cg_number= C_number+G_number
    cg_cont= (total_cg_number/ len (seq))
    return (cg_cont)



def number_of_elements_in_seq (element , seq):
    counter=0
    for i in range (len(seq)):
        if (seq [i]== element ):
            counter = counter+1       
    return (counter)




#print( "The cg_content in the seq is = " +str (cg_content(DNA_Sequence)))
        