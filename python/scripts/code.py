import os


def return_5():
    return 5


def merge_2_lists(listA, listB):
    mergedList = []
    mergedList.extend(a for a in listA if a not in mergedList)
    mergedList.extend(b for b in listB if b not in mergedList)
    return mergedList


def get_filenames_in_directory(directory):
    fileNames = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            fileNames.append(name)
    return fileNames


if __name__ == "__main__":
    return_5()
