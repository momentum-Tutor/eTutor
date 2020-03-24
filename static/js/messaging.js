console.log("hello")
let messageForm = document.querySelector('#message-form')

messageForm.addEventListener('submit', e => {
    e.preventDefault()
    let recipientInput = document.querySelector('#recipient-input')
    let messageInput = document.querySelector('#message-input')
    let data = {recipient: recipientInput.value, message: messageInput.value}
    console.log(data)
    fetch('/messaging/send/', {
        method: 'POST',
        headers: {'Content-type': 'application/json',},
        body: JSON.stringify(data)
    })
    .then((response) => response.json())
    .then(data => {
        console.log(data)
    })
    .catch((error) => {
        console.error('JSON response ERROR')
    })
})