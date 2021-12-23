list_lower_RU = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
list_upper_RU = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']

list_lower_EU = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_upper_EU = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lenguaje = input('Выберите язык сообщения (RU/EU): ')
chois = input('Выберите Шифровать или дешифровать (ENC/DEC): ')
messege = input('Введите сообщение которое нужно зашифровать или дешифровать: ')
shift = int(input('Введите шаг шифровки или дешифровки: '))
cikl = input('Нужно ли зациклить программу (Y/N): ')
n = int(input('Введите количество циклов работы программы: '))


def encrypt(messege, shift, lenguaje):
    ret = ''
    if lenguaje == "RU":
        for x in messege:
            if x in list_lower_RU:
                ind = list_lower_RU.index(x) % len(list_lower_RU)
                ret += list_lower_RU[(ind+shift) % len(list_lower_RU)]
            elif x in list_upper_RU:
                ind = list_upper_RU.index(x) % len(list_lower_RU)
                ret += list_upper_RU[(ind+shift) % len(list_lower_RU)]
            else:
                ret += x
        return ret

    elif lenguaje == "EU":
        for x in messege:
            if x in list_lower_EU:
                ind = list_lower_EU.index(x) % len(list_lower_EU)
                ret += list_lower_EU[(ind + shift) % len(list_lower_EU)]
            elif x in list_upper_EU:
                ind = list_upper_EU.index(x) % len(list_lower_EU)
                ret += list_upper_EU[(ind + shift) % len(list_lower_EU)]
            else:
                ret += x
        return ret

def decrypt(messege, shift, lenguaje):
    ret = ''
    if lenguaje == "RU":
        for x in messege:
            if x in list_lower_RU:
                ind = list_lower_RU.index(x)
                ret += list_lower_RU[ind-shift]
            elif x in list_upper_RU:
                ind = list_upper_RU.index(x)
                ret += list_upper_RU[ind-shift]
            else:
                ret += x
        return ret
    elif lenguaje == "EU":
        for x in messege:
            if x in list_lower_EU:
                ind = list_lower_EU.index(x)
                ret += list_lower_EU[ind - shift]
            elif x in list_upper_EU:
                ind = list_upper_EU.index(x)
                ret += list_upper_EU[ind - shift]
            else:
                ret += x
        return ret


for _ in range(1, n+1):
    if chois == "ENC":
        print(encrypt(messege, shift, lenguaje))

    elif chois == "DEC":
        print(decrypt(messege, shift, lenguaje))