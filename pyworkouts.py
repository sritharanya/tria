


n=5
for i in range(1,n+1):
 print(' '*(n-i)+'*'*(2*i-1)) 
 '''same condition 1-5 then 4-0'''
for i in range(n-1,0,-1): 
 print(' '*(n-i)+'*'*(2*i-1))

 rows = 5

# Top half
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Bottom half
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

 

 

