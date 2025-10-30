// Your data
const userName = "Alice";

// Find the container div
const container = document.getElementById("date_item");

// Create a new HTML element (like a paragraph)
const userElement = document.createElement("p");

// Add the userName as text inside the paragraph
userElement.textContent = "User name: " + userName;

// Add the element to the page
container.appendChild(userElement);

