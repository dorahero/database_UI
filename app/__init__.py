from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from app.utils import setting
from flask import request, render_template

# from werkzeug.contrib.fixers import ProxyFix

sql_app = Flask(__name__)
# sql_app.wsgi_app = ProxyFix(sql_app.wsgi_app)
sql_app.config.from_object(setting) 

api = Api(app = sql_app,
          version="1.0"  ,
          title="Winbond Data Team Apis",
          description="Manage names of various apps api of the application"          
)

# Register namespace
ns_DataBase_SQL = api.namespace('DataBase_SQL', description='read database')

# Db connector
db = SQLAlchemy(sql_app)


from app.models.databaseSQLmodel import checkUser, getData
@sql_app.route('/login', methods=['GET', 'POST'])
def login():
    request_method = request.method
    if request.method == 'GET':
        return render_template('start.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if checkUser(username, password):
            return render_template('query.html',
                                request_method=request_method,
                                username=username,
                                password=password
                                )
        else:
            return render_template('start.html',
                    request_method='GET'
                    )

@sql_app.route('/DN21/data', methods=['GET', 'POST'])
def queryData():
    request_method = request.method
    if request.method == 'GET':
        return render_template('start.html')
    elif request.method == 'POST':
        table_name = request.form.get('table_name')
        lot_id = request.form.get('lot_id')
        wafar_id = request.form.get('wafar_id')
        print(getData(table_name, lot_id, wafar_id))
        return render_template('result.html',
                            request_method=request_method,
                            table_name=table_name,
                            lot_id=lot_id,
                            wafar_id=wafar_id
                            )


# from app.Controllers import WhatTheMaskController, APIAuthController, RabbitMQController
# from app.Expects import WhatTheMaskExpect
# from app.Models import WhatTheMaskModel, APIAuthModel, RabbitMQModel
# from app.Services import WhatTheMaskService, APIAuthService, RabbitMQService