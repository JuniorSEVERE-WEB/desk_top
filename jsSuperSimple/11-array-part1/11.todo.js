const todoList = ['fff', 'ddd'];
renderTodoList();
function renderTodoList()
{
    let todoListHTML = '';

    for(let i = 0; i < todoList.length; i++) 
    {
        const todo = todoList[i];
        const html = `<p>${todo}</p>`;
        todoListHTML += html;
    }
    console.log(todoListHTML);
    document.querySelector('.js-todo-list.todo-grid').innerHTML = todoListHTML;
}


function addTodo()
{
    const inputElement = document.querySelector('.js-name-input');
    const name = inputElement.value;
    console.log(name);


    todoList.push(name);
    console.log(todoList);

    inputElement.value = '';
    renderTodoList();
    
    
}