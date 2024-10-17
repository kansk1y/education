# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)

# print_number(2, 3, 11)

# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1

# print_text('Python', 4)


def draw_triangle(fill, base):
    for i in range(1, base+1):
        print(fill * i)
    for i in range(base-1, 0 , -1):
        print(fill * i)



draw_triangle('#', 9)