#You are required to create a linked list that contains the following 'private' member variables:

#tuneID, tuneName, tuneGroup, tuneGenre, dateEntry, chartPosition, price

#Create a linked list of your music library to simulate a personal music library system. Your program is to include the following functionality:

#1. Add a new item to the Linked List (options: beginning, end or middle)
#2. Display all items in your Music Library
#3. Search for and display a song (you build the search options)
#4. Search for and display all items from a specific genre (i.e. pop, rock etc)
#5. Delete an item (Choices: 1. From Start, 2. From End 3. Search).
#6. Sort the items in the alphabetically linked list (options by song, genre or group) using one of the sorting options (insertion, selection or bubble sort).
import csv
import datetime
import math
import uuid

class Tune:
    #Tune object, which has the getters, setters and private memeber variables for name, group, genre, price, date and od
    def __init__(self, tuneName, tuneGroup, tuneGenre, tunePrice, tuneDate, tuneId):
        self.__id = tuneId
        self.__name = tuneName
        self.__group = tuneGroup
        self.__genre = tuneGenre
        self.__date = tuneDate
        self.__price = tunePrice

    def setId(self, tuneId):
        self.__id = tuneId

    def getId(self):
        return self.__id

    def setName(self, tuneName):
        self.__name = tuneName

    def getName(self):
        return self.__name

    def setGroup(self, tuneGroup):
        self.__group = tuneGroup

    def getGroup(self):
        return self.__group

    def setGenre(self, tuneGenre):
        self.__genre = tuneGenre

    def getGenre(self):
        return self.__genre

    def setDate(self, tuneDate):
        self.__date = tuneDate

    def getDate(self):
        return self.__date

    def setPrice(self, tunePrice):
        self.__price = tunePrice

    def getPrice(self):
        return self.__price

class LinkedList:
    #Linked list object that has the getters, setters and private member variables for the next, previous and current (song in the list).
    def __init__(self, next, previous, current):
        self.__next = next
        self.__previous = previous
        self.__current = current

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

    def setPrevious(self, previous):
        self.__previous = previous

    def getPrevious(self):
        return self.__previous

    def setCurrent(self, current):
        self.__current = current

    def getCurrent(self):
        return self.__current

