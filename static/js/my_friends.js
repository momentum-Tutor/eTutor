let userSelector = document.querySelectorAll('#user-selector')
let selfUser = document.querySelector('#self-user')

for (let user of userSelector) {
    console.log(user.innerText.split(" ")[0])
    let username = user.innerText.split(" ")[0]
    let generatedMessageSelector = document.querySelector(`#message-${username}`)
    generatedMessageSelector.addEventListener('click', function () {
        let arr = [username, selfUser.innerText]
        arr.sort()
        window.location.href = "/direct_message/" + arr[0] + arr[1]
    })
}