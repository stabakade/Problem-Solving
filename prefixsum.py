#this file has every general modification tha can be applied on prefix sum
#here the basic code is given first
from collections import defaultdict

def fillprefixsum(prefixarray, n, arr):
    
    prefixarray[0] = 0  #initialise the array

    for index in range(1, n):
        prefixarray[index] = prefixarray[index-1] + arr[index]   #main logic of prefix sum array

#______________________________________________________________________________________________________________________
#helping questions
#Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, 
#returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.

# [-7, 1, 5, 2, -4, 3, 0]  will return index 3 because -7+1+5 = -4+3+0
#here we can use the prefix sum concept

def equillibrium(arr, n):

    leftsum = 0
    rightsum = sum(arr)  #initialise both of these sums 

    for index, number in enumerate(arr):
        #for every index right sum will be get subtracted 
        rightsum -= number
        if rightsum == leftsum: #if that sum is equal to leftsum we have found our index
            return index
        leftsum += number #otherwise add value at index i to the leftsum before moving to next index

    return -1 #if equilibrium not found

#      Time complexity of the solution is O(n)
#___________________________________________________________________________________________________________________________

# Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.
#Use hashing. The idea is to iterate through array and for every element arr[i] calculate sum += arr[i]
#if it's in hashtable we have found zero sum unless keep looking
#we can use set or dictionary as a hash table here
def zerosum(arr):

    d = defaultdict()  #create a hashtable
    sum = 0 

    for i, v in enumerate(arr):
        sum += v
        if sum in d or sum ==0:     
            for j in range(d[sum]+1, i+1):   #prints all indices whose elements sum equals zero
                print(j, end=" ")
            return 
        else:
            d[sum] = i   #add it to hashtable
    print("not found")

#The time complexity of the solution is O(n) if time for printing the indices is not taken
#______________________________________________________________________________________________________________


