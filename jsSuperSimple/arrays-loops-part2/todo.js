const todoList = [
    {
        name: 'make dinner',
        dueDate: '2022-12-22',
    },
    {
        name:'wash the car',
        dueDate: '2023-10-04',
    }
];

function taperEnter(event)
{
    if(event.key === 'Enter')
    {
        addTodo();
    }
}
function renderTodoList()
{
    let todoListHTML = '';
    for (let i = 0; i < todoList.length; i++)
    {
        const todoObject = todoList[i];
       // const name = todoObject.name;
        //const dueDate = todoObject.dueDate;
        const {name, dueDate} = todoObject;
        const html = `
                        <div>${name}</div>
                        <div>${dueDate}</div>
                        <button onclick="
                           todoList.splice(${i}, 1);
                           renderTodoList();
                        "  class="delete-button">Delete</button>
                    `;
        todoListHTML += html ;
    }
    document.querySelector('.js-todo-list').innerHTML = todoListHTML;
}


function addTodo()
{
    const inputElement = document.querySelector('.js-input');
    const name = inputElement.value;
    const dateInputElement = document.querySelector('.js-due-date-input');
    const dueDate = dateInputElement.value;

    inputElement.value = '';
    todoList.push({
        name,
        dueDate
    });
    dateInputElement.value = '';
    console.log(todoList);

    renderTodoList(); 
}