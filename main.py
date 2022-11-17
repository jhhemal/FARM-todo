from fastapi import FastAPI, status
from database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Create TodoRequest Base model
class ToDoRequest(BaseModel):
    task: str


# Create the database
Base.metadata.create_all(engine)



app = FastAPI()

@app.get('/')
async def root():
    return "todo"

@app.post('/todo', status_code=status.HTTP_201_CREATED)
async def create_todo(todo: ToDoRequest):

    # Create a new Database Session
    session = Session(bind=engine, expire_on_commit=False)
    
    # Creare an instance of the Todo Database model
    tododb = ToDo(task = todo.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()

    # Grab the id given to the object from the database
    id = tododb.id

    # Close the session
    session.close()
    
    return f'create todo item with {id}'

@app.get('/todo/{id}')
async def read_todo(id: int):
    return "read todo item with id {id}"

@app.put('/todo/{id}')
async def update_todo(id: int):
    return "Update todo item with id {id}"

@app.delete('/todo/{id}')
async def delte_todo(id: int):
    return "delete todo item with id {id}"

@app.get("/todo")
async def read_todo_list():
    return "read todo list"

