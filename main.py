# main.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    print("Обратная строка:", reverse_string(user_input))
