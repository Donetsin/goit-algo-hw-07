import avl_tree as avl

# Завдання 1: Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку або в AVL-дереві
def find_max_value(root):
    if root is None:
        return None
    while root.right_child is not None:
        root = root.right_child
    return root.data

# Завдання 2: Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві
def find_min_value(root):
    if root is None:
        return None
    while root.left_child is not None:
        root = root.left_child
    return root.data

# Завдання 3: Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
def sum_of_values(root):
    if root is None:
        return 0
    return root.data + sum_of_values(root.left_child) + sum_of_values(root.right_child)

def main():
    Gavl = avl.AVL()
    Gavl.insert(98)
    Gavl.insert(30)
    Gavl.insert(40)
    Gavl.insert(70)
    Gavl.insert(45)
    Gavl.insert(27)
    Gavl.insert(32)
    Gavl.insert(42)
    Gavl.insert(80)
    Gavl.insert(91)
    Gavl.insert(96)
    Gavl.insert(26)
    Gavl.insert(56)

    Gavl.display()

    print(f'Найбільше значення: {find_max_value(Gavl.root)}')
    print(f'Найменше значення: {find_min_value(Gavl.root)}')
    print(f'Сума всіх значень: {sum_of_values(Gavl.root)}')

if __name__ == '__main__':
    main()

