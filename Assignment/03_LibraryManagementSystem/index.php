<?php
include 'php/functions.php';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
if (isset($_POST['add'])) {
addBook($_POST['title'], $_POST['author'], $_POST['isbn'], $_POST['genre'],
$_POST['status']);
} elseif (isset($_POST['update'])) {
updateBook($_POST['id'], $_POST['title'], $_POST['author'], $_POST['isbn'], $_POST['genre'],
$_POST['status']);
} elseif (isset($_POST['delete'])) {
deleteBook($_POST['id']);
}
}
$books = getBooks();

?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/style.css">
<title>Library Management System</title>
</head>
<body>
<h1>Library Management System</h1>
<form method="post">
<input type="text" name="title" placeholder="Book Title" required>
<input type="text" name="author" placeholder="Author" required>
<input type="text" name="isbn" placeholder="ISBN" required>
<input type="text" name="genre" placeholder="Genre">
<select name="status">
<option value="Available">Available</option>
<option value="Checked Out">Checked Out</option>
</select>
<button type="submit" name="add">Add Book</button>
</form>

<table>
<thead>
<tr>

<th>ID</th>
<th>Title</th>
<th>Author</th>
<th>ISBN</th>
<th>Genre</th>
<th>Status</th>
<th>Actions</th>
</tr>
</thead>
<tbody>
<?php foreach ($books as $book): ?>
<tr>
<td><?= $book['id'] ?></td>
<td><?= $book['title'] ?></td>
<td><?= $book['author'] ?></td>
<td><?= $book['isbn'] ?></td>
<td><?= $book['genre'] ?></td>
<td><?= $book['availability_status'] ?></td>
<td>
<form method="post" style="display:inline;">
<input type="hidden" name="id" value="<?= $book['id'] ?>">
<button type="submit" name="delete">Delete</button>
</form>
</td>
</tr>
<?php endforeach; ?>
</tbody>

</table>
</body>
</html>
