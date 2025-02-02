def unique_elements(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique
