#---- Imports ----------------------------------------------------------------

from lib.patients.Patients import Patients


#---- Functions ---------------------------------------------------------------


def display_menu():
    print(
"""
1 - Create AD database and patients table
2 - Load csv file into the database
3 - Get patient information
q - Return to main menu
""")
    command = input("Please select: ")
    return command


def call_patients_info():
    command = True
    db = Patients()

    while(command):
        command = display_menu()
        if (command == '1'):
            db.create_database()
            db.create_table()
            database_and_table_exist = True
        elif(command == '2'):
            db.load_csv_into_database()
        elif(command == '3'):
            patient_id = input("Enter patient ID: ")
            #import pdb; pdb.set_trace()
            data = db.get_patient_info(patient_id)
            print(("Patient age: {} gender: {} education: {}").format(
                                                            data[0],
                                                            data[1],
                                                            data[2]))
            print(data)
        elif(command == 'q'):
            command = False
        else:
            command = True
