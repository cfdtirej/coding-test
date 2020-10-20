tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

# 行きがけ順
def snake_search(pos):
    print(pos, end=' ')
    for i in tree[pos]:
        snake_search(i)

# 帰りがけ順
def return_order_search(pos):
    for i in tree[pos]:
        return_order_search(i)
    print(pos, end=' ')

# 通りがけ順
def passing_order_search(pos):
    if len(tree[pos]) == 2:
        passing_order_search(tree[pos][0])
        print(pos, end=' ')
        passing_order_search(tree[pos][1])
    elif len(tree[pos]) == 1:
        passing_order_search(tree[pos][0])
        print(pos, end=' ')
    else:
        print(pos, end=' ')


if __name__ == '__main__':
    snake_search(0)
    print('\n')
    return_order_search(0)
    print('\n')
    passing_order_search(0)
