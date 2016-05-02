## noDuplicates.py
# Lauren Tubbs and Jake Hennessy

list = [1,2,3,1,2,3,4,5,4,5,6,6,6,7,1,7]
noDupe = []

def removeDuplicates(list):
    list = noDupe
    for item in list:
        if item not in noDupe:
            noDupe.append(item)
    #print(list)

def main():
    print(list)
    removeDuplicates(list)
    print(list)
main()
