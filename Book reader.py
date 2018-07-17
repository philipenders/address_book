import csv

# test database 'address_book_one.csv'

"""
The Book class takes a filename at creation, opens that file and then reads it into a list.
Each item in that list is then converted to an Entry class object.
Book ultimately is an object that holds entry objects in self.data. 
"""


# The book class interfaces with the csv file
class Book:
    def __init__(self, filename='address_book_one.csv'):
        # It feels better to have filename be part of the book class
        self.filename = filename
        # This empty list will be filled with list objects initially
        self.data = []
        # opens "self.filename" in read only format in Universal newline mode.
        with open(self.filename, 'rbU') as csvfile:
            my_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in my_csv:
                self.data.append(row)

        # At this point self.data is a list of list objects read from the original file

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


# The entry class objects make up Book objects and contain a line of data from the csv
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
        # below this point, I combine the above parsed data into slightly more useful consumable peices.
        self.Full_Address = self.Street_Address + " " + self.City + ", " + self.State + " " + self.Zip
        self.Full_Name = self.First_Name + " " + self.Last_Name
        self.Contact_Info = [self.Phone_Number, self.Email]

    # it's not the most beautiful but it is
    def __repr__(self):
        return str(self.Raw_Entry)

    # The following three methods check if certain input information matches the Entry
    def does_match_full_name(self, full_name):
        return (self.Full_Name == full_name)

    def does_match_zip(self, zip):
        return (self.Zip == zip)

    def does_match_state(self, state):
        return (self.State == state)

    def does_match_last_name(self, l_name):
        return (self.Last_Name == l_name)


# _______________________________________

# The address book UI contains all text based control options for the Address Book.

class AddressBookUI():
    def __init__(self, name="Default UI"):
        self.name = name

    def __repr__(self):
        return self.name

    # this function takes the "book_in_question", and prints each entry contained therein
    def read_fullbook(self, book_in_question):
        for entry in book_in_question.data:
            print entry
            print("")

    # This adds a new contact to the currently active Book
    def add_contact_to_book(self, book_in_question):
        # collects the necissary information for the new Entry object
        f_n = raw_input("Enter First Name: ")
        l_n = raw_input("Enter Last Name: ")
        street_ad = raw_input("Enter Street Address: ")
        city = raw_input("Enter City: ")
        state = raw_input("Enter State: ")
        zipcode = raw_input("Enter Zip Code: ")
        telep = raw_input("Enter Phone Number: ")
        email = raw_input("Enter e-mail: ")
        # puts all of the above datapoints in the right order
        data_entry = [f_n, l_n, street_ad, city, state, zipcode, telep, email]
        # converts the new information into an Entry object
        entry_to_add = Entry(data_entry)
        # adds the Entry object to the currently active Book.
        book_in_question.data.append(entry_to_add)
        yes_or_no = raw_input("Do you want to save changes to the csv file? please enter 'y' or 'n'")
        yes_or_no = yes_or_no.upper()
        if yes_or_no == 'Y':
            book_in_question.update_book()
            print("Understood, csv file updated.")
        elif yes_or_no == 'N':
            print(
                "Understood, I'll hold off on updating the csv file. You'll still be able to save later if you'd like.")
        else:
            print("I'm sorry, i didn't understand the input. If you want to save to the csv, "
                  "please select 'U' as your choice in the main menu")
        print("")
        print("Working Directory Updated")

    def find_address_from_full_name(self, book_in_question):
        search_term = raw_input("Please Enter the Full Name of the desired Contact")
        match_count = 0
        for Entry in book_in_question.data:
            if Entry.does_match_full_name(search_term):
                print Entry.Full_Address
                match_count += 1
        if match_count == 0:
            print ("I'm sorry, no matches found for '" + search_term + "'")
            return False, search_term
        return True, search_term

    def find_all_names_in_zip(self, book_in_question):
        search_term = raw_input("Please Enter the zip code you'd like to search for: ")
        match_count = 0
        for entry in book_in_question.data:
            if entry.does_match_zip(search_term):
                print ("")
                print ("Addresses in zip code " + str(search_term) +":")
                print (entry.Full_Name + " at : " + str(entry.Full_Address))
                match_count += 1
        if match_count == 0:
            return match_count, search_term
        return match_count, search_term

    def load_book(self, book_title='address_book_one.csv'):
        return Book(book_title)

    def quitting(self):
        print("")
        print ("Now closing program")
        print("...")
        print("Quitting")
        print("...")
        print("")

    def main_UI(self):
        print("Thanks for taking a look at this project. It's very simple right now, "
              "with limited function.")
        print("The idea is to create an updatable book of contacts in a csv file.")
        print("....")
        print("")

        print("Welcome to the program, I appreciate you trying out my address book.")
        current_book = self.load_book()
        invalid_entry_count = 0
        while True:
            if invalid_entry_count > 3:
                print("I'm sorry, there appears to be an unspecified error between the keyboard and chair.")
                break
            print("Please select an option.")
            print("1. list contacts and contact information.")
            print("2. add a contact to the directory.")
            print("3. find an address given a full name.")
            print("4. find all contacts in a zip code.")

            # TODO make the above into a general "Search" function

            print("5. Exit")
            print("U. update the csv file for the current book.")

            # TODO add option to update or correct information on an existing contact

            choice = raw_input("Please enter a number corresponding to your choice: ")
            if choice == '1':
                self.read_fullbook(current_book)

            # Adds a contact to current_book and updates the csv file when uncommented
            elif choice == '2':
                self.add_contact_to_book(current_book)
                # current_book.update_book() #<--remove this in a live program to actually update the book

            # let's the user search the address book and add a contact if there is no match
            # TODO add functionality so users don't have to re-enter the name once typed.
            elif choice == '3':
                found, full_name = self.find_address_from_full_name(current_book)
                if not found:
                    selection = raw_input("Would you like to add their information to the directory?,"
                                          "enter '1' for 'yes'. alternatively enter '2' for 'no'.")
                    if selection == '1':
                        self.add_contact_to_book(current_book)
                    if selection == '2':
                        print ("Alright! So sorry we couldn't find that person in the directory.")
                print("")

            # choice four should let a user print any matching contacts to the screen
            # TODO see above - Add general search functionality
            elif choice == '4':
                number_of_matches, returned_zip = self.find_all_names_in_zip(current_book)
                if number_of_matches == 0:
                    print("")
                    print ("I'm sorry, no matches found for '" + returned_zip + "'")
                else:
                    print("")
                    print(str(number_of_matches) + " found in zip code: " + str(returned_zip))
                print("")


            # calls the quitting() method to provide exit scripting
            elif choice == '5':
                self.quitting()
                break

            elif choice == 'u' or "U":
                yes_or_no = raw_input("Do you want to save changes to the csv file? please enter 'y' or 'n'")
                yes_or_no = yes_or_no.upper()
                if yes_or_no == 'Y':
                    current_book.update_book()
                    print("Understood, csv file updated.")
                elif yes_or_no == 'N':
                    print("Understood, I'll hold off on updating the csv file.")
                else:
                    print("I'm sorry, i didn't understand the input. exiting saving menu")
                print("")

            else:
                print("Invalid Entry. Please try Again.")
                print(" ")
                invalid_entry_count += 1

        print("Thank you for using the directory. Goodbye.")


AB_UI = AddressBookUI('AB_UI')

AB_UI.main_UI()
