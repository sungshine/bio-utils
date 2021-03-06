#!/usr/bin/env python

""" Test the functionality of Python's default-timer.

"""


import os
import subprocess
from timeit import default_timer


__author__ = 'Sung Im'
__email__ = 'wla9@cdc.gov'


# Testing the default timer library in Python 3.4.
start = default_timer()
inputDirectory = '/home/sim/Projects/ANI/tmp/'

aniPath = '/home/sim/Setup/enveomics-master/Scripts/ani.rb'
paths = [os.path.join(inputDirectory, fn) for fn in next(os.walk(inputDirectory))[2]]

# initialize 2D array.
aniMatrix = [[[] for i in range(len(paths))] for j in range(len(paths))]

for i in range(len(paths)):
    aniMatrix[i][i] = 100
    for j in range(i+1, len(paths)):
        aniCall = subprocess.check_output([aniPath,
                                           '-q',
                                           '-1',
                                           paths[i],
                                           '-2',
                                           paths[j],
                                           '-t 64'
                                           ]
                                          )
        aniScores = aniCall.rstrip().split()
        aniMatrix[i][j] = aniScores[24]
        aniMatrix[j][i] = aniScores[24]

print('The ANI calculations took: ' + `default_timer() - start`)
print(aniMatrix)