# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)

# print_number(2, 3, 11)

# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1

# print_text('Python', 4)


# объявление функции
def draw_triangle(fill, base):
    for i in (base, -1):
        print('#' * i)
    # for i in (base, base-1, +1):
    #     print('#' * i)
    

# считываем данные
fill = '#'
base = 9

# вызываем функцию
draw_triangle(fill, base)