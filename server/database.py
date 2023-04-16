import sqlite3
from sqlite3 import Error

class Database():
    def __init__(self, db):
        #Connects the database
        self.conn = None 
        try:
            self.conn = sqlite3.connect(db)
            print(sqlite3.version)
        except Error as e:
            print(e)
    def create_table(self, table_info):
        try:
            cursor = self.conn.cursor()
            cursor.execute(table_info)
            print('Added table')
        except Error as e:
            print(e)
    
    def create_user(self, data):
        sql = '''INSERT INTO users(email,phone_number,credit_score,
                    community,name)
              VALUES(?,?,?,?,?) '''
        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()
        print('User created')
        return cursor.lastrowid
    
    def create_post(self, data):
        sql = '''INSERT INTO daisy_hill(email,time,duration,
                    item,type,tags)
              VALUES(?,?,?,?,?,?) '''
        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()
        print('Post created')
        return cursor.lastrowid
    
    def delete_post(self, id):
        sql = 'DELETE FROM daisy_hill WHERE email=?'
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        self.conn.commit()
        print(f'Deleted post with ID: {id}')
    
    def delete_usr(self, email):
        cursor = self.conn.cursor()
        cursor.execute(f'DELETE FROM users WHERE email={email}')
        self.conn.commit()
        print(f'Deleted post with email: {email}')
    
    def delete_all_users(self):
        sql = 'DELETE FROM users'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.con.commit()
        print('All users deleted')
    
    def delete_all_posts(self):
        sql = 'DELETE FROM daisy_hill'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.con.commit()
        print('All posts deleted')
    
    def select_all_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        return rows
    
    def select_all_posts(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM daisy_hill")
        rows = cur.fetchall()
        return rows

    def select_one_user(self, email):
        cur = self.conn.cursor()
        cur.execute(f"SELECT phone_number,community FROM users WHERE email={email}")
        usr_num = cur.fetchone()
        return usr_num

    def get_email_to_id(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for index, row in enumerate(rows):
            if row[0] == email:
                return index+1
if __name__ == '__main__':
    db_file_path = r"C:\Users\arnav\PycharmProjects\spare\database\database.db"
    db = Database(db_file_path)
    
    #usr_email = "'SampelUser@asdf.com'"
    #db.delete_usr(usr_email)

    print(db.get_email_to_id('SampUser@asdf.com'))

    '''users_table = """ CREATE TABLE IF NOT EXISTS users (
                        email text PRIMARY KEY,
                        phone_number text NOT NULL,
                        credit_score integer NOT NULL,
                        community text NOT NULL,
                        name text NOT NULL
                    ); """
    daisy_hill = """ CREATE TABLE IF NOT EXISTS daisy_hill (
                        email text PRIMARY KEY,
                        time text NOT NULL,
                        duration integer NOT NULL,
                        item text NOT NULL,
                        type text NOT NULL,
                        tags text NOT NULL
                    );"""
    db.create_table(users_table)
    db.create_table(daisy_hill)'''