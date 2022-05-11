"""
DIRECTIONS:
Given a matrix with columns and n rows, print yes if all columns sum to zero.
"""

# If all of a matrix's columns sum to zero, then the sum of all sums of columns must also be zero.
# By summing the entire matrix, we can determine whether the matrix passes the conditions.
n = int(input())
xTotal = yTotal = zTotal = 0
for i in range(0, n):
    asList = input().split(' ')
    xTotal += int(asList[0])
    yTotal += int(asList[1])
    zTotal += int(asList[2])
print("YES" if (xTotal == 0 and yTotal == 0 and zTotal == 0) else "NO")
