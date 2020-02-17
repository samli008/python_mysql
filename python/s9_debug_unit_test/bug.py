# demo bug
numbers=[1,2,3,4,5,6,10,-4,-7,0]

def all_even(num_list):
  even_numbers=[]
  for number in num_list:
    if number%2==0:
      even_numbers.extend(number)
  return even_numbers

print(all_even(numbers))

# demo normal
numbers=[1,2,3,4,5,6,10,-4,-7,0]

def all_even(num_list):
  even_numbers=[]
  for number in num_list:
    if number%2==0:
      even_numbers.append(number)
  return even_numbers

print(all_even(numbers))
