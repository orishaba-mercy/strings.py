# !!!1!!Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def continue_if():
    x =1
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)
        x+=1

# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_numbers(num):
  
    if num>2:
     numbers=range(2,num)
    for i in numbers:
      if num%i==0:
        print(f"{num} is not prime number")
        break
    else:
        print(f" {num} is prime")


    
# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def even_numbers():
   
    sum =0
    for i in range(20):
        if i%2==0:
            sum=sum+i
            
            print(sum)
# Write a function that takes any two integers as input, and prints 
# the sum of all the numbers between the two integers (inclusive) that are divisible by 3.

def divide(num1,num2):
  sum=0
  for i in range(num1,num2+1):    
      if i%3==0:
         sum+=i
  print(sum)

                


    

    

        
                   