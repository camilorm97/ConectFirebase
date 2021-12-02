# Camilo Code

import pyrebase


def principal():
    firebaseConfig = {
        'apiKey': "",
        'authDomain': "",
        'databaseURL': "",
        'projectId': "",
        'storageBucket': "",
        'messagingSenderId': "",
        'appId': ""
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    dataInsertDefault = {
        'Name': "jorge",
        'Passwd': '12345',
        'LugarNacimiento': [
            'Paris', 'Francia'
        ],
        'Age': '20',
    }
    dataInsertCustom = {
        'Carrera': "Informatica",
        'Students': '2',
    }
    dataInsertCustomMale = {
        'Name': "jorge",
        'Passwd': '12345',
        'LugarNacimiento': [
            'Paris', 'Francia'
        ],
        'Age': '20',
    }
    dataInsertCustomFemale = {
        'Name': "Elizabeth",
        'Passwd': '54321',
        'LugarNacimiento': [
            'Milan', 'Italia'
        ],
        'Age': '19',
    }
    # Push data
    # Esto crea una tabla con un registro random
    db.push(dataInsertDefault)

    # Create your own key
    # Esto crea una tabla con un registro personalizado
    db.child("Students").set(dataInsertCustom)

    # Esto crea una tabla dentro de otra tabla (en este caso dentro de la anterior personalizada)
    # con un nombre personalizado
    db.child("Students").child("Males").set(dataInsertCustomMale)
    db.child("Students").child("Females").set(dataInsertCustomFemale)


if __name__ == '__main__':
    try:
        principal()
    except KeyboardInterrupt:
        print("Out form the system.")

