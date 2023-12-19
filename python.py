import random
N = random.randint(4, 30)
print("количество камней в куче:", N)
while True:
    try:
        k = int(input("вы взяли камней: "))
        if (k != 1) and (k != 2) and (k != 3):
            print("можно выбрать 1, 2 или 3 камня!")
            exit()
    except:
        print("введите целое число!")
        exit()
    N -= k
    print(f"осталось {N} камней")
    if N == 1:
        print("Вы победили!")
        exit()
    if N <= 0:
        print("куда так много, перебор)")
        exit()
    if N >= 4:
        p = random.randint(1,3)
    if N == 3:
        p = random.randint(1, 2)
    if N == 2:
        p = 1
    N -= p
    print(f"Я забрал {p} камня, осталось {N} камней")
    if N == 1:
        print("Я победил! ho-ho")
        exit()

