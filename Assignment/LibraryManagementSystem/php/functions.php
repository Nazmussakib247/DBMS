php
<?php

include 'config.php';

function addBook($title, $author, $isbn, $genre, $status) {
global $conn;
$sql = "INSERT INTO books (title, author, isbn, genre, availability_status) VALUES (?, ?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param('sssss', $title, $author, $isbn, $genre, $status);
$stmt->execute();
return $stmt->affected_rows > 0;
}

function getBooks() {
global $conn;
$result = $conn->query("SELECT * FROM books");
return $result->fetch_all(MYSQLI_ASSOC);
}

function updateBook($id, $title, $author, $isbn, $genre, $status) {
global $conn;
$sql = "UPDATE books SET title=?, author=?, isbn=?, genre=?, availability_status=? WHERE
id=?";
$stmt = $conn->prepare($sql);
$stmt->bind_param('sssssi', $title, $author, $isbn, $genre, $status, $id);
$stmt->execute();
return $stmt->affected_rows > 0;
}

function deleteBook($id) {
global $conn;
$sql = "DELETE FROM books WHERE id=?";
$stmt = $conn->prepare($sql);
$stmt->bind_param('i', $id);
$stmt->execute();
return $stmt->affected_rows > 0;
}
?>