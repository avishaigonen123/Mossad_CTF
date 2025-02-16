const correctUsername = 'EliCopter';
const correctPasswordHash = '0e00b78c60d6fe3b76c6c9f70fcd0c5f'; 

// Function to compute MD5 hash
function md5(str) {
    return crypto.createHash('md5').update(str).digest('hex');
}

// Check if the request is a POST request
if (window.location.method === 'POST') {
    // Retrieve POST data (assuming the data comes as a JSON object in the body)
    let postData = JSON.parse(request.body);

    // Check if username and password are provided
    if (postData.username && postData.password) {
        const { username, password } = postData;

        // Compare provided username and password hash with the stored values
        if (username === correctUsername && md5(password) === correctPasswordHash) {
            // Authentication successful
            const response = { authenticated: true, redirect_url: 'capturedtheflag.html' };
            // Respond with 200 OK status and the JSON object
            return new Response(JSON.stringify(response), { status: 200 });
        } else {
            // Authentication failed
            const response = { authenticated: false };
            // Respond with 401 Unauthorized status
            return new Response(JSON.stringify(response), { status: 401 });
        }
    } else {
        // Invalid request: Missing username or password
        const response = { error: 'Invalid request' };
        // Respond with 400 Bad Request status
        return new Response(JSON.stringify(response), { status: 400 });
    }
} else {
    // Method not allowed
    const response = { error: 'Method not allowed' };
    // Respond with 405 Method Not Allowed status
    return new Response(JSON.stringify(response), { status: 405 });
}
