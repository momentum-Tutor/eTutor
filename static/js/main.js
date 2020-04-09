(function ($) {
  $(function () {
    $('nav ul li a:not(:only-child)').click(function (e) {
      $(this).siblings('.nav-dropdown').toggle()
      $('.nav-dropdown').not($(this).siblings()).hide()
      e.stopPropagation()
    })
    $('html').click(function () {
      $('.nav-dropdown').hide()
    })
    $('#nav-toggle').click(function () {
      $('nav ul').slideToggle()
    })
    $('#nav-toggle').on('click', function () {
      this.classList.toggle('active')
    })
  })
})(jQuery)

$(document).ready(function () {
  $('#myInput').on('keyup', function () {
    var value = $(this).val().toLowerCase()
    $('#myList li').filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
  })
})

let totalNotification = document.querySelector('#total-notification')
let dmNotification = document.querySelector('#DM-notification')
let frNotification = document.querySelector('#FR-notification')

function notifications () {
  fetch('/notification/get/', {
    method: 'GET',
    headers: { 'Content-type': 'application/json' },
  })
    .then((response) => response.json())
    .then(data => {
      console.log('works')
      displayNotifications(data)
    })
    .catch((error) => {
      console.error('notifications failed')
    })
  function displayNotifications (data) {
    if (data.total > 0) {
      totalNotification.setAttribute('class', 'etutor-notification')
      totalNotification.innerText = data.total
    } else {
      totalNotification.classList.remove('etutor-notification')
      totalNotification.innerText = ''
    }
    if (data.total > 0) {
      dmNotification.setAttribute('class', 'etutor-notification')
      dmNotification.innerText = data.dm
    } else {
      dmNotification.classList.remove('etutor-notification')
      dmNotification.innerText = ''
    }
    if (data.total > 0) {
      frNotification.setAttribute('class', 'etutor-notification')
      frNotification.innerText = data.friend
    } else {
      frNotification.classList.remove('etutor-notification')
      frNotification.innerText = ''
    }
  }
}

notifications()

setInterval(notifications, 5000)

function LikeOrDislike () {
  console.log('LikeOrDislike')
  const likeButtons = document.querySelectorAll('.like')
  const disLikeButtons = document.querySelectorAll('.dislike')

  for (const button of likeButtons) {
    button.addEventListener('click', (event) => {
      const userId = button.dataset.user
      event.preventDefault()
      fetch(`/users/like/${userId}`, { method: 'POST' })
        .then((response) => response.json())
        .then(response => {
          console.log('JsonResponse recieved')
          console.log(response)
        })
        .catch((error) => {
          console.error('JSON response ERROR')
        })
    })
  }
  for (const button of disLikeButtons) {
    button.addEventListener('click', (event) => {
      const userId = button.dataset.user
      event.preventDefault()
      fetch(`/users/dislike/${userId}`, { method: 'POST' })
        .then((response) => response.json())
        .then(response => {
          console.log('JsonResponse recieved')
          console.log(response)
        })
        .catch((error) => {
          console.error('JSON response ERROR')
        })
    })
  }
}

LikeOrDislike()