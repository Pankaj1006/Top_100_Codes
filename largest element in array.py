def findMaxRec(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMaxRec(A, n - 1))
 
# Driver Code
if __name__ == "__main__":

lst = []
  
num = int(input("Enter number of elements : "))
  
for i in range(0, num):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
    print(lst)
n = len(A)
print(findMaxRec(A, n))
