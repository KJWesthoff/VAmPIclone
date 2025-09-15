from config import vuln_app, db
from models.user_model import User
import os

'''
 Decide if you want to server a vulnerable version or not!
 DO NOTE: some functionalities will still be vulnerable even if the value is set to 0
          as it is a matter of bad practice. Such an example is the debug endpoint.
'''
vuln = int(os.getenv('vulnerable', 1))
# vuln=1
# token alive for how many seconds?
alive = int(os.getenv('tokentimetolive', 60))


# Initialize database on startup
def init_db():
    try:
        # Check if database exists and has tables
        db.create_all()
        # Only populate if no users exist
        if not User.query.first():
            User.init_db_users()
            print("Database initialized with default data")
    except Exception as e:
        print(f"Database initialization error: {e}")

# start the app with port 5000 and debug on!
if __name__ == '__main__':
    with vuln_app.app.app_context():
        init_db()
    vuln_app.run(host='0.0.0.0', port=5000, debug=True)
