
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import databasedemo
import scrapping
import datetime
myapp = Flask(__name__)
myapi = Api(myapp)


#making class for a particular resource
#get and post mthods correpond to get and pot requests
# automaticall mapped by flask_restful
class Hello(Resource):

    def get(self):
        date=datetime.date.today()
        datalist=scrapping.get_jason_data()
        return jsonify({f'{date}':datalist})

    def post(self):
        data = request.get_json()
        return jsonify({'data': data})


class Square(Resource):

    def get(self, num):
        if num % 2 == 0:
            status = "even"
        else:
            status = "odd"

        return jsonify({'square': num**2, 'status': status})


class even_odd(Resource):
    def get(self, num):
        if num % 2 == 0:
            status = "even"
        else:
            status = "odd"
        return jsonify({'value': num, 'status': status})

class share_api(Resource):
    def get(self,date):
        database_obj=databasedemo.main_database("Today_Share_Price_demo",date)
        myconn=database_obj.create_databases()
        mytable_conn=database_obj.create_tables(myconn)
        # print(myconn.list_collection_names())
        print("date = ",date)
        all_data=[]
        for collection in myconn.list_collection_names():
            if collection==date:
                # print("collection =",collection)
                for datalist in database_obj.fetch_from_db(mytable_conn):
                    all_data.append(datalist)
                
        return jsonify({f'{date}':all_data})
                # datalist = database_obj.fetch_from_db(myconn)
             # print(datalist)
class front_end(Resource):
    def get(self):
        pass
    def post(self):
        pass



myapi.add_resource(Hello, '/hello')
myapi.add_resource(even_odd, '/pair/<int:num>')
myapi.add_resource(Square, '/square/<int:num>')
myapi.add_resource(share_api,'/today_share/<string:date>')
if __name__ == "__main__":
    myapp.run(debug=True)
