#Создаем словарь которые будут участвовать в шифровании
def form_dict():
    d = {}
    iter = 0
    for i in range(0, 127):
        d[iter] = chr(i)
        iter += 1
    return d
#Сопостовление букв в слове с буквами в словаре и присвоение соответствующих индексов
def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict()

    for w in range(lent):
        for vaule in d:
            if word[w] == d[vaule]:
                list_code.append(vaule)
    return list_code


def comparate(vaule, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in vaule:
        dic[full] = [i, key[iter]]
        full += 1
        iter += 1
        if (iter >= len_key):
            iter = 0
    return dic

#сопоставляем индексы ключа с индексами нашего слова функцией full_encode():
def full_encode(vaule, key):
    dic = comparate(vaule, key)
    print(f'Сравните полное ли кодирование: {dic}')
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go)
    return lis


def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict()

    for i in range(lent):
        for vaule in d:
            if list_in[i] == vaule:
                list_code.append(d[vaule])
    return list_code
#Раскодировать же все это можно с помощью функции full_decode(), первым аргументом которой есть список числовых индексов шифра, а вторым — список индексов ключа:
def full_decode(vaule, key):
    dic = comparate(vaule, key)
    print(f'Дешифровка = {dic}')
    d = form_dict()
    lis = []

    for v in dic:
        go = (dic[v][0] - dic[v][1]+len(d)) % len(d)
        lis.append(go)
    return lis

if __name__ == "__main__":
    word = input("Введите слово для шифровки: ")
    key = input("Введите ключ: ")

    print(f"Слово: {word}")
    print(f"Ключ: {key}")

    key_encoded = encode_val(key)
    vaule_encoded = encode_val(word)

    print(f"Vaule = ",vaule_encoded)
    print(f"Key = ",key_encoded)

    shifre = full_encode(vaule_encoded, key_encoded)
    print(f"Шифр = ", "".join(decode_val(shifre)))

    decode = full_decode(vaule_encoded, key_encoded)
    print(f"Decode list = {decode}")
    decode_word_list = decode_val(decode)
    print(f"word = ", "".join(decode_word_list))