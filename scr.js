// Get the modal
var modal = document.getElementById("myModal");
var modalImg = document.getElementById("img01");

function showFullImg(img){
  modal.style.display = "block";
  modalImg.src = img.src;
}

// Close
var span = document.getElementsByClassName("close")[0];
span.onclick = function() { 
  modal.style.display = "none";
}