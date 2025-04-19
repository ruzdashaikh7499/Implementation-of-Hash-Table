
class HashTable:
    def __init__(self):                                    
        self.m = int(input("Enter size of hash table: "))     
        self.hashTable = [None] * self.m           
        self.elecount = 0                                    
        print(self.hashTable) 
    
    def hashFunction(self, key):
        return key % self.m

    def isFull(self):
        return self.elecount == self.m

    def linearProbing(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        while self.hashTable[index] is not None:
            index = (index + 1) % self.m
            compare += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print("Data inserted at:", index)
        print(self.hashTable)
        print("No. of comparisons =", compare)

    def getLinear(self, key, data):
        index = self.hashFunction(key)
        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            index = (index + 1) % self.m
        return None

    def quadraticProbing(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        i = 0
        while self.hashTable[index] is not None:
            i += 1
            index = (index + i * i) % self.m
            compare += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print("Data inserted at:", index)
        print(self.hashTable)
        print("No. of comparisons =", compare)

    def getQuadratic(self, key, data):
        index = self.hashFunction(key)
        i = 0
        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            i += 1
            index = (index + i * i) % self.m
        return None    

    def insertViaLinear(self, key, data):
        if self.isFull():
            print("Table is full!")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print("Data inserted at:", index)
            print(self.hashTable)
        else:
            print("Collision occurred. Applying Linear Probing.")
            self.linearProbing(key, data)

    def insertViaQuadratic(self, key, data):
        if self.isFull():
            print("Table is full!")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print("Data inserted at:", index)
            print(self.hashTable)
        else:
            print("Collision occurred. Applying Quadratic Probing.")
            self.quadraticProbing(key, data)


def menu():
    obj = HashTable()
    while True:
        print("\n********** MENU **********")
        print("1. Linear Probing")
        print("2. Quadratic Probing")
        print("3. Exit")
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            while True:
                print("\n1. Insert")
                print("2. Search")
                print("3. Back to Main Menu")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:
                    key = int(input("Enter phone number (key): "))
                    name = input("Enter name: ")
                    obj.insertViaLinear(key, name)
                elif ch2 == 2:
                    key = int(input("Enter key to search: "))
                    name = input("Enter name: ")
                    pos = obj.getLinear(key, name)
                    if pos is None:
                        print("Key not found.")
                    else:
                        print("Key found at index:", pos)
                elif ch2 == 3:
                    break
                else:
                    print("Invalid choice.")
        elif ch == 2:
            obj1 = HashTable()
            while True:
                print("\n1. Insert")
                print("2. Search")
                print("3. Back to Main Menu")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:
                    key = int(input("Enter phone number (key): "))
                    name = input("Enter name: ")
                    obj1.insertViaQuadratic(key, name)
                elif ch2 == 2:
                    key = int(input("Enter key to search: "))
                    name = input("Enter name: ")
                    pos = obj1.getQuadratic(key, name)
                    if pos is None:
                        print("Key not found.")
                    else:
                        print("Key found at index:", pos)
                elif ch2 == 3:
                    break
                else:
                    print("Invalid choice.")
        elif ch == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

# Start the program
menu()
