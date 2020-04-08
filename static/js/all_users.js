let userSelector = document.querySelectorAll('#user-selector')
let selfUser = document.querySelector('#self-user')

for (let user of userSelector) {
    let username = user.innerText.split(" ")[0]
    let generatedMessageSelector = document.querySelector(`#message-${username}`)
    let generatedFriendSelector = document.querySelector(`#friend-${username}`)
    generatedMessageSelector.addEventListener('click', function () {
        let arr = [username, selfUser.innerText]
        arr.sort()
        window.location.href = `/direct_message/${arr[0]}SPL${arr[1]}`
    })
    generatedFriendSelector.addEventListener('click', function () {
        let arr = [username, selfUser.innerText]
        arr.sort()
        sendFriendRequest(arr)
    })

}

function sendFriendRequest(arr) {
    if (arr[0] == selfUser.innerText) {
        let data = { user_one: arr[0], user_two: arr[1], accepted_one: "True" }
        fetchRequest(data)
    } else {
        let data = { user_one: arr[0], user_two: arr[1], accepted_two: "True" }
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
}

function LikeOrDislike () {
    console.log('LikeOrDislike')
    const likeButtons = document.querySelectorAll('.like')
    const disLikeButtons = document.querySelectorAll('.dislike')
    
        for (let button of likeButtons){
        button.addEventListener('click', (event) => {
        let userId = button.dataset.user
        event.preventDefault()
        fetch(`/users/like/${userId}`, { method: 'POST' })
        .then((response) => response.json())
            .then(response => {
                console.log("JsonResponse recieved")
                console.log(response)
            })
            .catch((error) => {
                console.error('JSON response ERROR')
            })
        })}
    for (let button of disLikeButtons){
  button.addEventListener('click', (event) => {
      let userId = button.dataset.user
    event.preventDefault()
    fetch(`/users/dislike/${userId}`, { method: 'POST' })
      .then((response) => response.json())
            .then(response => {
                console.log("JsonResponse recieved")
                console.log(response)
            })
            .catch((error) => {
                console.error('JSON response ERROR')
            })
  })
}}

LikeOrDislike()