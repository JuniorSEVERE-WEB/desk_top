const todoList = [{
    name: 'Junior',
    dueDate: '2022-09-09'
    },
    {
    name: 'SEVERE',
    dueDate: '2021-10-10'
    }];


function renderTodoList()
{
    let todoListHTML = '';
    for(let i = 0; i < todoList.length; i++)
    {
        const todoObject = todoList[i];
        const {name, dueDate} = todoObject;
        const html = `
        <p>
        ${name}
        ${dueDate}
        <button onclick="
          todoList.splice(${i}, 1);
          renderTodoList();
        ">Delete</button>
        </p>
        `;
        todoListHTML += html;
    }
    document.querySelector('.js-todo-list').innerHTML = todoListHTML;
}


function addTodo()
{
    const inputElement = document.querySelector('.js-input-name');
    const name = inputElement.value;
    inputElement.value = '';
    const inputDate = document.querySelector('.js-input-dueDate');
    const dueDate = inputDate.value;
    todoList.push({
        name,
        dueDate
    });
    console.log(todoList);
    renderTodoList();
    
}