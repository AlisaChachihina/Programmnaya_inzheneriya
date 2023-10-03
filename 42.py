import random
def main():
    a = int(random.randint(1,6))
    if a == 5 or a == 6:
        print(f"Значение кубика: {a}. Вы победили")
    elif a == 1 or a == 2:
        print(f"Значение кубика: {a}. Вы проиграли")
    else:
        print(f"Значение кубика: {a}.")
        main()
if __name__ == '__main__':
    main()