# Dynamic programming stores previous results instead of 
#   recalculating them.
fibonacci_list = [0, 1]
# specify the n th fibonacci number we are interested in
n = 100
for i in range(2, 100):
    fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
print('The %d th fibonacci number is %d\n' % (n, fibonacci_list[n-1]))