class Main:
    #Initiate the variables head, tail and length
    head = None
    tail = None
    length = 0

    #Main menu method
    def menu(self):
        print("Generic Python Music Player")
        print("----------------------------")
        print("1. Display library")
        print("2. Add song to library")
        print("3. Search library")
        print("4. Remove song from library")
        print("5. List library alphabetically")
        print("0. Exit")
        print("")

        #Based on selection, the next method is run
        selection = input("Select action :")
        if selection == '1':
            self.displayLibrary()
            self.menu()
        elif selection == '2':
            self.addSong()
            self.saveCSV()
            self.menu()
        elif selection == '3':
            self.searchLibrary()
            self.menu()
        elif selection == '4':
            self.seek()
            self.saveCSV()
            self.menu()
        elif selection == '5':
            self.sortLibrary()
            self.menu()
        elif selection == '0':
            exit()
        else:
            print("Invalid input")

    #Lists the songs in the library
    def displayLibrary(self):
        item = self.head
        if item is None:
            print("--------------------------")
            print("Library is currently empty")
            print("--------------------------")
        else:
            while item.getNext() is not None:
                print(item.getCurrent().getName())
                item = item.getNext()
            print(item.getCurrent().getName())

    #Creates the song object you wish to add to the library
    def addSong(self):
        print("Enter the song info")
        print("--------------------")
        name = input("Enter the song's name: ")
        group = input("Enter the group who made the song: ")
        genre = input("Enter the song's genre: ")
        price = input("Enter the song's price: ")
        id = uuid.uuid4()
        date = datetime.datetime.now()
        song = Tune(id, name, group, genre, date,  price)
        listElement = LinkedList(None, None, song)
        print("")

        #Menu which allows the user to choose where to add song in library
        print("Where in the library would you like to add a song?")
        print("---------------------------------------------------")
        print("1. Start")
        print("2. Middle")
        print("3. End")
        print("")

        #Based on selection, relevant method will run
        selection = input("Select action: ")
        if selection == '1':
            self.addToStart(listElement)
        elif selection == '2':
            self.addToMiddle(listElement)
        elif selection == '3':
            self.addToEnd(listElement)
        else:
            print("Invalid input")

    #Adds the song to the start of the library
    def addToStart(self, song):
        if self.head is None:
            self.head = song
            self.tail = song
        else:
            song.setNext(self.head)
            self.head.setPrevious(song)
            self.head = song

        self.length += 1

    # Adds the song to the middle of the library, where the middle is equal to the half the length of the linked list (rounds down)
    def addToMiddle(self, song):
        count = 0
        if self.head is None:
            self.head = song
            self.tail = song
        else:
            middle = self.length / 2
            middle = math.floor(middle)
            item = self.head
            while item.getNext() is not None:
                if middle == count:
                    song.setNext(item)
                    song.setPrevious(item.getPrevious())
                    item.getPrevious().setNext(song)
                    item.setPrevious(song)

                count += 1
                item = item.getNext()

            if middle == count:
                song.setNext(item)
                song.setPrevious(item.getPrevious())
                item.getPrevious().setNext(song)
                item.setPrevious(song)

        self.length += 1

    # Adds the song to the end of the library
    def addToEnd(self, song):
        if self.head is None:
            self.head = song
            self.tail = song
        else:
            song.setPrevious(self.tail)
            self.tail.setNext(song)
            self.tail = song

        self.length += 1

    #Menu that allows the user to choose what they wish to search the library by
    def searchLibrary(self):
        print("What do you want to search the library by?")
        print("1. Song name")
        print("2. Genre")
        print("")

        #Based on selection, relevant method is run.
        selection = input("Select action: ")
        if selection == '1':
            self.searchByName()
        elif selection == '2':
            self.searchByGenre()
        else:
            print("invalid option")

    #Searches the linked list for a name input by the user, both the name and the items in the list are set to uppercase for flexibility
    def searchByName(self):
        name = input("Enter the name of the song you want to search for: ").upper()
        item = self.head
        while item.getNext() is not None:
            if item.getCurrent().getName().upper() == name:
                print(item.getCurrent().getName(), item.getCurrent().getGroup(), item.getCurrent().getGenre(), item.getCurrent().getPrice())
            item = item.getNext()
        if item.getCurrent().getName().upper() == name:
            print(item.getCurrent().getName(), item.getCurrent().getGroup(), item.getCurrent().getGenre(), item.getCurrent().getPrice())

    # Searches the linked list for a genre input by the user, both the name and the items in the list are set to uppercase for flexibility
    def searchByGenre(self):
        genre = input("Enter the genre of the song you want to search for: ").upper()
        item = self.head
        while item.getNext() is not None:
            if item.getCurrent().getGenre().upper() == genre:
                print(item.getCurrent().getName(), item.getCurrent().getGroup(), item.getCurrent().getGenre(),
                      item.getCurrent().getPrice())
            item = item.getNext()
        if item.getCurrent().getGenre().upper() == genre:
            print(item.getCurrent().getName(), item.getCurrent().getGroup(), item.getCurrent().getGenre(),
                  item.getCurrent().getPrice())

    # Searches the linked list for a name input by the user, both the name and the items in the list are set to uppercase for flexibility
    # The desired element is then passed as an argument for the method that will remove it
    def seek(self):
        name = input("Enter the name of the song you want to search for and remove: ").upper()
        element = self.head
        while element.getNext() is not None:
            if element.getCurrent().getName().upper() == name:
                self.andDestroy(element)
                return True
            element = element.getNext()
        if element.getCurrent().getName().upper() == name:
            self.andDestroy(element)

    #Method that removes the desired element from the linked list
    def andDestroy(self, element):
        #Accounts for if the element is the only element in the list
        if self.head == element and self.tail == element:
            self.head = None
            self.tail = None
            print("Song removed")

        #Accounts for if the element is the head of the list
        elif self.head == element:
            element.getNext().setPrevious(None)
            self.head = element.getNext()
            print("Song removed")

        #Accounts for if the element is the tail of the list
        elif self.tail == element:
            element.getPrevious().setNext(None)
            self.tail = element.getPrevious()
            print("Song removed")

        #Accounts for if the element is somewhere in the middle of the list
        elif self.head != element and self.tail != element:
            element.getNext().setPrevious(element.getPrevious())
            element.getPrevious().setNext(element.getNext())
            print("Song removed")

        else:
            print("That song does not feature in the library")

        self.length -= 1

    #Menu that allows the user to choose what to sort by
    def sortLibrary(self):
        print("What would like to sort alphabetically?")
        print("1. Name")
        print("2. Group")
        print("3. Genre")
        print("")
        selection = input("Select action: ")

        #Runs relevant method based on selection
        if selection == '1':
            self.sortName()
        elif selection == '2':
            self.sortGroup()
        elif selection == '3':
            self.sortGenre()
        else:
            print("Invalid input")

    #Uses selection sort to sort names of songs alphabetically
    def sortName(self):
        sortedList = []
        item = self.head
        if item is None:
            print("--------------------------")
            print("Library is currently empty")
            print("--------------------------")
        else:
            while item.getNext() is not None:
                sortedList.append(item.getCurrent().getName())
                item = item.getNext()
            sortedList.append(item.getCurrent().getName())
            for i in range(len(sortedList)):

                # Find the minimum element in remaining
                minPosition = i

                for j in range(i + 1, len(sortedList)):
                    if sortedList[minPosition] > sortedList[j]:
                        minPosition = j

                # Swap the found minimum element with minPosition
                temp = sortedList[i]
                sortedList[i] = sortedList[minPosition]
                sortedList[minPosition] = temp
            print("-------------")
            for i in sortedList:
                print(i)
            print("-------------")

    # Uses selection sort to sort names of groups alphabetically
    def sortGroup(self):
        sortedList = []
        item = self.head
        if item is None:
            print("--------------------------")
            print("Library is currently empty")
            print("--------------------------")
        else:
            while item.getNext() is not None:
                sortedList.append(item.getCurrent().getGroup())
                item = item.getNext()
            sortedList.append(item.getCurrent().getGroup())
            for i in range(len(sortedList)):

                # Find the minimum element in remaining
                minPosition = i

                for j in range(i + 1, len(sortedList)):
                    if sortedList[minPosition] > sortedList[j]:
                        minPosition = j

                # Swap the found minimum element with minPosition
                temp = sortedList[i]
                sortedList[i] = sortedList[minPosition]
                sortedList[minPosition] = temp
            print("-------------")
            for i in sortedList:
                print(i)
            print("-------------")

    # Uses selection sort to sort genres of songs alphabetically
    def sortGenre(self):
        sortedList = []
        item = self.head
        if item is None:
            print("--------------------------")
            print("Library is currently empty")
            print("--------------------------")
        else:
            while item.getNext() is not None:
                sortedList.append(item.getCurrent().getGenre())
                item = item.getNext()
            sortedList.append(item.getCurrent().getGenre())
            for i in range(len(sortedList)):

                # Find the minimum element in remaining
                minPosition = i

                for j in range(i + 1, len(sortedList)):
                    if sortedList[minPosition] > sortedList[j]:
                        minPosition = j

                # Swap the found minimum element with minPosition
                temp = sortedList[i]
                sortedList[i] = sortedList[minPosition]
                sortedList[minPosition] = temp
            print("-------------")
            for i in sortedList:
                print(i)
            print("-------------")

    #Method that loops through the linked list nad saves each item to the CSV file
    def saveCSV(self):
        item = self.head
        with open("songs.csv", 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            while item.getNext() is not None:
                csv_writer.writerow([str(item.getCurrent().getName()), str(item.getCurrent().getGroup()), str(item.getCurrent().getGenre()), str(item.getCurrent().getPrice()), str(item.getCurrent().getDate()), str(item.getCurrent().getId())])
                item = item.getNext()
            csv_writer.writerow([str(item.getCurrent().getName()), str(item.getCurrent().getGroup()), str(item.getCurrent().getGenre()), str(item.getCurrent().getPrice()), str(item.getCurrent().getDate()), str(item.getCurrent().getId())])

    #Method that loops through the CSV file and re adds everything back to the linked list
    def loadCSV(self):
        with open("songs.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                name = row[0]
                group = row[1]
                genre = row[2]
                price = row[3]
                date = row[4]
                id = row[5]
                song = Tune(name, group, genre, price, date, id)
                listElement = LinkedList(None, None, song)
                self.addToEnd(listElement)


if __name__ == '__main__':
    main = Main()
    main.loadCSV()
    main.menu()

