var btn = document.querySelector('button')
var body = document.querySelector('body')
var nav = document.querySelector('nav')

btn.onclick = () => {

  body.classList.toggle('dark')
  nav.classList.toggle('dark_nav')
  var a = document.querySelectorAll('a')
  for (var i = 0; i < a.length; i++) {
    
    // Tab to edit
    a[i].style.color = 'black'
    btn.style.background = 'white'
  }
}