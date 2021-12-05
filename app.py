from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('study')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://evgenii:rnhf89ed@localhost/flask_db'
db = SQLAlchemy(app)

# def get_info():
#     request.json
#     request.headers.get('')
#
#     return jsonify({'status': 'ok'} )
#
# app.add_url_rule('/info', view_func=get_info, methods=['GET'])
# app.run(host='0.0.0.0', port=5000)
