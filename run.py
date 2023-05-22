from app import app
from app import db
from app.models import User

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
        #Runs the app
        app.run(debug=True)
