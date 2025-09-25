# Dictionary Exercises

# Task 1
d = { 'a': 3, 'b': 1, 'c': 2 }
asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

# Task 2
d = {0: 10, 1: 20}
d[2] = 30
print(d)

# Task 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic = {}
for d in (dic1, dic2, dic3):
    dic.update(d)
print(dic)

# Task 4
n = int(input("Enter n: "))
sq = {x: x*x for x in range(1, n+1)}
print(sq)

# Task 5
sq = {x: x*x for x in range(1, 16)}
print(sq)


# Set Exercises

# Task 1
s = {1, 2, 3}
print(s)

# Task 2
s = {"a", "b", "c"}
for i in s:
    print(i)

# Task 3
s = {1, 2}
s.add(3)
s.update([4, 5])
print(s)

# Task 4
s = {1, 2, 3, 4}
s.remove(2)
print(s)

# Task 5
s = {1, 2, 3}
s.discard(4)   
print(s)
