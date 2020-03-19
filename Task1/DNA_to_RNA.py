<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
@author: Mostafa Hisham
"""

import numpy as np


def Convert_DNA_To_RNA (DNA_seq):
    DNA_Sequence= np.asarray (DNA_seq)
    DNA_Sequence[DNA_Sequence=="T"]="U"
    return (DNA_Sequence)
=======
# -*- coding: utf-8 -*-
"""
@author: Mostafa Hisham
"""

import numpy as np


def Convert_DNA_To_RNA (DNA_seq):
    DNA_Sequence= np.asarray (DNA_seq)
    DNA_Sequence[DNA_Sequence=="T"]="U"
    return (DNA_Sequence)
>>>>>>> e5fea93de0b0bac0d198a68b34f40c3480fedd50
