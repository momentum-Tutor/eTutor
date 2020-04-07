(function($) { 
  $(function() { 
    $('nav ul li a:not(:only-child)').click(function(e) {
      $(this).siblings('.nav-dropdown').toggle();
      $('.nav-dropdown').not($(this).siblings()).hide();
      e.stopPropagation();
    });
    $('html').click(function() {
      $('.nav-dropdown').hide();
    });
    $('#nav-toggle').click(function() {
      $('nav ul').slideToggle();
    });
    $('#nav-toggle').on('click', function() {
      this.classList.toggle('active');
    });
  }); 
})(jQuery); 

$(document).ready(function () {
  $('#searchBar').on('keyup', function () {
    var value = $(this).val().toLowerCase()
    $('#usersList li').filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
  })
})


let totalNotification = document.querySelector('#total-notification')
let dmNotification = document.querySelector('#DM-notification')
let frNotification = document.querySelector('#FR-notification')

function notifications() {
  fetch('/notification/get/', {
    method: 'GET',
    headers: {'Content-type': 'application/json',},
  })
  .then((response) => response.json())
  .then(data => {
    displayNotifications(data)
  })
  .catch((error) => {
    console.error('notifications failed')
    setTimeout(notifications(), 10000)
})
  function displayNotifications(data) {
    if (data.total > 0) {
      totalNotification.setAttribute('class', 'notification')
      totalNotification.innerText = data.total
    }
    else {
      totalNotification.classList.remove('notification')
      totalNotification.innerText = ''
    }
    if (data.total > 0) {
      dmNotification.setAttribute('class', 'notification')
      dmNotification.innerText = data.dm
    }
    else {
      dmNotification.classList.remove('notification')
      dmNotification.innerText = ''
    }
    if (data.total > 0) {
      frNotification.setAttribute('class', 'notification')
      frNotification.innerText = data.friend
    }
    else {
      frNotification.classList.remove('notification')
      frNotification.innerText = ''
    }
    
  }
}

notifications()
// setInterval(notifications, 3000)