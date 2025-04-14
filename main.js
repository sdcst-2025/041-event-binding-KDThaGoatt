var lobotomy = new Audio("lobotomy.mp3")
var carti = new Audio("SEEYUH.mp3")
var ye = new Audio("imevil.mp3")
var izzo = new Audio("swampizzo.mp3")
var chickjock = new Audio("chickenjocky.mp3")

function button1(e) {
lobotomy.cloneNode(true).play() 
}
function button2(e) {
carti.cloneNode(true).play()
}
function button3(e) {
ye.cloneNode(true).play()
}
function button4(e) {
izzo.cloneNode(true).play()
}
function button5(e) {
chickjock.cloneNode(true).play()
}
  
b = document.getElementById('div1')
b_action = b.addEventListener("click",button1)

b2 = document.getElementById('div2')
b2_action = b2.addEventListener("click",button2)

b3 = document.getElementById('div3')
b3_action = b3.addEventListener("click",button3)

b4 = document.getElementById('div4')
b4_action = b4.addEventListener("click",button4)

b5 = document.getElementById('div5')
  b5_action = b5.addEventListener("click",button5)