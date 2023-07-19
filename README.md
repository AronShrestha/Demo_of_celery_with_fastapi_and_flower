# Demo_of_celery_with_fastapi_and_flower
I am exploring Celery by creating FastAPI endpoints for a long-running task, which is handled by Celery using Redis as the broker. Additionally, I have containerize the application using Docker.

## You can test this demo project by:
1) Clone the repo
2) Built and run the docker using command : "docker-compose up"
3) You can see the differnt ports used, in docker-compose.yaml file
4) You can test diferrent endpoints by navigating to url: localhost:8003/docs. 
5) You can monitor celery working wih flower my going to url : localhost:5556.
