document.getElementById("loadPhotos").addEventListener("click", async () => {
    const response = await fetch("/photos");
    const photos = await response.json();

    const container = document.getElementById("photoContainer");
    container.innerHTML = "";

    photos.forEach(photo => {
        const img = document.createElement("img");
        img.src = photo.thumbnailUrl;
        img.style.margin = "10px";
        container.appendChild(img);
    });
});
