from flask import Response
import traceback

from models.user_model import *
from app import vuln

def populate_db():
    try:
        print("Starting database population...")
        db.drop_all()
        print("Dropped all tables")
        db.create_all()
        print("Created all tables")
        User.init_db_users()
        print("Initialized users")
        response_text = '{ "message": "Database populated." }'
        response = Response(response_text, 200, mimetype='application/json')
        return response
    except Exception as e:
        print(f"Database population error: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        error_text = '{ "error": "Database initialization failed", "details": "' + str(e) + '" }'
        return Response(error_text, 500, mimetype='application/json')

def basic():
    response_text = '{ "message": "VAmPI the Vulnerable API", "help": "VAmPI is a vulnerable on purpose API. It was ' \
                    'created in order to evaluate the efficiency of third party tools in identifying vulnerabilities ' \
                    'in APIs but it can also be used in learning/teaching purposes.", "vulnerable":' + "{}".format(vuln) + "}"
    response = Response(response_text, 200, mimetype='application/json')
    return response
