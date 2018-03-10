numbers = [2, 4, 2, 6]
def dedup_numbers(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

print dedup_numbers(numbers)