import math
biology = int(input("Количество биологов: "))
informatics = int(input("Количество информатиков: "))

gcd = math.gcd(biology, informatics)
lcm = (biology * informatics) // gcd
print("Наименьшее общее кратное равно {", lcm, "}.")