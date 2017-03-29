#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from Patients import Patients

#---- Main --------------------------------------------------------------------

db = Patients()
#db.create_database()
#db.create_table()
#db.load_csv_into_database()
test = db.get_patient_info('X164_120423')
print("This is the test: ", test)
