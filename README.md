# crud-python
CRUD em Python para a matéria de Backend I 

## Programas necessários
+ Python na versão - 3.11.5
+ MySQL na versão - 8.2.0
+ Visual Studio - 2019 x64

## Dependências
Para a utilização deste CRUD está sendo utilizado uma biblioteca externa para fazer a conexão entre a linguagem Python e o MySQL chamada mysql-connector-python. 

Para instalar a biblioteca no terminal digite: 
```
pip install -r requirements.txt
```
ou
```
pip3 install -r requirements.txt
```
## Banco de Dados
Para criar o user pode descomentar esses comandos e rodar no user 'root'
```
CREATE USER 'client'@'localhost' IDENTIFIED BY 'client';
GRANT ALL PRIVILEGES ON * . * TO 'client'@'localhost';
FLUSH PRIVILEGES;
```
Acesse o novo usuário e rode o script do banco de dados
