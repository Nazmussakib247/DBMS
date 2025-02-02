<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "DBMS_Assignment_User_management";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
