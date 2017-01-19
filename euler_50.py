"""
Code that solves Project Euler problem 50, Consecutive Prime Sum:
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def get_prime(n):
    """Returns True if n is prime, else False.
    Works in this code for primes less than or equal to 997661

    @type n: int
    @rtype: bool
    """
    for num in primes:
        if n % num == 0:
            return False
        if num > n / 2:
            return True

    return True

primes = [2]
count = 2
iterator = 3

while count + iterator < 1000000:

    if get_prime(iterator):
        primes.append(iterator)
        count += iterator

    iterator += 1

# print(primes, count)
# print(get_prime(8431))

attempt = 0

if get_prime(count):
    print(count)

done = False
while not done:
    sums = []
    end_primes = []

    for i in range(attempt):
        end_primes.append(primes[i])
    sums.append(sum(end_primes))

    for i in range(-1, -attempt-1, -1):
        end_primes[i] = primes[i]
        sums.append(sum(end_primes))

    for i in sums:
        if get_prime(count - i):
            print(count - i, "is the solution!")
            done = True

    attempt += 1

