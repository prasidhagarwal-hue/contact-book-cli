from contact_book import Contactbook

def main():
    book = Contactbook()

    while True:
        print("1. Add Contact: ")
        print("2. View All Contacts: ")
        print("3. Search Contact: ")
        print("4. Delete Contact: ")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name:  ")
            phone = input("Enter phone number:")
            email = input("enter email:")
            book.add_contact(name, phone,email)
        elif choice == '2':
            book.view_all()
        elif choice == '3':
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == '5':
            print("Exited")
            break  

if __name__ == "__main__":
    main()
    