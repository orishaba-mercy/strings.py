def even_numbers():
    x =range (10)
    for i in x:
        if i%2==0:
            print(i)

def divisible_by_five():
    x= range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not divisible by 5")





 # ELIF Statement
def multiple_comprison():
    x= range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
    
        elif i%7==0:
            print(f"{i} is divisible by 7")
    
        elif i%9==0:  
            print(f"{i} is divisible by 9")
        else:
            print(f"{i} is divisible by 5,7 and 9")


def add_or_even():
    x=range (20)
    for i in x:
        if i%2==0 and i%3==0:
            print(f"{i} is divisible by both 2 and 3")
        elif i%2==0 or i%3==0:
            print(f"{i} is divisible by either 2 or 3")
        else:
            print(f"{i} is not divisible by either 2 or 3")

def while_loop():
    x=1
    while x<10:
        print("hello")
        x+=1    

                # break statement stops the looping evn if the condition is true.
def break_statement():
    x=1
    while x<10:
        print("hello")
        x+=1 
        if x==5:
            break  
        # continue statement
        # it skips the reminder of the current iteration and moves to the next iteration (2,4,6 it jumped 1,3 )

def continue_statement():
    x=0
    while x<=20:
        x+=1
        if x%3==0:
            continue
        print(x)       


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

                


    

    

        
                   