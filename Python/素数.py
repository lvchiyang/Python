def odd_list():
    '''奇数生成器(不包括1)生成的是一个无限序列'''
    n = 1
    while True:
        n += 2
        yield n

def filter_not_prime(n):
    '''过滤因子'''
    return lambda x : x % n #返回闭包

def primes():
    '''生成素数序列'''
    yield 2
    it = odd_list()
    while True:
        n = next(it)
        yield n
        it = filter(filter_not_prime(n), it)

def is_prime(num):
    '''遍历素数生成器'''
    for i,x in enumerate(primes()):  #为什么函数是可迭 代对象啊
        if x > num:
            break
        else:
            print(x)

def run():
    is_prime(100)


run()
