const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");

function uploadImage() {
    let imgFile = inputFile.files[0];
    if (imgFile) {
        let imgLink = URL.createObjectURL(imgFile);
        imageView.style.backgroundImage = `url(${imgLink})`;
        imageView.textContent = '';
    }
}


inputFile.addEventListener("change", function() {
    uploadImage();
});

dropArea.addEventListener("dragover", function(e) {
    e.preventDefault();
    dropArea.classList.add('dragover');
});

dropArea.addEventListener("dragleave", function(e) {
    e.preventDefault();
    dropArea.classList.remove('dragover');
});

dropArea.addEventListener("drop", function(e) {
    e.preventDefault();
    dropArea.classList.remove('dragover');

    inputFile.files = e.dataTransfer.files;
    uploadImage();
});
