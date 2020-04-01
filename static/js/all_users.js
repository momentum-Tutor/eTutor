let userSelector = document.querySelectorAll('#user-selector')
let selfUser = document.querySelector('#self-user')
let homeButton = document.querySelector('#home-button')

for (let user of userSelector) {
    let username = user.innerText.split(" ")[0]
    let generatedSelector = document.querySelector(`#message-${username}`)
    generatedSelector.addEventListener('click', function() {
        let arr = [username, selfUser.innerText]
        arr.sort()
        window.location.href = "/direct_message/" + arr[0] + arr[1]
    })
}