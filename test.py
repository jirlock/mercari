import numpy as numpy
import pandas as pd
from time import time


print('loading')
start_time = time()
train = pd.read_table('data/train.tsv')
end_time = time()
print('loading done ' + str(end_time-start_time))

print(type(train))
print(type(train.columns))
