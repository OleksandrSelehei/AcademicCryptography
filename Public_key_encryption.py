# логіка
# функція поділу повідомлення на рівні частини
def split_string(string, number):
    length = len(string)
    return [string[i:i + length // number] for i in range(0, length, length // number)]


# алгоритм Евкліда
def euclidean_algorithm(a, m):
    while m != 0:
        a, m = m, a % m
    return a


# знаходження оберненого дійсного числа
def inverse_mod(a, m):
    if euclidean_algorithm(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1,
            u2 - q * v2,
            u3 - q * v3,
            v1,
            v2,
            v3,
        )
    return u1 % m


# перетворення з восьмеричної в десятичну систему
def dec_to(octal_number):
    decimal = 0
    for digit in octal_number:
        decimal = decimal * 8 + int(digit)
    return decimal


# перетворення с десятичної в двійкову систему
def dec_to_bin(n):
    n = dec_to(str(n))
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = binary + str(n % 2)
        n //= 2
    return binary


# створення пари ключів
def pair_of_keys():
    private_key = [1, 2, 4, 10, 20, 40]
    public_key = [i * 31 % 110 for i in private_key]
    return private_key, public_key


# шифрування повідомлення
def encryption(message, public_key):
    encryption_message = []
    number = len(message) / len(public_key)
    work_message = split_string(message, int(number))
    for element_message in work_message:
        result = 0
        index = 0
        for item in element_message:
            if item == '1':
                result += public_key[index]
            index += 1
        encryption_message.append(result)
    return encryption_message


# дешифрування повідомлення
def decryption(encryption_message, weight):
    decryption_number_message = []
    decryption_message = ''
    for item in encryption_message:
        decryption_number_message.append(item * inverse_mod(31, 110) % 110)
    for decryption_number in decryption_number_message:
        decryption_bin = dec_to_bin(decryption_number)
        while True:
            if len(decryption_bin) != weight:
                decryption_bin = decryption_bin + '0'
            else:
                break
        decryption_message = decryption_message + decryption_bin
    return decryption_message


# інтерфейс
flag = True
private_key_, public_key_ = pair_of_keys()
while flag:
    print("Оберіть дії: \n1/Зашифрувати повідомлення.\n2/Розшифрувати повідомлення.\n3/Вихід.")
    actions = input()
    if actions == '1':
        message_ = input('Введіть повідомлення: ')
        encryption_message_ = encryption(message_, public_key_)
        print(f'Зашифроване повідомлення: {encryption_message_}')
    elif actions == '2':
        message_ = input('Введіть зашифроване повідомлення через пробіл: ')
        message_ = [int(n) for n in message_.split()]
        decryption_message_ = decryption(message_, len(private_key_))
        print(f'Розшифроване повідомлення: {decryption_message_}')
    elif actions == '3':
        flag = False
        print("Допобачення!")
    else:
        print("Error!")
    print('-' * 50)
