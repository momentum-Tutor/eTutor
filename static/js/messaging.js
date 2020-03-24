console.log("hello")
let messageForm = document.querySelector('#message-form')

messageForm.addEventListener('submit', e => {
    e.preventDefault()
    let recipientInput = document.querySelector('#recipient-input')
    let messageInput = document.querySelector('#message-input')
    let data = {recipient: recipientInput.value, message: messageInput.value}
    console.log(data)
})