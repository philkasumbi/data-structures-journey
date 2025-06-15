def count_ways_top_down(n, memo=None):
    if memo is None:
        memo = {}
        
    if n == 0 or n == 1:
        return 1   
    
    if n in memo:
        return memo[n]
    
    memo[n] = count_ways_top_down(n - 1, memo) + count_ways_top_down(n - 2, memo)
    return memo[n]
     
input = int(input("Enter a number: "))

print(f"ways to reach step {input} is: {count_ways_top_down(input)} ways")
