<?php
// Replace with your actual username and password
$correctUsername = 'EliCopter';
$correctPassword = 'MossadRules';

// Check if the request is a POST request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve POST data
    $postData = json_decode(file_get_contents('php://input'), true);

    // Check if username and password are provided
    if (isset($postData['username']) && isset($postData['password'])) {
        $username = $postData['username'];
        $password = $postData['password'];

        // Simple authentication logic
        if ($username === $correctUsername && $password === $correctPassword) {
            // Authentication successful
            $response = array('authenticated' => true, 'redirect_url' => 'capturedtheflag.html');
            http_response_code(200);
        } else {
            // Authentication failed
            $response = array('authenticated' => false);
            http_response_code(401);
        }
    } else {
        // Invalid request
        $response = array('error' => 'Invalid request');
        http_response_code(400);
    }
} else {
    // Method not allowed
    $response = array('error' => 'Method not allowed');
    http_response_code(405);
}

// Return JSON response
header('Content-Type: application/json');
echo json_encode($response);
?>
