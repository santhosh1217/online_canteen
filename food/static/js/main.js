var hours = 24;

var myDate = new Date();
var myTime = myDate.getTime();
var stepTime = localStorage.getItem('stepTime'); 

if (stepTime == null){
    localStorage.setItem('stepTime',myTime);
}
else{ 
    if (myTime - stepTime > hours*60*60*1000){
        localStorage.clear();
        localStorage.setItem('stepTime', myTime);
    }
}

var orders = JSON.parse(localStorage.getItem('orders'));
var total = localStorage.getItem('total');

if (orders === null|| orders === undefined){
    localStorage.setItem('orders',JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if (total === null|| total === undefined){
    localStorage.setItem('total',0);
    total = (localStorage.getItem('total'));
}

var cart = document.querySelector("#cart");
cart.innerHTML= orders.length;
