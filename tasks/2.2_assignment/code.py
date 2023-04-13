# Name :Muhammad safi(2303.khi.deg.023)
# Assignment partner: Huzaifa Ali (2302.khi.deg.016)

import numpy as np
np_matrix= np.random.randint(10,size=(6,4))
print('before :\n{}'.format(np_matrix))
np_matrix[4:5],np_matrix[5:6]=np_matrix[0:1]+np_matrix[2:3],np_matrix[1:2]+np_matrix[3:4]
print('After :\n{}'.format(np_matrix))
