# About the project

The project is a platform in which the users will be able to exchange knowledge through it. You can learn from playing the guitar to the basics of a programming language, in which there will be a knowledge exchange, meaning that since you will be teaching someone else, it is expected that you too will be learning from your study partner.

This platform is being developed by all participants in the Processos de Software course at UFRN.

# API Component

This component is responsible for create an API for use in web and android versions of system being developed.

## Technologies
- Python 3
- Falcon
- MySQL

## API Description
Api in development for the platform described above, includes the following methods: 

|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /users            | GET    | empty   | ---     |   Return all users    | 
| /user/{id}        | GET    | empty   | ---     |   Return a user by given id | 
| /user/email/{e-mail}    | GET    | empty   | --- |   Return a user by given email    | 
| /user             | POST   | JSON    | {<br/>"name":"Example",<br/>"email":"example@example.com",<br/>"age":"21",<br/>"password":"123456"<br/>} |   Add a user | 
| /user/{id}        | DELETE | empty   | ---     |   Delete user by id | 
| /login            | GET    | empty   | ---     |   +++++++++++       | 
| /users      | GET    | empty   | ---     |   Take all users  | 
| /users      | GET    | empty   | ---     |   Take all users  | 

## Getting Started
### Installing prerequisites
To use the api server you will need Python 3, Falcon and a WSGI Server (in our project we use gunicorn).

To run our api server you will need to do this following steps one time:

1. Install python-pip if you don't have it;
2. Install falcon using pip: `# pip install falcon`;
3. Install gunicorn using pip: `# pip install gevent gunicorn`.

For easier management of pip packages, it's recommended to use [virtualenv](https://virtualenv.pypa.io/en/stable/). It creates isolated Python environments, and does not need superuser privileges to install packages. 

### Running
To run the api server do the following: 

1. Clone the project: `$ git clone git@github.com:Processos-de-software-2016-2/python-api.git`;
2. Run the server: `gunicorn main:app`;
3. Make a HTTP request on port 8000 to any of the URLs listed in API Description section.

# How to Contribute
1. Clone the project: `$ git clone git@github.com:Processos-de-software-2016-2/python-api.git`;
2. If you already have the project update it: `$ git pull origin master`;
3. Create a branch to start coding: `$ git checkout -b <branch_name>`;
4. Commit and push your changes: `$ git push origin <branch_name>`;
5. Create a pull request from your branch to master.

# Team
- [Daniel Tiago de Souza Brito](https://github.com/danielmanfred)
- [João Eduardo Medeiros](https://github.com/joaomedeiros95)
- [Stefano Momo Loss](https://github.com/Stefano10)
- [victorsv](https://github.com/victorsv)
- [Vinícius Kleiton da Trindade Ramos](https://github.com/Vinnykt)

# Other Parts of this Project 

- [Android](https://github.com/Processos-de-software-2016-2/Android)
- [Infrastructure](https://github.com/Processos-de-software-2016-2/Infraestrutura) 
- [WebApp](https://github.com/Processos-de-software-2016-2/Web-App)
- [UX](https://github.com/Processos-de-software-2016-2/UX)
