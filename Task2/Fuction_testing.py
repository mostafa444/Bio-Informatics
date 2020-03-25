# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:28:46 2020

@author: Mostafa Hisham
"""

import pandas
import numpy as np
import Seq_allignment as SA

#in case of uploading seq from excel sheets
seq11 =np.asarray( pandas.read_excel('Seq1.xlsx'))
seq12 =np.asarray(pandas.read_excel('Seq2.xlsx'))


#Seq for trying
seq21= "CTATTGACGTAACAT"
seq22= "CTATTGAACAT"

#another Seq
seq31="GAATTCAGTTA"
seq32="GGATCGA"

gab=-3
match=4
missmatch=-1

SA.seq_allignment(seq11,seq12, gab,match,missmatch)

