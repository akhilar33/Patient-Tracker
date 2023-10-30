import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import random

class  PaitentDAO:
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
        hostname= "localhost"
        database= "Patient"
        username= "root"
        password= "password"

        self.engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))

    def insert_patient_data(self, data):
        try:
            print(type(data))

            # Insert the data into the MySQL database table
            data['patient_id'] = [random.randint(1000,9999) for _ in range(len(data))]
            data.to_sql(name='patient', con=self.engine, if_exists='append', index=False)
            #data is insert
            #possible update could be show a pop up saying that paitent data is sucessfully added. 

            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")


    def getquery(self , feild , patientdata):
        query = f"SELECT * FROM patient WHERE {feild} = %s"
        self.cursor.execute(query, (patientdata,))
        df = pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        #return the df
        print(type(df))

    def updated(self, first_name, field_to_update, new_value):
        try: 
            update_query = f"UPDATE patient SET {field_to_update} = %s WHERE FIRST_Name = %s"
            self.cursor.execute(update_query, (new_value, first_name))
            self.connection.commit()
        except Exception as e:
            return f"Error: {e}"
    def delete(self, firstName):
        try: 
            delete_query = "DELETE FROM patient WHERE FIRST_Name = %s"
            self.cursor.execute(delete_query, (firstName,))
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            return f"Error: {e}"

        


if __name__ == "__main__":
    # Data for the new patient
    data = {
    'username': ['DocJohn21', 'DrSarahMD', 'HealingDocMike', 'DrEmilyD', 'RoboDoc'],
    'password': ['password1', 'password2', 'password3', 'password4', 'password5']
    }
    data = pd.DataFrame(data)
    
    inserter = PaitentDAO()
    inserter.delete('Akhila')




