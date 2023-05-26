# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input("Введите ширину шоколадки: "))
height = int(input("Введите высоту шоколадки: "))
count_segment = int(input("Введите количество долек: "))
if count_segment < width * height and (count_segment % width == 0 or count_segment % height == 0):
    print(f"От шоколадки размером {width}x{height} можно отломить {count_segment} долек")
else:
    print(f"От шоколадки размером {width}x{height} нельзя отломить {count_segment} долек")