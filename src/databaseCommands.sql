# Se for necessário criar o user pode descomentar esses comandos e rodar no user 'root'
# CREATE USER 'client'@'localhost' IDENTIFIED BY 'client';
# GRANT ALL PRIVILEGES ON * . * TO 'client'@'localhost';
# FLUSH PRIVILEGES;



# Com o usuário já criado rode o script do BD
CREATE DATABASE school;
USE school;

CREATE TABLE aluno (
    RA INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(20) NOT NULL,
    Idade INT NOT NULL,
    Sexo CHAR(1) NOT NULL,
    Telefone VARCHAR(11) NOT NULL
);

CREATE TABLE curso (
    ID_curso INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(20) NOT NULL,
    Descricao VARCHAR(40) NOT NULL,
    Numero_vagas INT(2) NOT NULL,
    Carga_horaria INT(2) NOT NULL
);

CREATE TABLE aluno_curso (
    ID_curso_aluno INT PRIMARY KEY AUTO_INCREMENT,
    FK_RA_aluno INT NOT NULL,
    FK_ID_curso INT NOT NULL,
    FOREIGN KEY (FK_RA_aluno) REFERENCES aluno (RA) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FK_ID_curso) REFERENCES curso (ID_curso) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO aluno (Nome, Idade, Sexo, Telefone) VALUES ("Eduardo",22,1,15123456789);
INSERT INTO aluno (Nome, Idade, Sexo, Telefone) VALUES ("Maria",18,2,15123456789);
INSERT INTO aluno (Nome, Idade, Sexo, Telefone) VALUES ("Rafael",45,1,15123456789);
INSERT INTO aluno (Nome, Idade, Sexo, Telefone) VALUES ("Caique",35,1,15123456789);
INSERT INTO aluno (Nome, Idade, Sexo, Telefone) VALUES ("Marcela",30,2,15123456789);

INSERT INTO curso (Nome, Descricao, Numero_vagas, Carga_horaria) VALUES ("Backend I", "Desenvolvimento com Python", 40, 40);
INSERT INTO curso (Nome, Descricao, Numero_vagas, Carga_horaria) VALUES ("Backend II", "Desenvolvimento de API com Flask", 40, 40);
INSERT INTO curso (Nome, Descricao, Numero_vagas, Carga_horaria) VALUES ("Frontend I", "HTML e CSS", 40, 40);
INSERT INTO curso (Nome, Descricao, Numero_vagas, Carga_horaria) VALUES ("Frontend II", "Javascript Basico", 40, 40); 
INSERT INTO curso (Nome, Descricao, Numero_vagas, Carga_horaria) VALUES ("Fullstack I", "Projeto WEB completo", 40, 40); 

INSERT INTO aluno_curso (FK_RA_aluno, FK_ID_curso) VALUES (1,1);
INSERT INTO aluno_curso (FK_RA_aluno, FK_ID_curso) VALUES (2,2);
INSERT INTO aluno_curso (FK_RA_aluno, FK_ID_curso) VALUES (3,3);
INSERT INTO aluno_curso (FK_RA_aluno, FK_ID_curso) VALUES (4,4);
INSERT INTO aluno_curso (FK_RA_aluno, FK_ID_curso) VALUES (5,5);