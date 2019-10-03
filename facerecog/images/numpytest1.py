import numpy as np

a = np.zeros((2,2))   # آرایه دو دویی با مقدار پیش فرض صفر
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # آرایه با مقادیر پیش فرض یک
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # آرایه با مقدار پیش فرض ۷
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # ماتریس یکانی
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # یک ماترین با مقادیر تصادفی
print(e)

