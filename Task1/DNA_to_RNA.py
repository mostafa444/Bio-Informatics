# -*- coding: utf-8 -*-
"""
@author: Mostafa Hisham
"""

import numpy as np


def Convert_DNA_To_RNA (DNA_seq):
    DNA_Sequence= np.asarray (DNA_seq)
    DNA_Sequence[DNA_Sequence=="T"]="U"
    return (DNA_Sequence)
