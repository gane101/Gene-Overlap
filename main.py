import numpy as np
from scipy import signal
import math

value_map = {
	0 : [1,0,0,0],
	1 : [0,1,0,0],
	2 : [0,0,1,0],
	3 : [0,0,0,1]
}

func = np.vectorize(lambda x:math.floor(x*4))

c = func(np.random.rand(10))
d = func(np.random.rand(10))
print(c)
print(d)


res_1 = []
res_2 = []

for v in c:
	res_1 += value_map[v]
for v in d:
	res_2 += value_map[v]

print(res_1)
print(res_2)



# res = signal.convolve(c,d)
# print(res)
# for i in range(1,len(res)):
	# res[-i] -= res[-i-1]
# print(res)



