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


#створення публичного ключа
def choose_public_key(phi_n):
    e = random.randrange(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    return e


#знаходження f(n)
def euler_function(p, q):
    return (p - 1) * (q - 1)


# створення закритого ключа
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


#шифрування
def encryption(text, n, public_key):
    result = []
    text = list(map(int, str(text)))
    for element in text:
        result.append((element ** public_key) % n)
    return result


#дешифрування
def decription(arr, n, private_key):
    result = []
    for element in arr:
        result.append((element ** private_key) % n)
    return int(''.join(list(map(str, result))))


# Згенерувати два великі прості числа.
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
cript_text = encryption(312, n, public_key)
decript_text = decription(cript_text, n, private_key)

print("Добуток")
print(n)
print("Публічний ключ")
print(public_key)
print("Зашифрване повідомлення")
print(cript_text)
print("Розшифроване повідомлення")
print(decript_text)
