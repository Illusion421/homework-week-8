
def ZeroDuplicates(array):

    toReturn = []
    AlreadyOccured = set()

    for i in array:

        if i not in AlreadyOccured:
            toReturn.append(i)
            AlreadyOccured.add(i)

        else:
            toReturn.append(0)

    return toReturn


array = [5, 5, 1, 1, 2, 3, 4, 4, 5]
result = ZeroDuplicates(array)
print(result)
