from fake_math import divide as dv_fake
from true_math import divide as dv_true


result1 = dv_fake(4,2)
result2 = dv_fake(4,0)
result3 = dv_true(88,2)
result4 = dv_true(88,0)
print(result1)
print(result2)
print(result3)
print(result4)