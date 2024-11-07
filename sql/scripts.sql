show databases;

#criando banco de dados
create database db_gerefacil;

use db_gerefacil;

show tables;

# criando tabelas

create table usuarios (
	ID int unique primary key auto_increment,
    Nome varchar(255) not null,
    login varchar(100) not null unique,
    senha int(50) not null unique,
    perfil varchar(45) not null
);

create table produtos (
	id int primary key auto_increment not null,
    nome_produto varchar(255) not null,
    descricao varchar(255),
    qtd int not null
);

# inserindo dados

# tabela de produots
INSERT INTO produtos(nome_produto, descricao, qtd)
VALUES ('teclado', 'teclado desktop', 5);

#tabela de usuarios

INSERT INTO usuarios (nome, login, senha, perfil)
VALUES ('kaio', 'adm', 123, 'adm');

select * from usuarios;
select * from produtos;