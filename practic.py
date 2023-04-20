def multiply(num1,num2):
    product =num1*num2
    if product<=1000:
        return product
    else: 
        return num1+num2

def sum_multiply(sum,product):
    return (f'the sum of 2 and 6 is {sum} and their product is {product}')
print(sum_multiply(6+2+7+3+2,6*2)) 

def names(firstname="av",secname="bv"):
    return(f"my name is {firstname} {secname}")
print(names())
print(names ("loice"))
print(names("mercy","orishaba"))
print(names(firstname="orishaba",secname="mercy"))
    
def firstname(*names):
    for name in names:
     print(name)
    # print(f"hello{final}")
firstname("orishaba","mercy","demo","faith")

def firstname(**names):
    for name in names.values():
        print(name)

firstname(a="mercy",b="orishaba",c="loice")
name ="orishaba"
print(name[3::-1])
print(name[::-1])
print(name[::-3])

# def addition(Intergers):
#     sum=0
#     for interger in intergers:
#         result+=
   
def palindrome(word):
    word='noon'
    passing = word[::-1] 
    if passing==word:
     return "true"
    else:
       return "false"
print(palindrome("noon"))
def addition(num1,num2):
    sum =num1+num2
    print(sum)
def multiply(a,b):
    product =a*b
    print(product) 
def subtract(h,j):
    subr =h-j
    print(subr)       


def eatables(*fruits):
    return fruits.append()
#Given a range of numbers from 0 to 100, console”Fizz” if the numbers are divisible by 3,
# “Buzz” if the numbers are divisible by 5, and “FizzBuzz” if divisible by both 3 and 5.
def divisible():
     for i in range (101):
         if i%3==0 and i%3==0:
             print("fizzbuzz")
         elif i%3==0:
             print("fizz") 
         elif i%5==0:
             print("buzz")  
         else:
             print (i)
                      


