# Python. Вступ. Основи
# Загальна характеристика:
# - покоління: 4
# - спосіб виконання: інтерпретатор (REPL)
# - парадигма: мульти-, основна - функціональна
# - типізація: динамічна, фіксована при записі
x = 2j                 # Python орієнтований на математику, зокрема
print( x, type(x) )    # вбудована підтримка комплексних чисел (j - уявна одиниця)
                       # Розділення команд - ";" або розрив рядка
y = 11                 # Змінні оголошувати не треба, вони створюються першим присвоюванням
print( y, type(y) )    # 11 <class 'int'>
                       # Тип змінних встановлюється присвоєнням і надалі не змінюється
                       # (до іншого присвоєння)
w = x + y              # Тест на "суворість" типізації
print( w, type(w) )    # (11+2j) <class 'complex'>

x = "2"                # нове присвоєння змінює тип, тепер х - str
#print( x + y )        # TypeError: can only concatenate str (not "int") to str
#print( y + x )        # TypeError: unsupported operand type(s) for +: 'int' and 'str'
                       # Оператори переозначені для різних типів, тому помилки різні
print( int(x) + y )    # 3
print( x + str(y) )    # 21

print( 2 ** 1024 )     # Python 3 підтримує BigNumber, формального найбільшого числа не існує

if y < 10 :                # Формування блоків - починається ":"
    print( "y is" )        # і задається відступами
    print( "less than" )   # до одного блоку належать інструкції, що 
    print( "10" )          # мають однаковий відступ
else :                     # Кінець блоку задається втяжкою
  print( "y is not" )      # Новий блок також задається відступами    
  print( "less than" )     # Відступи у новому блоці можуть відрізнятись 
                           # від попереднього, але мають однаковими між собою
  print( "10" )            # пропуск рядка на блок не впливає


# Введеня даних (зі стандартного потоку)
x = input( "Введіть х = " )   # Введіть х = 10      
print( x, type(x) )           # 10 <class 'str'>
x = int(x)                    # 
print( x, type(x) )           # 10 <class 'int'>       

# Рядкові літерали
x = 'Hello'               # один рядок (без розривів)
x = "World"               # різниці між '' та "" немає
x = '''
Hello, World'''
x = """
Hi, All!
"""
# багаторядковий синтаксис вживають також для коментарів
"""
Формально, це рядок, але нічому не присвоєний він є коментарем
"""