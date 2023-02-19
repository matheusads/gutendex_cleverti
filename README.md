Basic API Project to Python dev role at Cleverti/Moro Tech.

Tldr: Simple API that will help rate and review books.

I choose use minimum possible external libs, so in this project I only used:
Poetry - for dependencies management.  
FastApi with all your powerful to api routers.    
MongoEngine as ODM for MongoDB.  
Pytest - test python lib.  
Docker and Docker Compose to set up application environment and database.  

**Project Setup**

To run this project you'll need **Docker** and **Docker Compose**.

``git clone git@github.com:matheusads/gutendex_cleverti.git``

Run docker compose file with command bellow  
``docker-compose up -d``  

This command will build and up database and server

With server up you can see FastAPI provided documentation in   
http://localhost:8000/docs  
http://localhost:8000/redoc  

At first above link you can also easily test the endpoints. 
If you like to use Postman I provide a basic collection json in CLEVERTI.postman_collection to request all the routes 
and most of the cases 

