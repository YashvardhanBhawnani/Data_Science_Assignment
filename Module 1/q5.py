# Question 5 -> Saving Output R/Python
a = 10
b = 20

f = open("D:/coding/Python/Data_Science_Assignement/Module 1/q5.txt","w")
c = a+b

# Writing Into Text File
f.write(f"The Result of add operation of {a} and {b} is {c}.")

f = open("D:/coding/Python/Data_Science_Assignement/Module1/q5.txt","r")
print(f.readline())
f.close();