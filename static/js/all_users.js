const userSelector = document.querySelectorAll('#user-selector')
const selfUser = document.querySelector('#self-user')

for (const user of userSelector) {
  const username = user.innerText.split(' ')[0]
  const generatedMessageSelector = document.querySelector(`#message-${username}`)
  const generatedFriendSelector = document.querySelector(`#friend-${username}`)
  generatedMessageSelector.addEventListener('click', function () {
    const arr = [username, selfUser.innerText]
    arr.sort()
    window.location.href = `/direct_message/${arr[0]}SPL${arr[1]}`
  })
  generatedFriendSelector.addEventListener('click', function () {
    const arr = [username, selfUser.innerText]
    arr.sort()
    sendFriendRequest(arr)
  })
}

function sendFriendRequest (arr) {
  if (arr[0] == selfUser.innerText) {
    const data = { user_one: arr[0], user_two: arr[1], accepted_one: 'True' }
    fetchRequest(data)
  } else {
    const data = { user_one: arr[0], user_two: arr[1], accepted_two: 'True' }
    fetchRequest(data)
  }
  function fetchRequest (data) {
    console.log(data)
    fetch('/users/friend_request', {
      method: 'POST',
      headers: { 'Content-type': 'application.json' },
      body: JSON.stringify(data)
    })
      .then((response) => response.json())
      .then(response => {
        console.log('JsonResponse recieved')
        console.log(response)
      })
      .catch((error) => {
        console.error('JSON response ERROR')
      })
  }
}
