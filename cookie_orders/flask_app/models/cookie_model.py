from flask_app.config.mysqlconnection import connectToMySQL
import pprint
from flask import flash

db = 'cookie_orders'

class Cookie:
    def __init__(self,data):
        self.id=  data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.boxes = data['boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 

    @classmethod
    def save(cls,data):
        query = "INSERT INTO cookies (name,cookie_type,boxes) VALUES (%(name)s, %(cookie_type)s,%(boxes)s)"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM cookies'
        results = connectToMySQL(db).query_db(query)
        all_orders = []
        pprint.pprint(results)
        for cookie in results:
            all_orders.append(cls(cookie))
        return all_orders

    @classmethod
    def get_one_order(cls,data):
        query = "SELECT * from cookies where id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update_order(cls,data,id):
        query = f'''
        UPDATE cookies 
        set name = %(name)s, cookie_type = %(cookie_type)s, boxes = %(boxes)s
        WHERE id ={id}
        '''
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def cookie_validator(cookie):
        is_valid = True
        if len(cookie['name']) < 2:
            flash('Your name needs to be at least 2 characters long')
            is_valid = False
        if len(cookie['cookie_type']) < 2:
            flash('Your Cookie Type needs to be at least 2 characters long')
            is_valid = False
        if int(cookie ['boxes']) <= 0:
            flash('Please choose an appropriate numebr of boxes')
            is_valid = False
        return is_valid

