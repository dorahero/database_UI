from app import db
import pandas as pd
from app.tools.process import query_to_dict

def checkUser(username, password):
    sql_cmd = """
                select user, password
                from account
    """
    user_data = db.engine.execute(sql_cmd).fetchall()
    checker = False
    for u in user_data:
        if u[0] == username and u[1] == password:
            checker = True
    return checker

def getData(table_name, lot_id, wafar_id):
    sql_cmd = f"""
                select *
                from {table_name} where lot_id = {lot_id} and wafar_id = {wafar_id}
    """
    query_data = db.engine.execute(sql_cmd).fetchall()
    print(query_data.column_descriptions)
    # data = query_to_dict(query_data)
    return data