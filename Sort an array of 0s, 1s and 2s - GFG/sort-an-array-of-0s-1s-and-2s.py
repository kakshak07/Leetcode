#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        a=arr
        arr_size=n
        lo = 0
        hi = arr_size - 1
        mid = 0
        # Iterate till all the elements
        # are sorted
        while mid <= hi:
            # If the element is 0
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo = lo + 1
                mid = mid + 1
            # If the element is 1
            elif a[mid] == 1:
                mid = mid + 1
            # If the element is 2
            else:
                a[mid], a[hi] = a[hi], a[mid]
                hi = hi - 1
        return a
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends