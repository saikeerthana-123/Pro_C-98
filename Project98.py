def Swapper():
    print("Welcome to the Data Swapper!!!! You can switch data from two file")
    File1 = input("First file : ")
    File2 = input("Second file : ")

    with open(File1, 'r') as a:
        dataA = a.read()

    with open(File2, 'r') as b:
        dataB = b.read()
        
    with open(File1, 'w') as a:
        a.write(dataB)

    with open(File2, 'w') as b:
        b.write(dataA)

    print("Data Swapped")

Swapper()