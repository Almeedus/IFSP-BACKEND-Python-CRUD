--CREATE USER 'cliente'@'localhost' IDENTIFIED BY 'client';
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
    FOREIGN KEY (FK_RA_aluno) REFERENCES aluno (RA),
    FOREIGN KEY (FK_ID_curso) REFERENCES curso (ID_curso)
);