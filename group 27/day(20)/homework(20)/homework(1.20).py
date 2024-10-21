#1)
num_list=[1,2,3,4,5,6,7,8,9,10]
def num_list_sum():
    print(sum(num_list))

num_list_sum()    
#9)
def prime_number():
    primenumber=int(input()) 
    if primenumber!=float:
        print(True)
    else:
        print("it is not a prime number,try again") 
prime_number()