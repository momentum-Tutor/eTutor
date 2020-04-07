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