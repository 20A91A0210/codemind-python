
def isUgly(n):
 
    # Base Cases
    if (n == 1):
        return 1
    if (n <= 0):
        return 0
 
    # Condition to check if the
    # number is divided by 2, 3, or 5
    if (n % 2 == 0):
        return (isUgly(n // 2))
         
    if (n % 3 == 0):
        return (isUgly(n // 3))
     
    if (n % 5 == 0):
        return (isUgly(n // 5))
 
    # Otherwise return false
    return 0
 
# Driver Code
if __name__ == "__main__":
 
    no = isUgly(int(input()))
     
    if (no == 1):
        print("Ugly Number")
    else:
        print("Not Ugly Number")