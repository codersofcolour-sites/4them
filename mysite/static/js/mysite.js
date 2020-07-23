/* Traffic Count setInterval */
var trafficCountIncrement = 0;
var trafficCountElement = document.querySelector('.traffic-count');

function writeTrafficCount() {
  if (trafficCountIncrement == 1) {
    trafficCountElement.innerText = trafficCountIncrement + ' Children died since visiting this site';
  }
  else {
    trafficCountElement.innerText = trafficCountIncrement + ' Children died since visiting this site';
  }
}

if (sessionStorage.getItem('trafficCountIncrement')) {
  trafficCountIncrement = sessionStorage.getItem('trafficCountIncrement');
  writeTrafficCount()
}

setInterval(increaseTrafficCount, 15000);

function increaseTrafficCount() {
  trafficCountIncrement++;
  sessionStorage.setItem('trafficCountIncrement', trafficCountIncrement)
  writeTrafficCount()
}

/* Timer */
var timerIncrement = 15;
var timerElement = document.querySelector('.timer');

setInterval(decreaseTimer, 1000);

function decreaseTimer() {
  timerIncrement--;
  timerElement.innerText = timerIncrement + 's';
  if (timerIncrement == 0) {
    timerIncrement = 15;
  }
}