# demo debug by pdb
# pdb mode cli: ? list step(s) print(p)
import pdb

numbers=[1,2,3,4,5,6,10,-4,-7,0]

pdb.set_trace() #add this line where you want to start debug mode

def all_even(num_list):
  even_numbers=[]
  for number in num_list:
    if number%2==0:
      even_numbers.extend(number)
  return even_numbers

print(all_even(numbers))

# pdb mode demo with list step(s)
# step(s) into function()
(Pdb) s
> /root/debug_pdb.py(12)all_even()
-> even_numbers.extend(number)
(Pdb) list
  7  
  8     def all_even(num_list):
  9       even_numbers=[]
 10       for number in num_list:
 11         if number%2==0:
 12  ->       even_numbers.extend(number)
 13       return even_numbers
 14  
 15     print(all_even(numbers))
 16  
[EOF]
(Pdb) s
TypeError: 'int' object is not iterable
> /root/debug_pdb.py(12)all_even()
-> even_numbers.extend(number)
(Pdb) p number
2

# pdb mode demo with list next(n)
# next(n) don't into function()
(Pdb) list
 10       for number in num_list:
 11         if number%2==0:
 12           even_numbers.extend(number)
 13       return even_numbers
 14  
 15  -> print(all_even(numbers))
 16  
[EOF]
(Pdb) n
TypeError: 'int' object is not iterable
> /root/debug_pdb.py(15)<module>()
-> print(all_even(numbers))
