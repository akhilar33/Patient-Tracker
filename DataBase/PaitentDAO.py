import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

class PaitentDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
             host = "localhost",
            user= "root",
            password= "password",
            database = 'Patient',
            auth_plugin='mysql_native_password'
        )
        print("Connection established")
        self.cursor = self.connection.cursor()

        
    
    def getquery(self , feild , patientdata):
        query = f"SELECT * FROM patient WHERE {feild} = %s"
        self.cursor.execute(query, (patientdata,))
        df = pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        #return the df
        print(type(df))





if __name__ == "__main__":
    # Data for the new patient
    query = GetPaitentData()
    query.getquery('Last_Name', 'Reddy')
 