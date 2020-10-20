def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        # 探索範囲の中央を計算
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
        # 中央の値より大きい場合は範囲を左に
            left = mid + 1
        # 中央の値より大きい場合は範囲を右に
        else:
            right = mid - 1
    return 'Nothing'


if __name__ == '__main__':
    data = [_ for _ in range(10, 91, 10)]
    print(binary_search(data, 90))
