let popup_1 = document.getElementById("popup_1");
popupToggle = document.getElementById("popup_1");
popupClose = document.querySelector(".close");
popupToggle.onclick = function() {
    popup_1.style.display="none";
};
popupClose.onclick = function() {
    popup_1.style.display="none";
};
window.onclick = function (e) {
    if(e.target == popup_1) {
        popup_1.style.display="none";
    }
};