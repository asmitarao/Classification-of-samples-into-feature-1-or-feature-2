a = 0.2 # a= alpha
x= [ [0.5,1.5] , [1, 1.5] , [1, 2], [1.5, 2] , [1.5, 2.5], [2,2.5], [3, 1], [3.5,1], [3.5,2] , [4,2], [4.5,2] ]
target=[0,0,0,0,0,0,1,1,1,1,1] #observed values
weight = [0,0]
def dot(x=[],y=[]): # each element of the list is being multiplied
  result = 0
  for i in range(2):
     result += x[i] * y[i]
  return result
number =1 #the loop variable ie how many times it should run
err =0 #error
while(number):
  number = 0
  for i in range(11):
	 result = dot(weight,x[i])
	 if(result <= 0):
		expected = 0
	 else:
		expected = 1
	 err = expected - target[i]
	 #print(err)
	 for k in range(2):
		weight[k] = weight[k] + a * err * x[i][k]
	 if(err == 1):
		number = 1
print(weight)
f1 = int(input(" Enter feature 1 = "))
f2 = int(input("Enter feature 2 = "))
z = weight[0]*f1 + weight[1] *f2
if (z>0):
   print("It belongs to class 1")
else:
   print("It belongs to class 0")
