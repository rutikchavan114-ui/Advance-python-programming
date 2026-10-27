import numpy as np

a=np.arange(1,11)
print("Array:",a)
print("Slice:",a[0:5])
print("Skip:",a[::2])

print("Sum:",a.sum())
print("Mean:",a.mean())
print("Min:",a.min())
print("Max:",a.max())

print("Add 10:",a+10)
