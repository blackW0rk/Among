import numpy as np

def active(z):
	if z >= 0.7:
		return 1
	else:
		return 0

print("1 - Yes, 0 - No")

v1 = int(input("Are there any suspicions about the first player?: "))
v2 = int(input("Do others have any suspicions of him?: "))
v3 = int(input("Stopped suspiciously?: "))
v4 = int(input("Didn't fill the task bar?: "))

n = np.array([[v1, v2, v3, v4]])

w = np.array([[0.3],
			  [0.3],
			  [0.2],
			  [0.2]])

output = active(np.dot(n, w))

print("Result is: " + str(output))
input("Thank you! ")