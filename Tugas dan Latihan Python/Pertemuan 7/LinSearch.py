# Mencari array (Linear Search)

def search (list,key):
    list1=[]
    flag=False
    for i in range(len(list)):
        if key == list[i]:
            flag=True
            list1.append(i+1)

    if flag==True:
        print("Ketemu di index ke:")
        for i in list1:
            print(i)
            
    else:
        print("Tidak Ketemu")

list=[2,3,5,7,9,12,15,20,25,31]
key=int(input("Nilai yang ingin dicari:"))
search(list,key)

