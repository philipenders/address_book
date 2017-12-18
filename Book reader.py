import csv


# test database 'address_book_one.csv'

class Book:
    def __init__(self, filename='address_book_one.csv'):
        self.filename = filename
        data = []
        with open(self.filename, 'rwbU') as csvfile:
            my_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
            for value, row in enumerate(my_csv):
                data.append(row)

        self.headline = {0 : 'First_Name', 1: 'Last_Name', 2:'Street_Address', 3:'City', 4: 'State', 5:'Zip', 6:'Phone_Number', 7:'Email'}
        self.data = data

        entries = []
        for line_of_data in self.data:
            this_entry = Entry(line_of_data)
            entries.append(this_entry)
        self.data = entries

    def update_book(self):
        with open(self.filename, 'wb') as csvfile:
            my_csv = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for value in range(len(self.data)):
                my_csv.writerow((self.data[value]).Raw_Entry)

    def add_contact(self):
        f_n = raw_input("Enter First Name: ")
        l_n = raw_input("Enter Last Name: ")
        full_ad = raw_input("Enter Street Address: ")
        city = raw_input("Enter City: ")
        state = raw_input("Enter State: ")
        zipcode = raw_input("Enter Zip Code: ")
        telep = raw_input("Enter Phone Number: ")
        email = raw_input("Enter e-mail: ")
        data_entry = [f_n, l_n, full_ad, city, state, zipcode, telep, email]
        entry_to_add = Entry(data_entry)
        self.data.append(entry_to_add)


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
        self.Full_Address = self.Street_Address + " " + self.City + ", " + self.State + " " + self.Zip
        self.Full_Name = self.First_Name + " " + self.Last_Name
        self.Contact_Info = [self.Phone_Number, self.Email]
    def __repr__(self):
        return str(self.Raw_Entry)

def mainloop():
    while True:
        print("Please select an option.")
        print("1. list contacts and contact information.")
        print("2. add a contact to the directory.")
        print("3. Exit")

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
            print("Quitting...")
            break
        else:
            print("Invalid Entry. Please try Again.")
            print(" ")

    print("Thank you for using the directory. Goodbye.")

mybook = Book()

mainloop()
