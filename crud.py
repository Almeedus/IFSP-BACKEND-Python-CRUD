from db import connect

#this variable is responsable to execute SQL comands.
cursor = connect.cursor()
databaseTables = ['aluno', 'aluno_curso', 'curso', 'sair']
databaseCRUD = ['Criar novo registro', 'Ler registro', 'Atualizar registro', 'Deletar registro']

def CloseConnectionTable():
    cursor.execute(f"SELECT * FROM {databaseTables[option-1]}")
    cursor.fetchall()
    


def updateAluno(option):
    optionChange = option

    try:
        newName = str(input('Novo nome: '))
        newAge = int(input('Nova idade: '))
        newGender = int(input('Novo sexo [1-Masc | 2-Fem]: '))
        newTelephone = int(input('Novo telefone [(xx)xxxxx-xxxx]: '))

        cursor.execute(f"UPDATE aluno SET Nome = '{newName}', Idade = {newAge}, Sexo = '{newGender}', Telefone = '{newTelephone}' WHERE RA = {optionChange}")
        connect.commit()
    except ValueError:
        return "Valor digitado não é o esperado."
        
            
def updateCurso(option):
    optionChange = option

    try:
        newName = str(input('Nome: '))
        newDescricao = str(input('Descricao: '))
        newNumeroVagas = int(input('Quantidade de vagas: '))
        newCargaHoraria = int(input('Carga horária: '))

        cursor.execute(f"UPDATE curso SET Nome = '{newName}', Descricao = '{newDescricao}', Numero_vagas = '{newNumeroVagas}', Carga_horaria = '{newCargaHoraria}' WHERE ID_curso = {optionChange}")
        connect.commit()
    except ValueError:
        return "Valor digitado não é o esperado."
            

while True:
    print('\nTABELAS DA ESCOLA')
    for indice, table in enumerate(databaseTables):
        print(f'{indice+1}. {table}')
    
    option = int(input('\nQual Tabela deseja realizar a operação: '))

    for indice, operation in enumerate(databaseCRUD):
        print(f'{indice+1}. {operation}')


    # Starting CRUD 
    optionCrud = int(input('\nQual operação deseja realizar: '))

    #Table ALUNO
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
            CloseConnectionTable()
        elif optionCrud == 3:
            #CRUD - Update
            CloseConnectionTable()

            optionChange = int(input('Qual o ID que deseja modificar: '))
            updateAluno(option=optionChange)
        elif optionCrud == 4:
            #CRUD - Delete
            alunoRA = int(input('Qual registro quer apagar: '))
            cursor.execute(f"DELETE FROM {databaseTables[option-1]} WHERE RA = {alunoRA}")
            
        else:
            print('Digite uma opção válida.')

    #TABLE ALUNO_CURSO
    elif option == 2:
        if optionCrud == 1:
            #CRUD - Create
            alunoRA = str(input('RA do Aluno: '))
            cursoID = int(input('ID do Curso: '))
            cursor.execute(f"INSERT INTO {databaseTables[option-1]} (FK_RA_aluno, FK_ID_curso) VALUES ('{alunoRA}',{cursoID})")
            connect.commit()
            print('Dados inseridos com sucesso.')
        elif optionCrud == 2:
            #CRUD - Read
            cursor.execute(f"SELECT ac.ID_curso_aluno, a.Nome AS RA, c.Nome AS ID_curso FROM aluno_curso ac JOIN aluno a ON ac.FK_RA_aluno = a.RA JOIN curso c ON ac.FK_ID_curso = c.ID_curso;")
            result = cursor.fetchall()
        elif optionCrud == 3:
            #CRUD - Update  VOLTAR AQUI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            cursor.execute(f"SELECT ac.ID_curso_aluno, a.Nome AS RA, c.Nome AS ID_curso FROM aluno_curso ac JOIN aluno a ON ac.FK_RA_aluno = a.RA JOIN curso c ON ac.FK_ID_curso = c.ID_curso;")
            result = cursor.fetchall()

            optionChange = int(input('Qual o ID que deseja modificar: '))
            
            RAorID = int(input('Digite 1. Aluno e 2.Curso: '))

            if RAorID == 1:
                cursor.execute(f"SELECT FK_RA_aluno FROM aluno_curso WHERE ID_curso_aluno = {optionChange}")
                FK_RA_aluno = cursor.fetchone()[0]
                updateAluno(FK_RA_aluno)
            elif RAorID == 2:
                cursor.execute(f"SELECT FK_ID_curso FROM aluno_curso WHERE ID_curso_aluno = {optionChange}")
                FK_RA_aluno = cursor.fetchone()[0]
                updateCurso(FK_RA_aluno)
            else:
                print('Opção inválida')
        elif optionCrud == 4:
            #CRUD - Delete
            alunoCursoID = int(input('Qual registro quer apagar: '))
            cursor.execute(f"DELETE FROM {databaseTables[option-1]} WHERE ID_curso_aluno = {alunoCursoID}")
        else:
            print('Digite uma opção válida.')

    #TABLE CURSO
    elif option == 3:
        if optionCrud == 1:
            nome = str(input('Nome: '))
            descricao = str(input('Descrição: '))
            numeroVagas = int(input('Quantidade de Vagas: '))
            cargaHoraria = int(input('Carga horária: '))
            cursor.execute(f"INSERT INTO {databaseTables[option-1]} (Nome, Descricao, Numero_vagas, Carga_horaria) VALUES ('{nome}','{descricao}', {numeroVagas}, {cargaHoraria})")
            connect.commit()
            print('Dados inseridos com sucesso.')
        elif optionCrud == 2:
            #CRUD - Read
            CloseConnectionTable()
        elif optionCrud == 3:
            #CRUD - Update
            CloseConnectionTable()

            optionChange = int(input('Qual o ID que deseja modificar: '))
            updateCurso(optionChange)
        elif optionCrud == 4:
             #CRUD - Delete
            cursoID = int(input('Qual registro quer apagar: '))
            cursor.execute(f"DELETE FROM {databaseTables[option-1]} WHERE ID_curso = {cursoID}")
        else:
            print('Digite uma opção válida.')

    elif option == 4:
        break
    else:
        print('Digite uma opção válida.')

    

