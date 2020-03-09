# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:58:40 2020

@author: Mostafa Hisham
"""
import numpy as np
import Functions_Script as FS
import pandas

excel_data_df  = pandas.read_excel('xx.xlsx')
excel_data_df=np.asarray(excel_data_df)
print (excel_data_df) 
#DNA_Sequence = ["a","b","s","v","f","d","e","s","a","w","r","r","l"]
RNA_Sequence=FS.Convert_DNA_To_RNA(excel_data_df)
Number , Remain =FS.Number_Of_Amino_Acid_In_RNA(RNA_Sequence)
print ("The Number Of Amino Acids in the RNA Sequence =  " + str( Number) )
print ("The Remain =" + str (Remain)) 
