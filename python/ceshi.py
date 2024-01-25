import numpy as np
teacher = np.dtype([('name','S20'), ('age', 'i1'), ('salary', 'f4')])
#输出结构化数据teacher
print(teacher)
#将其应用于ndarray对象
b = np.array([('ycs', 32, 6357.50),('jxe', 28, 6856.80)], dtype = teacher)
print(b)