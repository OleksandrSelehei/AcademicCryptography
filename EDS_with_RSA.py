import random
import math


# Функція для перевірки, чи є число простим.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# Функція для знаходження НСД двох чисел.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


#створення публичного ключа(e)
def choose_public_key(phi_n):
    e = random.randrange(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    return e


#знаходження f(n)
def euler_function(p, q):
    return (p - 1) * (q - 1)


# створення закритого ключа(d)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise ValueError('e is not invertible')
    else:
        return x % phi
    if temp_phi_n == 1:
        d = y2
    return d % phi_n


# створення
def hash_function(text, n, d, h_0):
    h = h_0
    text = list(map(int, str(text)))
    for element in text:
        h = ((element + h) ** 2) % n
    return (h ** d) % n, int(''.join(list(map(str, text)))), h


# Перевірка ЕЦП
def EDS_verification(s, e, n, text, h_0):
    h = h_0
    text = list(map(int, str(text)))
    for element in text:
        h = ((element + h) ** 2) % n
    m = (s ** e) % n
    if m == h:
        return True
    else:
        return False



#Згенерувати два великі прості числа.
p = random.randint(100, 1000)
while not is_prime(p):
    p += 1

q = random.randint(100, 1000)
while not is_prime(q):
    q += 1


#праця програми
n = p * q
phi_n = euler_function(p, q)
public_key = choose_public_key(phi_n)
private_key = modinv(public_key, phi_n)
hesh = hash_function(312, n, private_key, 6)


print(p)
print(q)
print("Добуток")
print(n)
print("Публічний ключ")
print(public_key)
print("Приватний ключ")
print(private_key)
print("Повідомлення")
print(hesh[1])
print("Хеш")
print(hesh[2])
print("Шифрований хеш")
print(hesh[0])
print("Перевірка")
print(EDS_verification(hesh[0], public_key, n, 312, 6))

