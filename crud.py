from db import connect

#this variable is responsable to execute SQL comands.
cursor = connect.cursor()
databaseTables = ['aluno', 'aluno_curso', 'curso', 'sair']
databaseCRUD = ['Criar novo registro', 'Ler registro', 'Atualizar registro', 'Deletar registro']

def close_connection_table():
    cursor.execute(f"SELECT * FROM {databaseTables[option-1]}")
    cursor.fetchall()
    


def update_student(option):
    option_change = option

    try:
        new_name = str(input('Novo nome: '))
        new_age = int(input('Nova idade: '))
        new_gender = int(input('Novo sexo [1-Masc | 2-Fem]: '))
        new_telephone = int(input('Novo telefone [(xx)xxxxx-xxxx]: '))

        cursor.execute(f"UPDATE aluno SET Nome = '{new_name}', Idade = {new_age}, Sexo = '{new_gender}', Telefone = '{new_telephone}' WHERE RA = {option_change}")
        connect.commit()
    except ValueError:
        return "Valor digitado não é o esperado."
        
            
def update_course(option):
    option_change = option

    try:
        new_name = str(input('Nome: '))
        new_description = str(input('Descricao: '))
        new_number_vacancies = int(input('Quantidade de vagas: '))
        new_workload = int(input('Carga horária: '))

        cursor.execute(f"UPDATE curso SET Nome = '{new_name}', Descricao = '{new_description}', Numero_vagas = '{new_number_vacancies}', Carga_horaria = '{new_workload}' WHERE ID_curso = {option_change}")
        connect.commit()
    except ValueError:
        return "Valor digitado não é o esperado."
            

while True:
    print('\nTABELAS DA ESCOLA')
    for index, table in enumerate(databaseTables):
        print(f'{index+1}. {table}')
    
    option = int(input('\nQual Tabela deseja realizar a operação: '))

    for index, operation in enumerate(databaseCRUD):
        print(f'{index+1}. {operation}')


    # Starting CRUD 
    option_crud = int(input('\nQual operação deseja realizar: '))

    #Table ALUNO
    if option == 1:
        if option_crud == 1:
            #CRUD - Create
            name = str(input('Nome: '))
            age = int(input('Idade: '))
            gender = int(input('Sexo [1-Masc | 2-Fem]: '))
            telephone = int(input('Telefone [(xx)xxxxx-xxxx]: '))
            cursor.execute(f"INSERT INTO {databaseTables[option-1]} (Nome, Idade, Sexo, Telefone) VALUES ('{name}',{age},{gender},{telephone})")
            connect.commit()
            print('Dados inseridos com sucesso.')
        elif option_crud == 2:
            #CRUD - Read
            close_connection_table()
        elif option_crud == 3:
            #CRUD - Update
            close_connection_table()

            option_change = int(input('Qual o ID que deseja modificar: '))
            update_student(option=option_change)
        elif option_crud == 4:
            #CRUD - Delete
            student_identification = int(input('Qual registro quer apagar: '))
            cursor.execute(f"DELETE FROM {databaseTables[option-1]} WHERE RA = {student_identification}")
            
        else:
            print('Digite uma opção válida.')

    #TABLE ALUNO_CURSO
    elif option == 2:
        if option_crud == 1:
            #CRUD - Create
            student_identification = str(input('RA do Aluno: '))
            course_id = int(input('ID do Curso: '))
            cursor.execute(f"INSERT INTO {databaseTables[option-1]} (FK_RA_aluno, FK_ID_curso) VALUES ('{student_identification}',{course_id})")
            connect.commit()
            print('Dados inseridos com sucesso.')
        elif option_crud == 2:
            #CRUD - Read
            cursor.execute(f"SELECT ac.ID_curso_aluno, a.Nome AS RA, c.Nome AS ID_curso FROM aluno_curso ac JOIN aluno a ON ac.FK_RA_aluno = a.RA JOIN curso c ON ac.FK_ID_curso = c.ID_curso;")
            result = cursor.fetchall()
        elif option_crud == 3:
            #CRUD - Update  VOLTAR AQUI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            cursor.execute(f"SELECT ac.ID_curso_aluno, a.Nome AS RA, c.Nome AS ID_curso FROM aluno_curso ac JOIN aluno a ON ac.FK_RA_aluno = a.RA JOIN curso c ON ac.FK_ID_curso = c.ID_curso;")
            result = cursor.fetchall()

            option_change = int(input('Qual o ID que deseja modificar: '))
            
            student_identification_or_course_id = int(input('Digite 1. Aluno e 2.Curso: '))

            if student_identification_or_course_id == 1:
                cursor.execute(f"SELECT FK_RA_aluno FROM aluno_curso WHERE ID_curso_aluno = {option_change}")
                FK_RA_aluno = cursor.fetchone()[0]
                update_student(FK_RA_aluno)
            elif student_identification_or_course_id == 2:
                cursor.execute(f"SELECT FK_ID_curso FROM aluno_curso WHERE ID_curso_aluno = {option_change}")
                FK_RA_aluno = cursor.fetchone()[0]
                update_course(FK_RA_aluno)
            else:
                print('Opção inválida')
        elif option_crud == 4:
            #CRUD - Delete
            student_course_id = int(input('Qual registro quer apagar: '))
            cursor.execute(f"DELETE FROM {databaseTables[option-1]} WHERE ID_curso_aluno = {student_course_id}")
        else:
            print('Digite uma opção válida.')

    #TABLE CURSO
    elif option == 3:
        if option_crud == 1:
            name = str(input('Nome: '))
            description = str(input('Descrição: '))
            number_vacancies = int(input('Quantidade de Vagas: '))
            workload = int(input('Carga horária: '))
            cursor.execute(f"INSERT INTO {databaseTables[option-1]} (Nome, Descricao, Numero_vagas, Carga_horaria) VALUES ('{name}','{description}', {number_vacancies}, {workload})")
            connect.commit()
            print('Dados inseridos com sucesso.')
        elif option_crud == 2:
            #CRUD - Read
            close_connection_table()
        elif option_crud == 3:
            #CRUD - Update
            close_connection_table()

            option_change = int(input('Qual o ID que deseja modificar: '))
            update_course(option_change)
        elif option_crud == 4:
             #CRUD - Delete
            course_id = int(input('Qual registro quer apagar: '))
            cursor.execute(f"DELETE FROM {databaseTables[option-1]} WHERE ID_curso = {course_id}")
        else:
            print('Digite uma opção válida.')

    elif option == 4:
        break
    else:
        print('Digite uma opção válida.')

    

