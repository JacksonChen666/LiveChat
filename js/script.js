var socket = io();

function sendMessage(message) {
    socket.emit('message', {message: message});
}

function addMessage(message) {
    var ul = document.getElementById("messages");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(message));
    ul.appendChild(li);
}

socket.on('message', function(data) {
    addMessage(data);
});

var input = document.getElementById("input");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        if (input.value) {
            sendMessage(input.value);
            input.value = "";
        }
    }
});