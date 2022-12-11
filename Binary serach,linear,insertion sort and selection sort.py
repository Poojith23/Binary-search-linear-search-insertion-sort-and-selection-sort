#!/usr/bin/env python
# coding: utf-8

# In[3]:


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        
        # If x is greater, ignore left half
        
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half

        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid

        else:
            return mid
 
    # If we reach here, then the element was not present

    return -1

# Test array

arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call

result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# In[7]:


def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)


# In[1]:


#Insertion sort

def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)


# In[2]:


#Selection sort

def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)


# In[ ]:





# In[ ]:




