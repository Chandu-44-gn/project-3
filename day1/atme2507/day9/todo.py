import requests
base='https://jsonplaceholder.typicode.com'
def read_all_todos():
    url=f'{base}/todos'
    response=requests.get(url)
    todos=response.json()
    return todos
def read_by_id(id):
    url=f'{base}/todos/{id}'
    response=requests.get(url)
    todo=response.json()
    return todo
def create(title,completed):
    url=f'{base}/todos'
    data={
        'userId':1,
        'title':title,
        'completed':completed
    }
    response=requests.post(url,json=data)
    return response.json() 
   
def update(id,title,completed):
    url=f'{base}/todos/{id}'
    data=read_by_id(id)
    data['title']=title
    data['completed']=completed
    response=requests.put(url,json=data)
    return response.json() 
def delete(id):
    url=f'{base}/todos/{id}'
    response=requests.delete(url)
    return response.json() 

def main():
    print('1-read all,2-read by id,3-create,4-update,5-delete,6-exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        todos=read_all_todos()
        print(todos)
    elif choice==2:
        id=int(input('Enter todo id:'))
        todo=read_by_id(id)
        print(todo)
    elif choice==3:
        title=input('Title:')
        completed=input('completed(y/n):')=='y'
        todo=create(title,completed)
        print(todo)   
    elif choice==4:
        id=int(input('Todo Id to update:'))
        print(read_by_id(id))
        title=input('New Title:')
        completed=input('completed(y/n):')=='y'
        todo=update(id,title,completed)
        print(todo)
    elif choice==5:
        id=int(input('Todo Id to delete:'))
        todo=delete(id)
        print(todo)
    return choice


choice=main()
while (choice!=6):
    choice=main()
    