# lambda is a way of writing a function without the def keyword and without using the return key word but it will retun the value of the operation
from functools import reduce

sum_total = lambda num : num + num

print(sum_total(5))

greet =  lambda name : f"hello {name}"
print(greet("john"))

# higher order functions are functions that take functions as arguments or return functions as results

# map() is a higher order function that takes a function as an argument and applies it to each elemennt



list_of_numbers = [1, 2, 3, 4, 5,13,89,23 , 12, 9]

squared_list = map(lambda num :  num * num, list_of_numbers)
print(dict(zip(list_of_numbers, squared_list)))

# filter() is a higher order function that takes a function as an argument and applies it to each elemennt and returns a list of the elements that return true


is_even = filter(lambda num : num % 2 ==0, list_of_numbers)
# print(list(is_even))
print(dict(zip(list_of_numbers, is_even)))

# reduce() is a higher order function that takes a function as an argument and applies it to each elemennt and returns a single value
total = reduce(lambda acc, cur : acc + cur , list_of_numbers) 
print(total)


names = ["abuja", "calabar", "kaduna", "kano", "lagos", "makurdi", "minna", "port harcourt"]

char_count = reduce(lambda acc, cur: acc + len(cur), names, 0)
print(char_count)
