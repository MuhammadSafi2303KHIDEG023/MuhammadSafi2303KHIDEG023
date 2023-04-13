"""
Name :Muhammad safi(2303.khi.deg.023)
Assignment partner: Huzaifa Ali (2302.khi.deg.016)

"""

import numpy as np
np_matrix= np.random.randint(10,size=(6,4)) #initializes a 6x4 matrix with random int
print('before :\n{}'.format(np_matrix))
np_matrix[4:5],np_matrix[5:6]=np_matrix[0:1]+np_matrix[2:3],np_matrix[1:2]+np_matrix[3:4] #adding 1st and 3rd row and assigning to 5th row , adding 2nd and 4th row and assigning to 6th row.
print('After :\n{}'.format(np_matrix))
