console.log('hello')
let userSelector = document.querySelectorAll('#user-selector')
let selfUser = document.querySelector('#self-user')

for (let user of userSelector) {
    let username = user.innerText.split(" ")[0]
    let generatedAcceptSelector = document.querySelector(`#accept-${username}`)
    let generatedDeclineSelector = document.querySelector(`#decline-${username}`)
    generatedAcceptSelector.addEventListener('click', function () {
        let arr = [username, selfUser.innerText]
        arr.sort()
        accept(arr)
    })
    generatedDeclineSelector.addEventListener('click', function () {
        let arr = [username, selfUser.innerText]
        arr.sort()
        decline(arr)
    })
}

function accept(arr) {
    console.log(arr)
    if (arr[0] == selfUser.innerText) {
        let data = { user_one: arr[0], user_two: arr[1], accepted_one: "True" }
        fetchRequest(data)
    } else {
        let data = { user_one: arr[0], user_two: arr[1], accepted_two: "True" }
        fetchRequest(data)
    }
}

function decline(arr) {
    data = { user_one: arr[0], user_two: arr[1], deleted: "True" }
    fetchRequest(data)
}

function fetchRequest(data) {
    console.log(data)
    fetch('/users/friend_request', {
        method: 'POST',
        headers: { 'Content-type': 'application.json', },
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .then(response => {
            console.log("JsonResponse recieved")
            console.log(response)
        })
        .catch((error) => {
            console.error('JSON response ERROR')
        })
}