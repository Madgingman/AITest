
def main(data, value):
    if data is None:
        print('Data is mandatory, but was not specified')
        return
    elif value is None:
        print('Value is mandatory, but was not specified')
        return

    if any(data[i] > data[i + 1] for i in range(0, len(data) - 1)):
        data.sort()
        print('Data was sorted:', data)

    search(data, value)


def search(data, value):
    i = 0
    j = len(data) - 1

    while i < j:
        k = int((i + j) / 2)
        if value > data[k]:
            i = k + 1
        else:
            j = k

    if i < len(data) and data[i] == value:
        print('Index =', i)
    else:
        print('Value was not found')


if __name__ == '__main__':
    print('Test: Smoke')
    main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
    print('Test: Unsorted array')
    main([1, 2, 3, 4, 5, 11, 6, 7, 8, 9, 10], 11)
    print('Test: Non existing value')
    main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
    print('Test: String data')
    main(['aaa', 'bbb', 'c34', 'hw'], 'c34')
    print('Test: Empty data')
    main([], 5)
    print('Test: Data is not specified')
    main(None, 5)
    print('Test: Value is not specified')
    main([1, 2], None)
