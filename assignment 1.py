#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to demonstrate printing pattern triangle 
def triangle(n): 
      
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n1=input("provide num")
n=int(n1)
triangle(n)


# In[2]:


def suma(n):
    lis=list()#creating a list to place the numbers inside
    sum=0
    for i in range(1,2*n,2): # setting the range for the loop
        lis.append(i)
        sum=sum+int(i)#adding the individual numbers in the loop
    print("The odd numbers are :",lis) # printing as required in the assignment
    print("The sum of integers is :",sum) # printing as required in the assignment
    

n1=input("Provide the n value")
n=int(n1) #passing values
suma(n)


# In[3]:


def isMonotonic(A): 
 
   return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
           all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
 
# Driver program 
A = [1,2,2,6] 
 
# Print required result 
print(isMonotonic(A))


# In[4]:


def count(arr,k): 
    count = 0
    n=len(arr)
    # Pick all elements one by one 
    for i in range(0, n): 
          
        # See if there is a pair of this picked element 
        for j in range(i+1, n) : 
              
            if arr[i] - arr[j] == k or arr[j] - arr[i] == k: 
                count=count+ 1
    print(count)
arr = [1, 3, 1, 5, 4] 
k = 0
count(arr,k)


# In[5]:


def keyboard(a,b): #takes entry of the keyboard and word
    la=list(a) #convert to list
    ls=list(b) # convert to list
    sum=0
    si=0
    total=0
    for i in ls: #Start taking one character at a time to compare
        if i in la: #if the given chracter is in the keyboard
            index=la.index(i) #find the index of it
            sum=abs(si-index) # subtract the index with the previous index
            total=total+sum #add the sum of index
            si=index # re assign the si index as the previous character's index
    return total # return the total value
            
        
a1="hijklmnopqrstuvwxyzabcdefg"
b1="gobulls"
keyboard(a1,b1)


# In[6]:


def change(str1, str2, c, d): 
  
    # If first string is empty, insert all characters of second string into first 
    if c == 0: 
         return d
  
    # If second string is empty,remove all characters of first string 
    if d == 0: 
        return c 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[c-1]== str2[d-1]: 
        return change(str1, str2, c-1, d-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(change(str1, str2, c, d-1),    # Insert 
                   change(str1, str2, c-1, d),    # Remove 
                   change(str1, str2, c-1, d-1)    # Replace 
                   ) 
  
# Driver program to test the above function 
str1 = "sunday"
str2 = "saturday"
print(change(str1, str2, len(str1), len(str2)))

