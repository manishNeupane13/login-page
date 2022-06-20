import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#database connection
mydb = myclient['Customer_detail']
# connection to table
mycol = mydb['General_info']


def inser_into_db(user_login_info):
    # inserting inside the mongodb
    mycol.insert_many(user_login_info)
    print("Insertion is sucessful.")


def fetch_from_db():
    data = mycol.find({}, {'_id': 0})
    # 'S.N.': 1, 'Traded Companies': 1, 'No. Of Transaction': 1, 'Max Price': 1,
    #                   'Min Price': 1, 'Closing Price': 1, 'Traded Shares': 1, 'Amount': 1, 'Previous Closing': 1, 'Difference Rs.': 1})

    return data


if __name__ == "__main__":
    inser_into_db()
    fetch_from_db()
