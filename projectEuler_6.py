def sum_of_sq(start, end):
  return sum([x**2 for x in range(start, end + 1)])

def sq_of_sum(start, end):
  return sum(range(start, end + 1))**2

start = 1
end = 100

sum_of_sq_val = sum_of_sq(start, end)
sq_of_sum_val = sq_of_sum(start, end)
print(sum_of_sq_val)
print(sq_of_sum_val)
print(sq_of_sum_val - sum_of_sq_val)


