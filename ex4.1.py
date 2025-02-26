# 
# Exercise 4 Part 1
# The best case complexity for the given code is if li has no elements greater than 5.
# Supposing that n = len(li), the outer loop is 2 operations and would run n times, the if li[i] > 5
# line has 2 operations and would also run n times. For the best case, the inner loop would not execute. 
# Calculating the best case complexity is 2n + 2n = 4n = O(n). So the best case complexity
# is O(n). The worst case complexity is if every element of li is greater than 5. 
# The outer loop and the if li[i] > 5 line both have 2 operations and run n times.
# The inner loop has 2 operations and loops n times, and runs n times due to the outer loop.
# So the inner loop would be 2n^2. The li[i] *= 2 line also has two operations and runs n*n times. So 
# calculating the worst case complexity would be 2n + 2n + 2n^2 + 2n^2 = 4n + 4n^2 = O(n^2).
# So the worst case complexity is O(n^2). The average case would be if li has some elements > 5
# and some <= 5. Supposing the p = % of elements > 5, the average case would be calculated as
# 2n + 2n + p * 2n^2 + p * 2n^2 = O(n^2). p is multiplied by each term that is dependant on 
# the element being > 5. From this, even if one element of li is > 5, the average case complexity
# is O(n^2).

#
# Exercise 4 Part 2
# The best (O(n)), worst (O(n^2)), and average (O(n^2)) cases are not the same.
# Below is an implementation where the case complexity is equivalent for the best,
# worst, and average cases.

def processdata(li):
    for i in range(len(li)):        # 2 ops n times
        for j in range (len[li]):    # 2 ops n * n times
            if li[i] > 5:           # 2 ops n * n times
                li[j] *= 2          # 2 ops n * n times
            
# The above is an implementation of the previous code where the best, worst, and
# average case complexities are the same. Supposing n = len(li), the best case compexity
# is if no elements of li are > 5. The outer loop has 2 operations and runs n times. The
# inner loop, and if statement both have 2 operations and run n*n times. So calculating
# the best case complexity gives 2n + 2n^2 + 2n^2 = 4n^2 + 2n = O(n^2). The worst case
# is if every element of li is > 5. The outer loop is still 2n, the inner loop and if statement
# are still 2n^2. The li[j] *= 2 is 2 operations and runs n*n times. Calculating the 
# worst case complexity is 2n + 2n^2 + 2n^2 + 2n^2 = 2n + 6n^2 = O(n^2). The average case
#  is if some elements are > 5 and some elements are < 5. Suppose that 
# p = % of elements > 5. Then the complexity for the average case would be
# 2n + 2n^2 + 2n^2 + p * 2n^2 = O(n^2). This implementation demonstrates that the 
# best, worst, and average complexities are equivalent, while maintaining the same functionality. 
