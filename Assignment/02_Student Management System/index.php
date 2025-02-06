<?php 
include 'php/functions.php'; 
if ($_SERVER['REQUEST_METHOD'] === 'POST') { 
if (isset($_POST['add'])) { 
addStudent($_POST['name'], $_POST['roll_number'], $_POST['department'], $_POST['email'], 
$_POST['contact']); 
} elseif (isset($_POST['update'])) { 
updateStudent($_POST['id'], $_POST['name'], $_POST['roll_number'], $_POST['department'], 
$_POST['email'], $_POST['contact']); 
} elseif (isset($_POST['delete'])) { 
deleteStudent($_POST['id']); 
} 
} 
$students = getStudents(); 
?> 
<!DOCTYPE html> 
<html lang="en"> 
<head> 
<meta charset="UTF-8"> 
<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
<link rel="stylesheet" href="css/style.css"> 
<title>Student Management System</title> 
</head> 
<body> 
    <h1>Student Management System</h1> 
    <form method="post"> 
        <input type="text" name="name" placeholder="Name" required> 
        <input type="text" name="roll_number" placeholder="Roll Number" required> 
        <input type="text" name="department" placeholder="Department"> 
        <input type="email" name="email" placeholder="Email"> 
        <input type="text" name="contact" placeholder="Contact Number"> 
        <button type="submit" name="add">Add Student</button> 
    </form> 
 
    <table> 
        <thead> 
            <tr> 
                <th>ID</th> 
                <th>Name</th> 
                <th>Roll Number</th> 
                <th>Department</th> 
                <th>Email</th> 
                <th>Contact</th> 
                <th>Actions</th> 
            </tr> 
        </thead> 
        <tbody> 
            <?php foreach ($students as $student): ?> 
            <tr> 
                <td><?= $student['id'] ?></td> 
                <td><?= $student['name'] ?></td> 
                <td><?= $student['roll_number'] ?></td> 
                <td><?= $student['department'] ?></td> 
                <td><?= $student['email'] ?></td> 
                <td><?= $student['contact_number'] ?></td> 
                <td> 
                    <form method="post" style="display:inline;"> 
                        <input type="hidden" name="id" value="<?= $student['id'] ?>"> 
                        <button type="submit" name="delete">Delete</button> 
                    </form> 
                </td> 
            </tr> 
            <?php endforeach; ?> 
        </tbody> 
    </table> 
</body> 
</html>