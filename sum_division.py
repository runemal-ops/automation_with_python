import math
def sum_divisors(n):
    # Return the sum of all divisors of n, not including n
    sum=0
    count=2
    if n == 0:
        return 0
    else:
        while count <= math.sqrt(n):
            if n % count == 0:
                if count == n/count :
                    sum = sum + count
                else:
                    sum = sum + (count + n/count)
            count = count + 1
        return (int(sum+1))

print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16
print(sum_divisors(100))