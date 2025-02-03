<?php 
include 'config.php'; 
function addStudent($name, $roll_number, $department, $email, $contact) { 
global $conn; 
$sql = "INSERT INTO students (name, roll_number, department, email, contact_number) VALUES (?, ?, 
?, ?, ?)"; 
$stmt = $conn->prepare($sql); 
$stmt->bind_param('sssss', $name, $roll_number, $department, $email, $contact); 
$stmt->execute(); 
return $stmt->affected_rows > 0; 
} 
function getStudents() { 
global $conn; 
$result = $conn->query("SELECT * FROM students"); 
return $result->fetch_all(MYSQLI_ASSOC); 
} 
function updateStudent($id, $name, $roll_number, $department, $email, $contact) { 
global $conn; 
$sql = "UPDATE students SET name=?, roll_number=?, department=?, email=?, contact_number=? 
WHERE id=?"; 
$stmt = $conn->prepare($sql); 
$stmt->bind_param('sssssi', $name, $roll_number, $department, $email, $contact, $id); 
$stmt->execute(); 
return $stmt->affected_rows > 0; 
} 
function deleteStudent($id) { 
global $conn; 
$sql = "DELETE FROM students WHERE id=?"; 
$stmt = $conn->prepare($sql); 
$stmt->bind_param('i', $id); 
$stmt->execute(); 
return $stmt->affected_rows > 0; 
} 
?> 