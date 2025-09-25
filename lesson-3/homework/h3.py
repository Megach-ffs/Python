# Task 1
fruits = input("Enter fruits: ").split()
print(fruits[2])

# Task 2
lst1 = list(map(int, input("Enter numers: ").split()))
lst2 = list(map(int, input("Enter numbers: ").split()))
lst3 = lst1 + lst2
print(lst3)

# Task 3
numbers = list(map(int, input("Enter numbers: ").split()))
first_middle_last = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(first_middle_last)

# Task 4
movies = input("Enter 5 movies separated by comma: ").split(",")
movies_tuple = tuple(m.strip() for m in movies)
print(movies_tuple)

# Task 5
cities = input("Enter cities: ").split()
print("Paris" in cities)

# Task 6
nums = list(map(int, input("Enter numbers: ").split()))
dupl = nums * 2
print(dupl)

# Task 7
swap_list = list(map(int, input("Enter numbers: ").split()))
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print(swap_list)

# Task 8
numbers = tuple(map(int, input("Enter numbers: ").split()))
print(numbers[3:8])

# Task 9
colors = input("Enter colors: ").split()
print(colors.count("blue"), "times")

# Task 10
animals = tuple(input("Enter animals: ").split())
print(animals.index("lion"))

# Task 11
tuple1 = tuple(map(int, input("Enter first typle: ").split()))
tuple2 = tuple(map(int, input("Enter second tuple: ").split()))
tuple3 = tuple1 + tuple2
print(tuple3)

# Task 12
sample_list = input("Enter list elements: ").split()
sample_tuple = tuple(input("Enter tuple elements: ").split())
print("Length of list:", len(sample_list))
print("Length of tuple:", len(sample_tuple))

# Task 13
numbers = tuple(map(int, input("Enter 5 numbers for tuple: ").split()))
lst = list(numbers)
print(lst)

# Task 14
num_tuple = tuple(map(int, input("Enter numbers for tuple: ").split()))
print("Max:", max(num_tuple))
print("Min:", min(num_tuple))

# Task 15
words = tuple(input("Enter words for tuple: ").split())
rev_tuple = words[::-1]
print(rev_tuple)

