import mysql.connector

connect = mysql.connector.connect(
    #change names after creat a database
    host='localhost',
    user='client',
    password='client',
    database='school'
)

#this variable is responsable to execute SQL comands.
cursor = connect.cursor()
databaseTables = ['aluno', 'aluno_curso', 'curso']
databaseCRUD = ['Criar novo registro', 'Ler registro', 'Atualizar registro', 'Deletar registro']

#cursor.execute("SELECT * FROM {}")
#results = cursor.fetchall()

while True:
    print('\nTABELAS DA ESCOLA')
    for indice, table in enumerate(databaseTables):
        print(f'{indice+1}. {table}')
    
    option = int(input('\nQual Tabela deseja realizar a operação: '))

    for indice, operation in enumerate(databaseCRUD):
        print(f'{indice+1}. {operation}')


    # Starting CRUD 
    optionCrud = int(input('\nQual operação deseja realizar: '))

    #Table CLIENTS
    if option == 1:
        if optionCrud == 1:
            #CRUD - Create
            name = str(input('Nome: '))
            age = int(input('Idade: '))
            gender = int(input('Sexo [1-Masc | 2-Fem]: '))
            telephone = int(input('Telefone [(xx)xxxxx-xxxx]: '))
            cursor.execute(f"INSERT INTO {databaseTables[option-1]} (Nome, Idade, Sexo, Telefone) VALUES ('{name}',{age},{gender},{telephone})")
            connect.commit()
            print('Dados inseridos com sucesso.')
        elif optionCrud == 2:
            #CRUD - Read
            cursor.execute(f"SELECT * FROM {databaseTables[option-1]}")
            result = cursor.fetchall()
            print(result)
            break
        elif optionCrud == 3:
            #CRUD - Update
            cursor.execute(f"SELECT * FROM {databaseTables[option-1]}")
            result = cursor.fetchall()
            print(result)

            optionChange = int(input('Qual o ID que deseja modificar: '))
            
            newName = str(input('Novo nome: '))
            newAge = str(input('Nova idade: '))
            newGender = str(input('Novo sexo [1-Masc | 2-Fem]: '))
            newTelephone = str(input('Novo telefone [(xx)xxxxx-xxxx]: '))

            if newName != '':
                name = newName
            else:
                name 
            if newAge != '':
                if isinstance(newAge, int):
                    age = int(newAge)
            if newGender != '':
                if isinstance(newGender, int):
                    gender = int(newGender)
            if newTelephone != '':
                if isinstance(newTelephone, int):
                    telephone = int(newTelephone)

            cursor.execute(f"UPDATE {databaseTables[option-1]} SET (Nome, Idade, Sexo, Telefone) VALUES ('{name}',{age},{gender},{telephone}), WHERE id = {optionChange}")
            ...
        elif optionCrud == 4:
            #CRUD - Delete
            
            ...
        else:
            print('Digite uma opção válida.')


    elif option == 2:
        if optionCrud == 1:
            ...
        elif optionCrud == 2:
            #CRUD - Read
            cursor.execute(f"SELECT * FROM {databaseTables[option-1]}")
            result = cursor.fetchall()
            print(result)
            break
        elif optionCrud == 3:
            ...
        elif optionCrud == 4:
            ...
        else:
            print('Digite uma opção válida.')


    elif option == 3:
        if optionCrud == 1:
            ...
        elif optionCrud == 2:
            #CRUD - Read
            cursor.execute(f"SELECT * FROM {databaseTables[option-1]}")
            result = cursor.fetchall()
            print(result)
            break
        elif optionCrud == 3:
            ...
        elif optionCrud == 4:
            ...
        else:
            print('Digite uma opção válida.')

    elif option == 4:
        if optionCrud == 1:
            ...
        elif optionCrud == 2:
            #CRUD - Read
            cursor.execute(f"SELECT * FROM {databaseTables[option-1]}")
            result = cursor.fetchall()
            print(result)
            break
        elif optionCrud == 3:
            ...
        elif optionCrud == 4:
            ...
        else:
            print('Digite uma opção válida.')

    else:
        print('Digite uma opção válida.')

    

