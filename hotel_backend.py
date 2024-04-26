import sqlite3

#_________________query str__________________#

# query str for user_tbl#
CREATE_USER_TBL = "CREATE TABLE IF NOT EXISTS user_tbl(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, lastname TEXT, username TEXT UNIQUE, password TEXT, hotel text)"
INSERT_INTO_USER_TBL = "INSERT INTO user_tbl(username, password, hotel) VALUES(?,?,?)"
SELECT_LOGIN = "SELECT username, password FROM user_tbl WHERE username = ? and password = ?"

# query str for guest_tbl #
CREATE_GUEST_TBL = "CREATE TABLE IF NOT EXISTS guest_tbl(guest_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, lastname TEXT, national_id INTEGER, gender text, nationality TEXT, phone_number TEXT)"
INSERT_INTO_GUEST_TBL = "INSERT INTO guest_tbl(name, lastname, national_id, gender, nationality, phone_number) VALUES(?,?,?,?,?,?)"
SELECT_GUESTS = "SELECT * FROM guest_tbl"
SELECT_GUESTS_WO_ID = "SELECT name, lastname, national_id, gender, nationality, phone_number FROM guest_tbl"
SEARCH_GUEST_ID = "SELECT * FROM guest_tbl WHERE guest_id = ?"
SEARCH_GUEST_NAME = "SELECT * FROM guest_tbl WHERE name = ?"
SEARCH_GUEST_LASTNAME = "SELECT * FROM guest_tbl WHERE lastname = ?"
SEARCH_GUEST_N_ID = "SELECT * FROM guest_tbl WHERE national_id = ?"
SEARCH_GUEST_GENDER = "SELECT * FROM guest_tbl WHERE gender = ?"
SEARCH_GUEST_PHONE_NUMBER = "SELECT * FROM guest_tbl WHERE phone_number = ?"
SEARCH_GUEST_NATIONALITY = "SELECT * FROM guest_tbl WHERE nationality = ?"
DELETE_GUEST_ID = "DELETE FROM guest_tbl WHERE guest_id = ? "

# query str for previous_guest_tbl #
CREATE_PREVIOUS_GUEST_TBL = "CREATE TABLE IF NOT EXISTS previous_guest_tbl(guest_id INTEGER, name TEXT, lastname TEXT, national_id INTEGER, gender text, nationality TEXT)"


#_______________connect method_______________#

def connection_check():
    return sqlite3.connect("info.db")

#________________query method________________#

def create_table(connection):
    with connection:
        connection.execute(CREATE_USER_TBL)
        connection.execute(CREATE_GUEST_TBL)
        connection.execute(CREATE_PREVIOUS_GUEST_TBL)

def add_user(connection, username, password, hotel):
    with connection:
        connection.execute(INSERT_INTO_USER_TBL, (username, password, hotel))

def select_login(connection, username, password):
    with connection:
        return connection.execute(SELECT_LOGIN, (username, password)).fetchall()
    
def add_guest(connection, name, lastname, national_id, gender, nationality, phone_number):
    with connection:
        connection.execute(INSERT_INTO_GUEST_TBL, (name, lastname, national_id, gender, nationality, phone_number))

def show_guests(connection,columns):
    # based on the given number columns will be selected
    if columns == 7: 
        with connection:
            return connection.execute(SELECT_GUESTS).fetchall()
    elif columns == 6 :
        with connection:
            return connection.execute(SELECT_GUESTS_WO_ID).fetchall()
        
def search_guest(connection, column, item):
    if column == 1:
        with connection:
            return connection.execute(SEARCH_GUEST_NAME, (item,)).fetchall()
    if column == 2:
        with connection:
            return connection.execute(SEARCH_GUEST_LASTNAME, (item,)).fetchall()
    if column == 3:
        with connection:
            return connection.execute(SEARCH_GUEST_N_ID, (item,)).fetchall()
    if column == 4:
        with connection:
            return connection.execute(SEARCH_GUEST_GENDER, (item,)).fetchall()
    if column == 5:
        with connection:
            return connection.execute(SEARCH_GUEST_NATIONALITY, (item,)).fetchall()
    if column == 6:
        with connection:
            return connection.execute(SEARCH_GUEST_PHONE_NUMBER, (item,)).fetchall()
    if column == 7:
        with connection:
            return connection.execute(SEARCH_GUEST_ID, (item,)).fetchall()
        
def delete_guest(connection, guest_id):
    with connection:
        connection.execute(DELETE_GUEST_ID, (guest_id,))
    