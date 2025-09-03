'''
what is Generator:

A generator in python is a special type of iterator that lets you 
generate values one at a time, instead of storing them all in memory

-> normal function : runs, return once and fiishes
-> Generatro function : can pause execution and resume later using "yield"
keyword

useful of lazy evaluation
'''


def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

'''
difference between return and yield

return -> ends function, sends back one value
yield -> pauses the function, saves its state and allows resuming later
'''

def count_up_to(n):
    i = 1
    while i<= n:
        yield i
        i+=1

gen = count_up_to(5)
# for num in gen:
#     print(num)


'''
Advantages of generators:
-> Memory efficient - They dont store all items in memory.
-> Lazy evaluation - They complete values on the fly
-> infinite Sequence - you can model infinite streams without memory issues.
'''



'''
send() -> Sending data into generator

normally a generator only yields values out
but with .send(value), you can send a value into the geneartor at oint where 
it was paused.
'''

def greeter():
    name = yield "What is your name?"
    yield f"Hello, {name}"

gen = greeter()
print(next(gen))
print(gen.send("Sadat"))

'''
how it works:
-> next(gen) -> runs until the first yield, gives "What is your name?"
-> gen.send("sadat") -> resumes the generator, and "sadat" becomes the result 
of name = yield..
'''

'''
close() -> stopping a generator
generator can be closed explicitly


'''
'''
Generator Delegation with yield from

instead of manually looping over another generator, you can use
yield from to delegate work to a sub-generator
'''

def sub_gen():
    yield 1
    yield 2
    yield 3

def main_gen():
    yield "start"
    yield from sub_gen()
    yield "End"

for val in main_gen():
    print(val)


# Generator Pipelines : ypu can chain generator together to build streaming
# data Pipelines

def numbers():
    for i in range(1,6):
        yield i

def square(nums):
    for n in nums:
        yield n * n

def even(nums):
    for n in nums:
        if n%2 == 0:
            yield n

pipeline = even(square(numbers()))
print(list(pipeline))