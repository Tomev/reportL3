import numpy as np


vals = [133 ,  130 ,104 , 120 , 123 , 133 , 130 , 161 , 133 , 126 , 130 , 130 , 140 , 146 , 141 , 126 , 130 , 141 , 95 , 141]

print(np.round(np.average(vals), decimals= 1))
print(np.round(np.std(vals), decimals=1))
