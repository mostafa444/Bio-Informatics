# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:58:40 2020

@author: Mostafa Hisham
"""
import numpy as np
import cg_content as cg
import DNA_to_RNA as DR
import Amino_Acid_num as An

#import DNA from excel sheet 
 
#import pandas
#DNA_Sequence  = pandas.read_excel('DNA_seq.xlsx')


DNA_Sequence = ["A","C","A","G","T","C","G","A","C","T","A","G","C","T","T","G","C","A","C","G","T","A","C"]

#Test  cg_content function
cg_content= cg.cg_content(DNA_Sequence)
print( "The cg_content in the seq is = " +str (cg_content))



#Test  DNA_to_RNA function
RNA_Sequence=DR.Convert_DNA_To_RNA(DNA_Sequence)
print ("The RNA Sequence = " + str (RNA_Sequence))


#Test  Amino_Acid_num function
Number , Remain =An.Number_Of_Amino_Acid_In_RNA(RNA_Sequence)
print ("The Number Of Amino Acids in the RNA Sequence =  " + str( Number) )
print ("The Remain =" + str (Remain)) 
