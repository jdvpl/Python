# 1*conejo + 1*gallina = 50 (total_animales)
# 4*conejo + 2*gallina = 140 (total_patas)


import numpy as np
a =  np.array([[1,1],[4,2]])
r = np.array([50,140])
solucion = np.linalg.solve(a,r)
print(solucion)
