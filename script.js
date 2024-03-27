document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value
    };
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("message").innerHTML = JSON.parse(xhr.responseText).message;
            document.getElementById("userForm").reset();
        }
    };
    xhr.send(JSON.stringify(formData));
});
