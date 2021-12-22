
//s = document.querySelector("#xGrid").innerHTML
//console.log(s)
canvasWigth=1600
hanvasHeight=1200

let step = canvasWidth/10
let s = ""

for(let i = 1; i < 10;i++) {
    x = i*step
    y1 = 0
    y2 = canvasHeight
    s += `<line x1=${x} x2=${x} y1=${y1} y2=${y2}></line>`
}
document.querySelector("#xGrid").innerHTML = s

step = canvasHeight/10
s = ""
x1 = 0
x2 = canvasWidth


for(let i = 0; i < 10;i ++) {
    y1 = i*step
    y2 = i*step
    s += `<line x1=${x1} x2=${x2} y1=${y1} y2=${y2}></line>`
}
document.querySelector("#yGrid").innerHTML = s

for(let i=1;i<10;i++) {
    x=i*step
    y=100+Math.sin(i/5)*300
    s += `<circle cx=${x} cy=${y} data-value=${y} r="5"></circle>`
}
document.querySelector("#graphic").innerHTML = s
