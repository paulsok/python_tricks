import random


def partition(seq, start, stop):
    # pivotIndex comes from the start location in the list.
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start + 1
    j = stop - 1

    while i <= j:

        while i <= j and not pivot < seq[i]:
            i += 1

        while i <= j and pivot < seq[j]:
            j -= 1

        if i < j:
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            i += 1
            j -= 1

    seq[pivotIndex] = seq[j]
    seq[j] = pivot

    return j


def quicksortRecursively(seq, start, stop):
    if start >= stop-1:
        return
    # pivotIndex ends up in between the two halves
    # where the pivot value is in its final location.
    pivotIndex = partition(seq, start, stop)
    quicksortRecursively(seq, start, pivotIndex)
    quicksortRecursively(seq, pivotIndex+1, stop)

    return seq


def quicksort(seq):
    # randomize the sequence first
    for i in range(len(seq)):
        j = random.randint(0, len(seq)-1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp

    quicksortRecursively(seq, 0, len(seq))

    return seq


def main():
    seq = [93, 75, 9, 82, 345, 8, 2, 34, 5, 923]
    print(seq)
    new_seq = quicksort(seq)
    print(new_seq)


if __name__ == '__main__':
    main()
