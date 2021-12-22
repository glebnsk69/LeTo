console.log("start")
let x_pos = 10
let y_pos = 10
let my_txt = "SVG-TEST"
//s = `<text x="${x_pos}" y="${y_pos}" font-size="30">${my_txt}</text>`
s = document.querySelector(".xxx").innerHTML

for (let index = 1; index < 2; index++) {
    y_pos = index*25
    my_txt = "SVG test x = " + x_pos + " y_pos = " + y_pos+" index = "+index
    s = s+`<text x="${x_pos}" y="${y_pos}" font-size="20">${my_txt}</text>`
    
}
document.querySelector(".xxx").innerHTML = s

x_pos = 10
y_pos = 50

for (let index = 1; index < 24; index++) {
    x_pos=index*25
    y_pos=150+Math.sin(index/3)*100
    s+=`<circle cx="${x_pos}" cy="${y_pos}" r="5" opacity="0.8" fill="lightblue"></circle>`

    
}

document.querySelector(".xxx").innerHTML = s
/*========================================*/ 
let map = new Map
for(let i=0;i<12;i++) {
    map.set(i,i*2)
}
console.log(map)
console.log(map[1])
console.log(map.size)

