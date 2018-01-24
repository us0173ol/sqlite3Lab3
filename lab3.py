import sqlite3

def create_db():
    db = sqlite3.connect('chainsaw_juggling_db') # Creates or opens database file
    cur = db.cursor() # Need a cursor object to perform operations

def create_table():
    db = sqlite3.connect('chainsaw_juggling_db') # Creates or opens database file
    cur = db.cursor() # Need a cursor object to perform operations
    # Create a table if not exists...
    cur.execute('create table if not exists recordHolders (RecordHolder text, Country text, NumberOfCatches int)')

    cur.execute('insert into recordHolders values("Aaron Gregg", "Canada", 88)')
    cur.execute('insert into recordHolders values("Chad Taylor", "USA", 78)')

def add_record():
    db = sqlite3.connect('chainsaw_juggling_db') # Creates or opens database file
    cur = db.cursor()
# Ask user for information
    RecordHolder = input('Enter the name of record holder: ')
    Country = input('Enter Country: ')
    NumberOfCatches = int(input('Enter number of catches (as an integer): '))

    # Parameters. Use a ? as a placeholder for data that will be filled in
    # Provide data as a second argument to .execute, as a tuple of values
    cur.execute('insert into recordHolders values (?, ?, ?)', (RecordHolder, Country, NumberOfCatches,))
    db.commit()
def display_table():
    db = sqlite3.connect('chainsaw_juggling_db') # Creates or opens database file
    cur = db.cursor()
    # Fetch and display all data. Results stored in the cursor object
    cur.execute('select * from recordHolders')

    for row in cur:
        print(row)

def save_close():
    db = sqlite3.connect('chainsaw_juggling_db') # Creates or opens database file
    cur = db.cursor()

    db.commit() # Ask the database to save changes!

    db.close()

def search(search_for):
    db = sqlite3.connect('chainsaw_juggling_db') # Creates or opens database file
    cur = db.cursor()

    if search_for == '1':
        name = input('Enter the name you would like to search for: ')
        cur.execute("select * from recordHolders where RecordHolder like '%"+name+"%'")

        for row in cur:
            print(row)

    elif search_for == '2':
        country = input('Enter the country you would like to search for: ')
        cur.execute("select * from recordHolders where Country like '%"+country+"%'")

        for row in cur:
            print(row)

    elif search_for == '3':
        numberOfCatches = int(input('Enter the number of catches you would like to search for: '))
        cur.execute('select * from recordHolders where NumberOfCatches = ?', (numberOfCatches,))

        for row in cur:
            print(row)


def search_choice():

    print('''Search by:
        1. Name
        2. Country
        3. Number of catches
        ''')

    search_for = input('Enter your selection: ')
    return search_for



def main():
    create_db()
    create_table()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = display_choice_options()
        handle_choice(choice)

def update_decision():
    db = sqlite3.connect('chainsaw_juggling_db')
    cur = db.cursor()
    cur.execute('select * from recordHolders')

    for row in cur:
        print(row)

    record = input('Enter the name of the record holder you would like to edit: ')
    cur.execute("select * from recordHolders where RecordHolder like '%"+record+"%'")

    for row in cur:
        print(row)

    print('''
            1. Edit Name
            2. Edit Country
            3. Edit Number of Catches
        ''')

    update_choice = input("Enter Selection: ")


    if update_choice == '1':
        new_name = input('Enter new name: ')
        cur.execute("update recordHolders set RecordHolder ='"+new_name+"'where RecordHolder ='"+record+"'")
        db.commit()
        print('Update Successful')

    elif update_choice == '2':
        new_country = input('Enter new country: ')
        cur.execute("update recordHolders set Country ='"+new_country+"'where RecordHolder ='"+record+"'")
        db.commit()
        print('Update Successful')

    elif update_choice == '3':
        new_numberOfCatches = input('Enter new number of catches: ')
        cur.execute("update recordHolders set NumberOfCatches ='"+new_numberOfCatches+"'where RecordHolder ='"+record+"'")
        db.commit()
        print('Update Successful')
    else:
        print('Make valid selection ')

def delete_record():
    db = sqlite3.connect('chainsaw_juggling_db')
    cur = db.cursor()
    cur.execute('select * from recordHolders')

    delete = input('Enter the name of the record holder you would like to delete: ')
    cur.execute("delete from recordHolders where RecordHolder ='"+delete+"'")
    db.commit()
    print(delete, 'was successfuly deleted from database ')

def handle_choice(choice):


        if choice == '1':
            display_table()

        elif choice == '2':
            add_record()

        elif choice == '3':
            search_for = search_choice()
            search(search_for)

        elif choice == '4':
            update_decision()

        elif choice == '5':
            delete_record()

        elif choice =='q' or 'Q':
            quit()

def quit():
    save_close()


def display_choice_options():
    print('''
            1. Display table
            2. Add new record
            3. Search records
            4. Edit records
            5. Delete records
            q. Quit
        ''')
    choice = input('Enter your selection: ')
    return choice



main()

# display_table()
# add_record()
