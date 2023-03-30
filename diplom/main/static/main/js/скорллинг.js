"use strict";
document.getElementById('scrollonas').addEventListener('click', scrollToElement);

function scrollToElement(e) {
    let element = document.getElementById("zagolovokmain")
    element.scrollIntoView(true);
}

document.getElementById('scrollassort').addEventListener('click', scrollToElement);

function scrollToElement(e) {
    let element = document.getElementById("zagolovokassorti")
    element.scrollIntoView(true);
}