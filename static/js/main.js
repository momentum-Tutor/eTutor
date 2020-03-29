(function ($) {
  $(function () {
    $('nav ul li a:not(:only-child)').click(function (e) {
      $(this).siblings('.nav-dropdown').toggle()
      $('.dropdown').not($(this).siblings()).hide()
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
  $('#searchBar').on('keyup', function () {
    var value = $(this).val().toLowerCase()
    $('#usersList li').filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
  })
})
