# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('dikshant','000','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('Dikshant','Madai','Psychiatrists'), Doctor('parmaye','G','Radiologists'), Doctor('punam','shrestha','Emergency physicians')]
    patients = [Patient('Renuka','singh', 21, '9862480622','D1 001'), Patient('Abishek','Poudel', 22,'985847000','S1 0001'), Patient('shyam','Bohora', 18, '9878521520','C4 444')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)

        elif op == '2':
            # print("-----Patients-----")
        
            # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            # admin.view_patient(patients)
            
            while True:
                op = input('Do you want to discharge a patient(Yes/No):').lower()

                if op == 'yes' :
                   admin.discharge(patients,discharged_patients)

                elif op == 'no' :
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            # 6 - Quit
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
