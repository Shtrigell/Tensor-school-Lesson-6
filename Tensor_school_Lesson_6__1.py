def string_to_byte(s_b):
    """Функция перевода строки в байт код.
    
    Принимает строку - s_b.
    Возвращает байт код, в виде списка - s_b_change.
    
    """
    s_b_change=[]
    for i in range(len(s_b)):
        for j in s_b[i]:
            s_b_change.append(ord(j))
    return s_b_change
def byte_to_string(b_s):
    """Функция перевода байт кода в строку.
    
    Принимает байт код - b_s .
    Возвращает строку, в виде списка - b_s_change.
    
    """
    b_s_change=[]
    for i in range(len(b_s)):
        b_s_change.append(chr(b_s[i]))
    return b_s_change
choice=input("""Введите номер необходимой операции:
1. Преобразование списка строк в список байт кодов.
2. Преобразование списка байт кодов в список строк. """)

if choice=="1":
    result_str_to_bt=string_to_byte(input("Введите текст, через пробел, который хотите преобразовать в список байт кодов: \n").split())
    print("Ваш список байт кодов: ",result_str_to_bt)
elif choice=="2":
    new_list=[]
    old_list=[]
    old_list=input("Введите байт коды, через пробел, который хотите преобразовать строки: \n").split()
    for i in range(len(old_list)):
        try:
            a=int(old_list[i])
        except ValueError:
            print(old_list[i]," - неверный формат данных, данные не будут включены в преобразование. ")
        else:
            new_list.append(a)
    result_bt_to_str=byte_to_string(new_list)
    print("Ваша строка: ",result_bt_to_str)
else:
    print("Неизвестная команда")

