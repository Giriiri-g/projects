## [Array Class Definition]

class Array:
    def __init__(self, size=0):
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index):
        print(index)
        return
        if self.size-1 <index:
            print("Index out of Bounds")
            return
        return self.data[index]

    def __setitem__(self, index, value):
        if self.size-1 <index:
            print("Index out of Bounds")
            return
        self.data[index] = value

    def __len__(self):
        return self.size

    def __str__(self):
        return f"Array({self.data})"

    def __delitem__(self, index):
        if self.size-1<index:
            print("Index out of Bounds")
            return
        self.data.pop(index)
        self.size -= 1

    def __iter__(self):
        return iter(self.data)

    def sort(self):
        self.data = qsort(self.data)
        return self
## [Efficient Quick Sort for Arrays]

    
def qsort(arr):
    if len(arr) <= 1:
        return arr
    piv = arr[0]
    l = [x for x in arr[1:] if x < piv]
    r = [x for x in arr[1:] if x >= piv]
    return qsort(l) + [piv] + qsort(r)

## [Array - Labsheet 1]

size = int(input("Enter the size of the Array : "))
arr = Array(size)
for i in range(size):
    arr[i] = int(input(f"Enter the {i}th Element :"))
arr.sort()
