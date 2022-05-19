fin1 = open("справочник.csv", "r", encoding= "windows-1251")
d = {}

for line in fin1:
    s = line.split(";")
    name = (s[0])
    kkal = (s[1])
    proteins = (s[2])
    fats = (s[3])
    carbohydrates = (s[4])

    # заменим "," на "." и уберем "\n"
    kkal = kkal.replace(',', '.')
    proteins = proteins.replace(',', '.')
    fats = fats.replace(',', '.')
    carbohydrates = carbohydrates.replace(',', '.')
    carbohydrates = carbohydrates.replace('\n', '')
    # carbohydrates = carbohydrates.replace('', '0')

    # заполним словарь d значениями
    d[name] = kkal, proteins, fats, carbohydrates

for i in range(1, 10):
    fin2 = open("раскладка.csv", "r", encoding="windows-1251")  # откроем файл с раскладом по дням.

    kal_sum_day_ = 0
    proteins_sum_day_ = 0
    fats_sum_day_ = 0
    carbohydrates_sum_day_ = 0

    for line in (fin2):
        s2 = line.split(";")
        day = s2[0]
        produkt = s2[1]
        weight = s2[2]
        weight = weight.replace('\n', '')
        weight = weight.replace('Вес в граммах\n', '')

        kal_sum = 0
        proteins_sum = 0
        fats_sum = 0
        carbohydrates_sum = 0

        if day == str(i):
            kal_sum = float(d[produkt][0]) * int(weight) / 100 + kal_sum  # каллорийность
            proteins_sum = float(d[produkt][1]) * int(weight) / 100 + proteins_sum  # белки
            fats_sum = float(d[produkt][2]) * int(weight) / 100 + fats_sum  # жиры
            if (d[produkt][3]) != "":
                carbohydrates_sum = float(d[produkt][3]) * int(weight) / 100 + carbohydrates_sum  # углеводы
            else:
                0
        kal_sum_day_ = kal_sum_day_ + kal_sum
        proteins_sum_day_ = proteins_sum_day_ + proteins_sum
        fats_sum_day_ = fats_sum_day_ + fats_sum
        carbohydrates_sum_day_ = carbohydrates_sum_day_ + carbohydrates_sum

    print(int(kal_sum_day_), end=" ")
    print(int(proteins_sum_day_), end=" ")
    print(int(fats_sum_day_), end=" ")
    print(int(carbohydrates_sum_day_))

fin1.close()
fin2.close()

fin1.close()
fin2.close()
