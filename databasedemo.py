import pymongo
import datetime
import scrapping


class main_database:
    def __init__(self, database_name, table_name):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database_name = database_name
        self.table_name = table_name

    def db_connection():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # connecting to database

    def create_databases(self):
        return self.conn[self.database_name]
    # connection to table

    def create_tables(self, mydb_conn):
        return mydb_conn[self.table_name]
    # set new db name

    def set_newdb(self, database_name):
        self.database_name = database_name
    # set new table_name

    def set_newtable(self, table_name):
        self.table_name = table_name

    def insert_into_db(self, mytable_conn, data_list):
        return mytable_conn.insert_many(data_list)

    def fetch_from_db(self, mytable_conn):
        return mytable_conn.find({}, {'_id': 0})


if __name__ == "__main__":
    database_name = "Today_Share_Price_demo"
    #  input("Enter the  name of the database schema :: ")
    table_name = str(datetime.datetime.now())

    # input("Enter the name of the Collection :: ")
    database_obj = main_database(database_name, table_name)
    loop = True
    # while True:
    # print("press \n1. To Create Database Schema \n2. To create Collection \n3. To Insert Inside Database")
    # menu_val=input()
    mydb_conn = database_obj.create_databases()
    collection1 = mydb_conn.list_collection_names()
    for collect in collection1:
        print(collect)
    mytable_conn = database_obj.create_tables(mydb_conn)
    
    # print(mydb_conn, mytable_conn)
    # database connection
    # for page_number in range(1,12):
    # page_number = int(input("Enter the page number of transaction :: "))
    # table_contents = scrapping.request_method(page_number)
    # heading_list = scrapping.get_heading_list(table_contents)
    # table_data = scrapping.get_table_data(table_contents)
    # data_list = scrapping.get_jason_file(heading_list,table_data)
    data_list = scrapping.get_jason_data()
    print(data_list)
    insert_id = database_obj.insert_into_db(mytable_conn, data_list)
    # for x in database_obj.fetch_from_db(mytable_conn):
    #     print(x)
    #  mytable_conn.insert_one(data_list)
