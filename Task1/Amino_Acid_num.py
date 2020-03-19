# -*- coding: utf-8 -*-
"""

@author: Mostafa Hisham
"""

import numpy as np     


def Number_Of_Amino_Acid_In_RNA (RNA):
    length= (len (RNA))
    number_Of_Amino_Acid = int (length/3)
    remain = (np.mod (length,3))
    return number_Of_Amino_Acid , remain
