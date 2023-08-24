def generator():
    yield 1
    yield 2
    yield 3


g = generator()


def countDown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countDown(5)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

# Generator Syntax > Equivelent to list comprehensions

g1 = (x for x in range(10) if x % 2 == 0)


# Understanding the memory effeciency of a generator
import sys

# Return list of counted elements


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstgen(n):
    num = 0
    while num < n:
        yield num
        num += 1


l = firstn(100000)  # [0, 1, 2, 3, 4]
g = firstgen(100000)

print(sys.getsizeof(l))  # 800984kb
print(sys.getsizeof(2))  # 28kb
