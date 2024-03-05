# Binary Search

def BinarySearch(list,key):
    low=0
    high=len(list)-1
    Found = False
    while low<=high and not Found:
        mid = (low+high)//2
        if key == list[mid]:
            Found = True
        elif key > list [mid]:
            low=mid+1
        else:
            high = mid-1
    if Found == True:
        print("Ketemu di indeks:")
    else:
        print("Nggak Ketemu")


list=[29,2,30,5,7,9,12,15,20,25,31]
list.sort()
print(list)
key=int(input("Nilai yang ingin dicari:"))
BinarySearch(list,key)


