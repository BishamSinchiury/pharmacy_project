const DocumentForm = document.getElementById("DocumentForm");
const token = localStorage.getItem("accessToken");

// Function to validate file extensions
function validateFileExtensions(fileList, allowedExtensions) {
    const allowed = allowedExtensions.map(ext => ext.toLowerCase());

    for (const file of fileList) {
        const fileExtension = file.name.split('.').pop().toLowerCase();
        if (!allowed.includes(fileExtension)) {
            return false;
        }
    }
    return true;
}

// Handle form submission
DocumentForm.addEventListener('submit', function(event) {
    event.preventDefault();

    // Get files from input fields
    const passport_sized_photo = document.getElementsByName('passport_sized_photo')[0]?.files[0];
    const signature = document.getElementsByName('signature')[0]?.files[0];
    const citizenship_front = document.getElementsByName('citizenship_front')[0]?.files[0];
    const citizenship_back = document.getElementsByName('citizenship_back')[0]?.files[0];
    const location_map = document.getElementsByName('location_map')[0]?.files[0];
    const selfie_with_citizenship = document.getElementsByName('selfie_with_citizenship')[0]?.files[0];

    // Filter out undefined values
    const fileList = [passport_sized_photo, signature, citizenship_front, citizenship_back, location_map, selfie_with_citizenship].filter(Boolean);

    // Allowed file extensions
    const allowedExtensions = ["jpg", "png"];

    // Validate file extensions
    if (!validateFileExtensions(fileList, allowedExtensions)) {
        console.error("Some files have invalid extensions. Only JPG and PNG are allowed.");
        return; // Stop further execution if validation fails
    }

    // Prepare FormData object
    const formData = new FormData();
    if (passport_sized_photo) formData.append('passport_sized_photo', passport_sized_photo);
    if (signature) formData.append('signature', signature);
    if (citizenship_front) formData.append('citizenship_front', citizenship_front);
    if (citizenship_back) formData.append('citizenship_back', citizenship_back);
    if (location_map) formData.append('location_map', location_map);
    if (selfie_with_citizenship) formData.append('selfie_with_citizenship', selfie_with_citizenship);

    // Send POST request with FormData
    fetch('http://127.0.0.1:8000/document-submit/', {
        method: 'POST',
        headers: {
            "Authorization": `Bearer ${token}`,
        },
        body: formData, // Send FormData directly
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data); // Log the success response
    })
    .catch(error => {
        console.error('Error:', error); // Log any errors
    });
});
