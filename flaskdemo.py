import datetime
import databasedemo
from flask import Flask, request, jsonify
from flask import *
app = Flask(__name__)


@app.route('/signin/<string:date>', methods=['GET', 'POST'])
def login(date):
    if request.method == 'POST':
        username = request.form['uname']
        pasword = request.form['psw']
        data = databasedemo
        for x in data:
            if x['Email Address'] == username and x['Password'] == pasword:
                print("match found")
                # return render_template(f'http://127.0.0.1:5000//share/{date}')
            # else:
                # return render_template('loginpage.html')

    return render_template('loginpage.html')


@app.route('/signup', methods=['GET', 'POST'])
def register():
    register_list = []

    if request.method == 'POST':
        email_address = request.form['email']
        first_name = request.form['fname']
        last_name = request.form['lname']
        contact_number = request.form['number']
        user_password = request.form['psw']
        conform_password = request.form['cpsw']
        register_list.append({'Email Address': email_address, 'First name': first_name,
                             'Last Name': last_name, 'Contact Number': contact_number, 'Password': user_password})

        print(register_list)
        writeintodatabase.inser_into_db(register_list)

    return render_template('newregister.html')
    # return 'hello world'


@app.route('/share/<string:date>', methods=['GET', 'POST'])
def sharedata(date):
    database_obj = databasedemo.main_database("Today_Share_Price_demo", date)
    myconn = database_obj.create_databases()
    mytable_conn = database_obj.create_tables(myconn)
     # print(myconn.list_collection_names())
    print("date = ", date)
    all_data = []
    for collection in myconn.list_collection_names():
            if collection == date:
                print("collection =",collection)
                for datalist in database_obj.fetch_from_db(mytable_conn):
                    all_data.append(datalist)

    return jsonify({f'{date}': all_data})
    # key_value =""
    # # print(sharedata)
    # # if request.method == "POST":
    # sharedata = writeintodatabase.fetch_from_db()
    # for list_data in sharedata:
    #      key_value = (list_data.keys())
    # return render_template('display.html', result_key=key_value, sharedata1=writeintodatabase.fetch_from_db())
    # return render_template("display.html")

if __name__ == "__main__":
    app.run(debug=True)
