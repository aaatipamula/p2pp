import sqlite3
from sqlite3 import Error
from dataclasses import dataclass

## ADD FUNCTIONS TO CONVERT TUPLES RETURNED BY SQL TO USER AND POST DATACLASSES
## add function to convert list of tuple to list of users/posts

class InvalidParameterFormat(RuntimeError):
    pass

@dataclass(frozen=True)
class User:
    uid: str = ''
    email: str = ''
    phone: str = ''
    credit: int = 0
    community: str = ''
    name: str = ''

usr = tuple[str, str, int, str, str]

@dataclass(frozen=True)
class Post:
    pid: str = ''
    uid: str = ''
    time: str = ''
    duration: int = 0
    item: str = ''
    type: str = ''
    tags: str = ''

post = tuple[str, str, str, int, str, str ,str]

class Database():
    # Connect database
    def __init__(self, db):
        try:
            self.conn = sqlite3.connect(db, check_same_thread=False)
            print(sqlite3.version)
        except Error as e:
            print(e)


    def create_table(self, table_info: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(table_info)
            print('Added table')
        except Error as e:
            print(e)
    
    def create_user(self, data: usr):

        '''
        The *data* tuple must be formatted as the following: 

        data = (uid,email,phone,credit,community,name)

        Not doing so will result in a InvalidParameterFormat error being raised
        '''

        # add check function that checks the data slightly more throughly
        if len(data) < 6 or len(data) > 6:
            raise InvalidParameterFormat('Provided tuple was either too large or small.')

        sql = '''INSERT INTO users(uid,email,phone,credit,community,name)
              VALUES(?,?,?,?,?);'''

        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()

        print('User created')
        # return user object instead?
        return cursor.lastrowid
    
    def create_post(self, data: tuple):

        '''
        The *data* tuple must be formatted as the following: 

        data = (pid,uid,time,duration,item,type,tags)

        Not doing so will result in a InvalidParameterFormat error being raised.
        '''

        # add check function that checks the data slightly more throughly
        if len(data) < 7 or len(data) > 7:
            raise InvalidParameterFormat('Provided tuple was either too large or small.')

        sql = '''INSERT INTO daisy_hill(pid,uid,time,duration,item,type,tags)
              VALUES(?,?,?,?,?,?);'''

        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()

        print(f'Post with pid{data[0]} created')
        # Perhaps return a post object instead?
        return cursor.lastrowid
    
    def delete_post(self, post: Post):
        # since pid will be a hash of the time and uid add params to search for the post using those two items

        # pseudo code:
        # if post.pid == '' then try hash(post.uid, post.time)

        sql = 'DELETE FROM daisy_hill WHERE pid=?;'

        cursor = self.conn.cursor()
        cursor.execute(sql, (post.pid,))
        self.conn.commit()

        print(f'Deleted post with ID: {post.pid}')
        return post
    
    def delete_usr(self, user: User):
        # has to have the whole user object, or construct with just the uid ig lol
        cursor = self.conn.cursor()
        cursor.execute(f'DELETE FROM users WHERE uid=?;', (user.uid,))
        self.conn.commit()

        print(f'Deleted post with uid: {user.uid}')
        return user
    
    def select_all_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users;")
        # wrap fetchall in function to convert list of tuple into a list of classes
        rows = cur.fetchall()
        return rows
    
    def select_post_by_community(self, community: str):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM ?;", (community,))
        # wrap fetchall in function to convert list of tuple into a list of classes
        rows = cur.fetchall()
        return rows

    def select_one_user(self, email: str):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE uid=?;", (email,))
        # convert to user class
        usr_num = cur.fetchone()
        return usr_num

    def __delete_all_users(self):
        sql = 'DELETE FROM users;'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.con.commit()
        print('All users deleted')
    
    def __delete_all_posts(self, community: str):
        sql = 'DELETE FROM daisy_hill;'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.con.commit()
        print('All posts deleted;')

    # def get_email_to_id(self, email: str):
    #     cur = self.conn.cursor()
    #     cur.execute("SELECT * FROM users")
    #     rows = cur.fetchall()
    #     for index, row in enumerate(rows):
    #         if row[0] == email:
    #             return index+1

if __name__ == '__main__':
    dbFile = r"./database.db"
    db = Database(dbFile)
    #user = ('SampUser@asdf.com', '4/15/23 3:14', 80, 'daisy_hill', 'OMARIO')
    #db.create_user(user)
    #usr_email = "'SampelUser@asdf.com'"
    #db.delete_usr(usr_email)
    # user_id = 1
    # db.delete_post(user_id)

    users_table = """ CREATE TABLE IF NOT EXISTS users (
                        uid text PRIMARY KEY,
                        email text NOT NULL,
                        phone text NOT NULL,
                        credit integer NOT NULL,
                        community text NOT NULL,
                        name text NOT NULL
                    ); """

    daisy_hill = """ CREATE TABLE IF NOT EXISTS daisy_hill (
                        pid text PRIMARY KEY,
                        uid text NOT NULL,
                        time text NOT NULL,
                        duration integer NOT NULL,
                        item text NOT NULL,
                        type text NOT NULL,
                        tags text NOT NULL
                    );"""

    db.create_table(users_table)
    db.create_table(daisy_hill)

