# Оператори та операції

# Присвоєння
x = 10         # Основним способом представлення даних у функціональних
x, y = 10, 20  # мовах є кортежі. Це сутність, схожа на stream - основною
# операцією є "читання одного символа" - відокремлення головного елементу
# (head) та залишок решти як "хвоста" (tail) як кортежа.
# unpacking|destructuring - розділення комплексних даних на окремі змінні
x, y = y, x      # swap
x, y = y, x + y  # Фібоначі

# зчеплення кортежів на прикладі форматування рядків
s = "Hello, %s!" % ("World")
s = "x = %d, y = %d" % (x, y)  # функціональний підхід
s = f"x = {x}, y = {y}"  # імперативний підхід

# Аріфметика
x, y = 14, 6
print( "%d + %d = %f" % (x, y, x + y) )
print( "%d - %d = %f" % (x, y, x - y) )
print( "%d * %d = %f" % (x, y, x * y) )
print( "%d / %d = %f" % (x, y, x / y) )    # 2.333333 - int/int -> float
print( "%d %% %d = %f" % (x, y, x % y) )   # %% - '%', залишок ділення
print( "%d ** %d = %f" % (x, y, x ** y) )
print( "%d // %d = %f" % (x, y, x // y) )  # 2.0 int//int -> int
# ще раз наголосимо: % для str - заповнення плейсхолдерів, для int - залишок ділення

# умовний оператор
if x > 2 and y > 2 :          # дужки в умовах не необхідні, тільки для
    print( "Both > 2" )       # зміни пріоритетів: not(x > 2 and y > 2)
elif x > 2 or y > 2 :         # Є блоки elif (else if)
    print( "one > 2" )        # Таких блоків може бути довільна кількість
elif not x > 2 :              # 
    print( "x not > 2" )      # 
else :                        # загальний else - один
    print( "Nothing aforementioned" )
# Кожен з блоків (окрім if) є опціональним, тобто можливі скорочені
# форми: if, if-elif, if-else, ...
# Умовний (тернарний) вираз:
w = 10 if x > 0 else 20

# Оператор циклу
while y > 0 :
    print( y, end=" " )
    y -= 1
else :            # блок успішного завершення - порушення циклової умови
    print()       # у цей блок не заходить, якщо цикл зупинений break

# цикл - ітератор перебирає елементи кортежу, для імперативних задач
# є спеціальний генератор послідовних кортежів - range
r10 = range(10)  # це генератор, сама послідовність отримується поелементно
for i in r10 :
    print( i, end=' ' )   #  0 1 2 3 4 5 6 7 8 9
print()

for i in range(1, 10) :   # від першого включно, до останнього не включно
    print( i, end=' ' )   #  1 2 3 4 5 6 7 8 9
print()

for i in range(1, 10, 2) :  # третій параметр - крок
    print( i, end=' ' )     #  1 3 5 7 9
print()

for i in range(10, 1, -1) :  # крок може бути від'ємний
    print( i, end=' ' )      #  10 9 8 7 6 5 4 3 2
print()
