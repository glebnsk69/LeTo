
//s = document.querySelector("#xGrid").innerHTML
//console.log(s)
minX = 0
maxX = 250
minY = -40
maxY = 40

function initParams(){
    Width=document.querySelector("svg").viewBox.baseVal.width
    Height=document.querySelector("svg").viewBox.baseVal.height
    
    xScale = Width/(maxX-minX)
    yScale = Height/(maxY-minY)
    _x0 = Math.abs(minX)*xScale
    _y0 = Math.abs(minY)*yScale
    xStep = 5
    yStep = 1
    shotMark = 5
    longMark = 10
    console.log(minY,yScale);
    //console.log(xScale,yScale)
}

initParams()    
xGreed()
yGreed()
xAxe()
yAxe()
redGraph()
blueGraph()
greenGraph()
//logElem("x==>","g#xGreed")
//logElem("y==>","g#yGreed")

function xGreed() {
    s = `<line x1=${0} x2=${Width} y1=${_y0} y2=${_y0}></line>`
    n = (maxX-minX)/xStep
    for(i = 1;i<n;i++) {
        s+=`<line x1=${_x(minX+i*xStep)} x2=${_x(minX+i*xStep)} y1=${_y(minY)} y2=${_y(maxY)}></line>`
    }
    document.querySelector("g#xGreed").innerHTML = s    
}

function yGreed() {
    s = `<line x1=${_x0} x2=${_x0} y1=${0} y2=${Height}></line>`
    n=(maxY-minY)/yStep
//    console.log(n,_x0,_y0)
    for(i=1;i<n;i++) {
        s+=`<line x1=${_x(minX)} x2=${_x(maxX)} y1=${_y(minY+i*yStep)} y2=${_y(minY+i*yStep)}></line>`
    }
    document.querySelector("g#yGreed").innerHTML = s    
}

function logElem(msg,Elem) {
    console.log(msg,document.querySelector("g#yGreed").innerHTML)
}

function xAxe() {
    s = `<line x1=${0} x2=${Width} y1=${_y0} y2=${_y0}></line>`
    n = (maxX-minX)/xStep
    startX = _x0/xScale
    for(i = 1;i<n;i++) {
        if(i%10==0) mark = longMark
        else mark = shotMark
        s+=`<line x1=${_x(minX+i*xStep)} x2=${_x(minX+i*xStep)} y1=${_y0-mark} y2=${_y0+mark}></line>`
    }
    document.querySelector("g#xAxe").innerHTML = s

}

function yAxe(){
    s = ""
    if(_x0>0) {
    s = `<line x1=${_x0} x2=${_x0} y1=${0} y2=${Height}></line>`
    }
    n=(maxY-minY)/yStep
    //console.log(n,_x0,_y0)
    for(i=1;i<n;i++) {
        if(i%10==0) {
            mark = longMark
            if(minY+i*yStep !=0) 
                s+=`<text x=${_x0+mark*1.5} y=${_y(minY+i*yStep)+5} class="small">${minY+i*yStep}</text>`
        }
        else mark = shotMark
        s+=`<line x1=${_x0-mark} x2=${_x0+mark} y1=${_y(minY+i*yStep)} y2=${_y(minY+i*yStep)}></line>`
    }
    document.querySelector("g#yAxe").innerHTML = s
}

function _x(x) {
    return _x0+x*xScale
}
function _y(y) {
    return _y0 - y*yScale
}

function f(x) {
    return Math.sin(x/30)*40
}
function f2(x) {
    return Math.cos(x/30)*40
}

function f3(x) {
    return (Math.sin(x/30) * Math.cos(x/30)) * 40
}

function redGraph() {
    s = ""

    n=(maxX-minX)/xStep
    xOld=minX
    yOld=f(xOld)
    
    for(x = minX+xStep;x < maxX;x+=xStep) {
        y = f(x)
        s+=`<line x1=${_x(xOld)} x2=${_x(x)} y1=${_y(yOld)} y2=${_y(y)}></line>`
        xOld = x
        yOld = y
    }
    document.querySelector("g#redGraph").innerHTML = s
}

function blueGraph() {
    s = ""
    n=(maxX-minX)/xStep
    xOld=minX
    yOld=f2(xOld)
    
    for(x = minX+xStep;x < maxX;x+=xStep) {
        y = f2(x)
        s+=`<line x1=${_x(xOld)} x2=${_x(x)} y1=${_y(yOld)} y2=${_y(y)}></line>`
        xOld = x
        yOld = y
    }
    document.querySelector("g#blueGraph").innerHTML = s
}

function greenGraph() {
    console.log("GreenGraph")
    s = ""
    n=(maxX-minX)/xStep
    xOld=minX
    yOld=f3(xOld)
    
    for(x = minX+xStep;x < maxX;x+=xStep) {
        y = f3(x)
        s+=`<line x1=${_x(xOld)} x2=${_x(x)} y1=${_y(yOld)} y2=${_y(y)}></line>`
        xOld = x
        yOld = y
    }
    document.querySelector("g#greenGraph").innerHTML = s
}

function initArray(){
    A=[]
    console.log("start init array")

    for(i=0;i<300;i++) {
        x=Math.sin(i/10*2)*70+Math.cos(i/100)*15
        y=Math.cos(i/10)*70+Math.sin(i/100)*15
        A[i]={x,y}
    }
    return A
}

//showArray("g#greenGraph",initArray())

function showArray(elem,A) {
    s = ""
    for(i=1;i<A.length;i++) {
        s+=`<line x1=${_x(A[i-1].x)} x2=${_x(A[i].x)} y1=${_y(A[i-1].y)} y2=${_y(A[i].y)}></line>`        
    }
    
    document.querySelector(elem).innerHTML = s
}


function reDrawAll() {
    initParams()
    xGreed()
    yGreed()
    xAxe()
    yAxe()
    redGraph()
    blueGraph()
    greenGraph()
}