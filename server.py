from app import sql_app

if __name__ == '__main__':
    sql_app.run(debug=True, host='0.0.0.0', port=8080)