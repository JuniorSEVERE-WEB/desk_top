const todoList = ['tache1', 'tache2']
renderTodoList();

function renderTodoList()
{

let todoListHTML = '';
for (let i = 0; i < todoList.length; i++)
{
    const todo = todoList[i];
    const html = `<p>${todo}</p>`;
    todoListHTML += html;
}
const para = document.querySelector('.js-todo-list');
para.innerHTML = todoListHTML;
}
function addTodo()
{
    const inputElement = document.querySelector('.js-input');
    const name = inputElement.value;
    console.log(name);

    todoList.push(name);
    console.log(todoList);
    renderTodoList();
    
    
}