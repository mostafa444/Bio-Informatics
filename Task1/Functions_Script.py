# -*- codin/g: utf-8 -*-
"""
Created on Sat Mar  7 02:45:37 2020

@author: Mostafa Hisham

"""
import numpy as np


def Convert_DNA_To_RNA (DNA):
    DNA_Sequence= np.asarray (DNA)
    DNA_Sequence[DNA_Sequence=="T"]="U"
    print ("The RNA Sequence = " + str (DNA_Sequence))
    return (DNA_Sequence)
    


def Number_Of_Amino_Acid_In_RNA (RNA):
    length= (len (RNA))
    number_Of_Amino_Acid = int (length/3)
    remain = (np.mod (length,3))
    return number_Of_Amino_Acid , remain
    

    
