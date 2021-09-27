'''
Η NumPy(Numeric Python) Βιβλιοθήκη μας δίνει την δυνατότητα να χειριστούμε
υψηλών διαστάσεων λίστες και πίνακες. 
'''

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    numpy_array = numpy.array([],float)
    for i in range(len(arr)-1, -1, -1):
        numpy_array = numpy.append(numpy_array, float(arr[i]))
        
    return numpy_array
        

arr = input().strip().split(' ')
result = arrays(arr)
print(result)