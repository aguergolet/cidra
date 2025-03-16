// (Place the JavaScript code from the previous response here)
fetch('http://localhost:5000/config')
  .then(response => response.json())
  .then(config => {
    // Update title and description
    document.title = config.title; 
    const description = document.createElement('p');
    description.textContent = config.description;

   // (Rest of the JavaScript code from previous response to create the menu)
   const sideMenu = document.createElement('ul');
    // ... (Add menu items as in the previous response)
    
    // Add the description and menu to the <app-root> element
    const appRoot = document.querySelector('app-root');  // Select the <app-root>
    appRoot.appendChild(description);                 // Append description
    appRoot.appendChild(sideMenu);                    // Append menu


  })
  .catch(error => {
    console.error('Error fetching config:', error);
    // Handle the error (e.g., show an error message)
  });