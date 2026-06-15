# CloudMasonryJuniorCase
Junior Developer Case Assessment for CloudMasonry

Once the repository is cloned and dependencies are installed:
  Starting the Flask server will allow you to navigate to your local host in your browser:
  http://localhost:5000

How to Use the App
  1. Enter a keyword (e.g., “Mars”, “Curiosity”, “Galaxy”).
  2. Enter a start year and end year.
  3. Click Search.
  4. Browse the image gallery.
  5. Click any image to enlarge it.
  6. Click "X" to return to the gallery.
If no images match your search, the app will display a friendly message.

Error Handling
    - The application gracefully handles:
    - Missing keyword or year range
    - Invalid year formats
    - Start year > end year
    - NASA API downtime
    - NASA returning unexpected HTML instead of JSON
    - No images found
You will always see a clear message instead of a blank screen.
