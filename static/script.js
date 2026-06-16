// Search photos on button click
document.getElementById("searchBtn").addEventListener("click", async () => {
    const keyword = document.getElementById("keyword").value;
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;
    const feedback = document.getElementById("feedback");
    const gallery = document.getElementById("gallery");

    // Show loading message and clear previous content
    feedback.textContent = "Loading...";
    gallery.innerHTML = "";
    const yearStart = startDate.slice(0, 4);
    const yearEnd = endDate.slice(0, 4);

    // Make the API request
    const response = await fetch(`/search?q=${keyword}&media_type=image&yearStart=${yearStart}&yearEnd=${yearEnd}`);
    const data = await response.json();

    // Catch any errors
    if (data.error) {
        feedback.textContent = "Error: " + data.error;
        return;
    }

    // Check if any photos were found
    if (data.photos.length === 0) {
        feedback.textContent = "No images found for that date range.";
        return;
    }

    // Display the number of photos found
    feedback.textContent = `Found ${data.photos.length} images`;

    // Display each photo
    data.photos.forEach(photo => {
        const img = document.createElement("img");
        img.src = photo.img_src;

        img.addEventListener("click", () => openModal(photo.img_src));

        gallery.appendChild(img);
    });
});

// Modal logic
const modal = document.getElementById("modal");
const modalImg = document.getElementById("modalImg");
const closeModalBtn = document.getElementById("closeModal");

// Open the modal with the clicked image
function openModal(src) {
    modal.style.display = "flex";
    modalImg.src = src;
}

// Close the modal by clicking the close button or outside the image
closeModalBtn.onclick = () => modal.style.display = "none";
modal.onclick = () => modal.style.display = "none";

// Test Image
const cabImg = document.getElementById("cabPhoto");
cabImg.addEventListener("click", () => openModal(cabImg.src));