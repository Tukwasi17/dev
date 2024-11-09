def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return False
    if lst[index] == target:
        return True
    return recursive_search(lst, target, index + 1)
numbers = [1, 3, 5, 7, 9, 11]
print(recursive_search(numbers, 7))
print(recursive_search(numbers, 4))