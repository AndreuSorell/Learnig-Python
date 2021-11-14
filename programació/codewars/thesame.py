def comp(array1, array2):
    print([array1, array2])
    squared = []
    if isinstance(array2, list) and  isinstance(array1, list):
        for num in array1:
            #acumulador -> squared = squared + nuevo elemento
            squared = squared + [num**2]
    else:
        return array1 == array2
    squared.sort()
    array2.sort()
    return squared == array2


comp([-121, -144, 19, -161, 19, -144, 19, -11], [121, 14641, 20736, 361, 25921, 361, 20736, 361])