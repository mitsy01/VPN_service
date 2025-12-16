var count = 0 
document.querySelector(".myButton").addEventListener("mouseover", function() {
    var messageDiv = document.querySelector(".message");
    messageDiv.innerHTML = `Privit ${count}` ;
    messageDiv.style.color = "green";
    count += 1;
})
//document.querySelector(".myButton").addEventListener("click", function() {
 //   alert("ere ")
//})