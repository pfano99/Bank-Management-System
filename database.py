import sqlite3

dbase = sqlite3.connect("banking_sytem.db")

def create_tables():

      dbase.execute(""" CREATE TABLE IF NOT EXISTS personal_information(
            id_number VARCHAR PRIMARY KEY NOT NULL,
            user_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            gender TEXT NOT NULL,
            cell_phone TEXT NOT NULL,
            user_name TEXT NOT NULL)""")
      
      dbase.execute(""" CREATE TABLE IF NOT EXISTS login_table(
            user_name TEXT PRIMARY KEY NOT NULL,
             user_password TEXT NOT NULL
      )""")

      dbase.execute(""" CREATE TABLE IF NOT EXISTS debit_account(
            account_number VARCHAR PRIMARY KEY NOT NULL,
            user_name TEXT NOT NULL,
            amount INT NOT NULL
      )""")

      dbase.execute(""" CREATE TABLE IF NOT EXISTS credit_account(
            account_number VARCHAR PRIMARY KEY NOT NULL,
            user_name TEXT NOT NULL,
            amount INT NOT NULL
      )""")

      dbase.execute(""" CREATE TABLE IF NOT EXISTS savings_account(
            account_number VARCHAR PRIMARY KEY NOT NULL,
            user_name TEXT NOT NULL,
            amount INT NOT NULL
      )""")

def inserting_data():
      dbase.execute(""" INSERT INTO personal_information(id_number, first_name, last_name, email, gender, cell_phone) VALUES(?, ?, ?, ?, ?, ?) """,
            ("1233455", "pfano", "sigama", "pfanosigama", "male", "12344567") )
      dbase.commit()
      dbase.execute(""" INSERT INTO login_table(user_name, user_password) VALUES(?, ?) """, ())
      dbase.commit()

##################### ADMIN USER #############################
def add_new_user(id_number, first_name, last_name, email, gender, cell_phone):

      dbase.execute(""" INSERT INTO personal_information(*) VALUES(?, ?, ?, ?, ?, ?) """,
            (id_number, first_name, last_name, email, gender, cell_phone) )
      dbase.commit()
      

def delete_user(id_number):
      dbase.execute(""" DELETE FROM personal_information WHERE id_number = (?) """, (id_number))

def modify_user_info():
      pass
def close_database():
      dbase.close()

# create_tables()
# inserting_data()
# dbase.close()

if __name__ == "_main__":
      create_tables()
      close_database()
      dbase.close()
