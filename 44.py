def main(*args):
    k = 0
    sum = 0
    for i in args:
        k += 1
        sum += i
    print(sum / k)
if __name__ == '__main__':
    main(4, 5, 7, 6, 8, 3, 2)