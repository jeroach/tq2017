def return_5():
    return 5


def merge_2_lists(listA, listB):
    mergedList = []
    mergedList.extend(a for a in listA if a not in mergedList)
    mergedList.extend(b for b in listB if b not in mergedList)
    return mergedList


if __name__ == "__main__":
    return_5()
