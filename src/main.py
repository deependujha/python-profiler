import time
import cProfile

def add(x, y):
    resulting_sum = 0
    resulting_sum += x
    resulting_sum += y
    print(fact(700))
    return resulting_sum

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def do_stuff():
    result = []
    for x in range(100000):
        result.append(x**2)
    return result

def waste_time():
    time.sleep(5)
    print("hello")

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(add(100, 5000))
        print(do_stuff())
        waste_time()
    pr.dump_stats(file="profile.prof")
