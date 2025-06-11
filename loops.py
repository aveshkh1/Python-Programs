# Programs using while loops
# i=100
# while i>=1:
#     print(i)
#     i-=1
#multplication table
# n=int(input("Enter the number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
#print the first 20 even numbers
# i=1
# while i<=20:
#     if i % 2==0:
#         print(i)
#     i+=1
#print sum of n natural numbers
# n=int(input("Enter the number"))
# i=0
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)
#factorial of number
# n=int(input("Enter the number:"))
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

#Printing the number in digits in an integer
# num=int(input("Enter the number:"))
# count=0
# if num==0:
#     count==1
# else:
#     while num>0:
#         num=num//10
#         count+=1
# print(count)
#Printing the digits in reverse order
# n=int(input("Enter the digit:"))
# while n>0:
#     digit=n%10
#     print(digit,end="")
#     n=n//10
# password=1234
# i=1
# while i<=3:
#     Enterpassword = int(input("Enter the correct password="))
#     if Enterpassword==password:
#         print("Password is correct")
#         break
#     else:
#         print("Incorrect Password")
#     i+=1
# if i>3:
#     print("Too many attempts your account is locked")
#searching the element from the tuple
# list=[1,2,3,9,10,55,77,88,21,4,66]
# idx=0
# x=77
# while idx<len(list):
#     if (list[idx]==x):
#         print("The number found at idx",idx)
#         break
#     else:
#         print("The number is not found in the idx",idx)
#
#     idx+=1

#sort only even numbers from the list
# idx=0
# sorted_list=[]
# while idx<len(list):
#     if (list[idx] % 2!=0):
#         sorted_list.append(list[idx])
#     idx+=1
# print(sorted_list)
# i=0
# while i<=100:
#     i += 1
#     if i % 2==0:
#         continue
#     print(i)
#
#
# using the range fuction
# for i in range(100,0,-1):
#     print(i)
# n=int(input("Enter the number:"))
# for i in range(11):
#     print(i*n)
#print sum of n natural numbers using for loop
# sum=0
# for i in range(6):
#     sum+=i
# print(sum)
#Add all the  values from the given list
list=[1,55,67,44,77,66,77]
sum=0
for el in list:
    sum+=el
print(sum)
#Add all the values from the given list using while loop
# i=0
# sum1=0
# while i<len(list):
#     sum1+=list[i]
#     i+=1
# print(sum1)
# n=int(input("Enter the nubmer:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
n=int(input("Enter the number:"))
if n<2:
    print("It's not prime number")
for i in range(2,int(n**0.5)+1):

    if n % i==0:
        print("It's not prime number")
        break
else:
    print("It's prime number")


