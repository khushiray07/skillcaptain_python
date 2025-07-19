const addTask = document.getElementById('addTask');
const input = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');

addTask.addEventListener('click', function() {
    const check = input.value.trim();
    if (check === '') {
        return;
    }

    const li = document.createElement('li');

    const span = document.createElement('span');
    span.textContent = check; 

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';

    span.addEventListener('click', function() {
        span.classList.toggle('completed');
    });

    deleteButton.addEventListener('click', function() {
        li.remove();
    });

    li.appendChild(span);
    li.appendChild(deleteButton);
    taskList.appendChild(li);

    input.value = ''; 
});