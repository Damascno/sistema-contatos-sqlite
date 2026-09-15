# 📇 Sistema de Contatos — Python + SQLite

Projeto desenvolvido durante meus estudos de **Python** e **banco de dados SQLite**.

O objetivo deste projeto é praticar operações básicas de banco de dados utilizando Python, incluindo **criação de tabelas, inserção, consulta, atualização e exclusão de registros (CRUD)**.

## 🚀 Tecnologias utilizadas

- 🐍 Python
- 🗄️ SQLite
- 📦 Biblioteca sqlite3

## 📚 Conceitos praticados

- Conexão com banco de dados SQLite
- Criação de tabelas
- Chave primária com AUTOINCREMENT
- Inserção de registros
- Consulta de dados com SELECT
- Atualização de registros com UPDATE
- Exclusão de registros com DELETE
- Uso de commit() para salvar alterações
- Uso de parâmetros ? nas consultas SQL
- Fechamento da conexão com close()

## ⚙️ Funcionalidades

- Criar a tabela de contatos
- Cadastrar contatos
- Consultar contatos
- Atualizar telefone de um contato
- Excluir um contato

## 📁 Estrutura do projeto

sistema-contatos-sqlite/
│
├── contatos.py
├── README.md
└── .gitignore

O arquivo contatos.db é criado localmente quando o programa é executado e não é enviado para o repositório.

## ▶️ Como executar

1. Instale o Python.

2. Clone o repositório:

git clone URL_DO_SEU_REPOSITORIO

3. Entre na pasta:

cd sistema-contatos-sqlite

4. Execute o programa:

python contatos.py

O banco de dados SQLite será criado automaticamente no diretório do projeto.

## 🗃️ Exemplo de dados

| ID | Nome | E-mail | Telefone |
|---:|---|---|---|
| 1 | João | joao@email.com | 123-456-7890 |
| 2 | Maria | maria@email.com | 987-654-3210 |
| 3 | Carlos | carlos@email.com | 555-555-5555 |

Durante a execução, o programa demonstra operações de UPDATE e DELETE.

## 🎯 Objetivo do projeto

Este projeto faz parte da minha jornada de aprendizado em programação.

A ideia é construir uma base sólida em **Python, SQL e bancos de dados**, evoluindo gradualmente para projetos mais completos.

## 📌 Próximos passos

- [ ] Criar um menu interativo no terminal
- [ ] Permitir cadastrar novos contatos pelo usuário
- [ ] Permitir pesquisar contatos
- [ ] Permitir editar qualquer contato
- [ ] Adicionar validação de e-mail e telefone
- [ ] Separar o código em funções
- [ ] Criar uma interface gráfica
- [ ] Melhorar o tratamento de erros

---

⭐ Projeto criado para fins de estudo e prática em Python e SQLite.
