import csv

# test database 'address_book_one.csv'

"""
The Book class takes a filename at creation, opens that file and then reads it into a list. Each item in that list is 
then converted to an Entry class object. Book ultimately is an object that holds entry objects in self.data. 
"""


class Book:
    def __init__(self, filename='address_book_one.csv'):
        # not sure if filename ever needs to be used later, but it feels better to write this out.
        self.filename = filename
        # This empty list will be filled with list items
        self.data = []
        # opens "self.filename" in read only format in Universal newline mode.
        with open(self.filename, 'rbU') as csvfile:
            my_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in my_csv:
                self.data.append(row)

        # At this point data is a list of list objects read from the original file

        # self.headline isn't useful yet, but it will be when I impliment looking up specific data about an entry.
        # self.headline = {0 : 'First_Name', 1: 'Last_Name', 2:'Street_Address', 3:'City', 4: 'State', 5:'Zip', 6:'Phone_Number', 7:'Email'}

        # The below process converts each list within self.data into an Entry object.
        entries = []
        for line_of_data in self.data:
            this_entry = Entry(line_of_data)
            entries.append(this_entry)
        self.data = entries

    # unsurprisingly, this updates the file with any changes that have been made to the active Book
    def update_book(self):
        with open(self.filename, 'wb') as csvfile:
            my_csv = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for value in range(len(self.data)):
                my_csv.writerow((self.data[value]).Raw_Entry)

    # This adds a new contact to the currently active Book
    def add_contact(self):
        # collects the necissary information for the entry object
        f_n = raw_input("Enter First Name: ")
        l_n = raw_input("Enter Last Name: ")
        full_ad = raw_input("Enter Street Address: ")
        city = raw_input("Enter City: ")
        state = raw_input("Enter State: ")
        zipcode = raw_input("Enter Zip Code: ")
        telep = raw_input("Enter Phone Number: ")
        email = raw_input("Enter e-mail: ")
        # puts all of the above datapoints in the right order
        data_entry = [f_n, l_n, full_ad, city, state, zipcode, telep, email]
        # converts the new information into an Entry object
        entry_to_add = Entry(data_entry)
        # adds the Entry object to the currently active Book.
        self.data.append(entry_to_add)

    def address_from_full_name(self):
        search_term = input("Please Enter the Full Name of the desired Contact")
        found = True
        for datapoint in self.data:
            found = False
            if datapoint.Full_Name == search_term:
                print datapoint.Full_Address
                found = True
                break
        if found == False:
            print("error, no such name found. Returning to Main Menu.")


# The entry class objects make up Book objects and contain a parsed version of the data from the csv file.
class Entry:
    def __init__(self, data_line):
        self.Raw_Entry = data_line
        self.First_Name = data_line[0]
        self.Last_Name = data_line[1]
        self.Street_Address = data_line[2]
        self.City = data_line[3]
        self.State = data_line[4]
        self.Zip = data_line[5]
        self.Phone_Number = data_line[6]
        self.Email = data_line[7]
        # below this point, I combine the above parsed data into slightly more consumable peices.
        self.Full_Address = self.Street_Address + " " + self.City + ", " + self.State + " " + self.Zip
        self.Full_Name = self.First_Name + " " + self.Last_Name
        self.Contact_Info = [self.Phone_Number, self.Email]

    # it's not the most beautiful but it is
    def __repr__(self):
        return str(self.Raw_Entry)


# I have this outside of the body of the program for testing purposes.
def mainloop():
    invalid_entry_count = 0
    while True:
        if invalid_entry_count > 3:
            print("I'm sorry, there appears to be an unspecified error between the keyboard and chair.")
            break
        print("Please select an option.")
        print("1. list contacts and contact information.")
        print("2. add a contact to the directory.")
        print("3. find an address given a full name.")
        print("4. Exit")

        choice = raw_input("Please enter a number corresponding to your choice: ")
        if choice == '1':
            for entry in mybook.data:
                print entry
                print("")
        elif choice == '2':
            mybook.add_contact()
            mybook.update_book()
            print("Directory updated")
        elif choice == '3':
            mybook.address_from_full_name()

        elif choice == '4':
            print("Quitting...")
            break
        else:
            print("Invalid Entry. Please try Again.")
            print(" ")
            invalid_entry_count += 1

    print("Thank you for using the directory. Goodbye.")


mybook = Book()
print("Thanks for taking a look at this project. It's very simple right now. Very basic UI.")
print("The idea is to create an updatable book of contacts in a csv file.")

mainloop()
