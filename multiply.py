# Multiplication between two numbers without using * operator 
# x and y 

def multiply(x,y): 
  
    # 0 multiplied with anything 
    # gives 0  
    if(y == 0): 
        return 0
  
    # Add x one by one  
    if(y > 0 ): 
        return (x + multiply(x, y - 1)) 
  
    # The case where y is negative 
    if(y < 0 ): 
        return -multiply(x, -y) 

# enter numers
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))    
print ("multiplication result is here:")
print(multiply(x, y)) 

#Output looks like this:
Enter first number: 6                                                                                                          
Enter second number: -5                                                                                                        
multiplication result is here:                                                                                                 
-30 
