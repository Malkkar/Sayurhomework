#input hello world
#we can get a output  olleh dlrow
str=input("enter the string")
#str=str.split(" ")
for i in str:
	if i!=" ":
		for j in range(len(str)-1,-1,-1):
			print(i,end=" ")
		print(end=" ")
	if i==" ":
		print(" ")