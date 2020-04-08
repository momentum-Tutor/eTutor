let newNotification = document.querySelectorAll('#new-notification')

newNotification.forEach((notification) => {
    if (notification.innerText == '') {
        notification.parentElement.removeChild(notification)
    }
})