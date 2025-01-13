<?php
include 'db.php';

if (isset($_POST['register'])) {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $sql = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$password')";
    if ($conn->query($sql) === TRUE) {
        echo "<script>alert('Registration successful!');</script>";
    } else {
        echo "<script>alert('Error: " . $sql . " - " . $conn->error . "');</script>";
    }
}

if (isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $sql = "SELECT * FROM users WHERE email='$email'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if (password_verify($password, $row['password'])) {
            echo "<script>alert('Login successful! Redirecting to welcome page...');</script>";
            header("Location: welcome.php");
            exit();
        } else {
            echo "<script>alert('Invalid password.');</script>";
        }
    } else {
        echo "<script>alert('No user found with this email.');</script>";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login & Register</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            width: 400px;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .form-switch {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
        }
        .form-switch button {
            background: none;
            border: none;
            color: #007BFF;
            font-size: 16px;
            cursor: pointer;
        }
        .form-switch button.active {
            font-weight: bold;
            text-decoration: underline;
        }
        form {
            display: none;
        }
        form.active {
            display: block;
        }
        input[type="text"], input[type="email"], input[type="password"], button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007BFF;
            color: white;
            border: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="form-switch">
            <button id="show-login" class="active">Login</button>
            <button id="show-register">Register</button>
        </div>
        <form id="login-form" class="active" method="POST">
            <h2>Login</h2>
            <label>Email:</label>
            <input type="email" name="email" required>
            <label>Password:</label>
            <input type="password" name="password" required>
            <button type="submit" name="login">Login</button>
        </form>
        <form id="register-form" method="POST">
            <h2>Register</h2>
            <label>Username:</label>
            <input type="text" name="username" required>
            <label>Email:</label>
            <input type="email" name="email" required>
            <label>Password:</label>
            <input type="password" name="password" required>
            <button type="submit" name="register">Register</button>
        </form>
    </div>

    <script>
        const loginForm = document.getElementById('login-form');
        const registerForm = document.getElementById('register-form');
        const showLogin = document.getElementById('show-login');
        const showRegister = document.getElementById('show-register');

        showLogin.addEventListener('click', () => {
            loginForm.classList.add('active');
            registerForm.classList.remove('active');
            showLogin.classList.add('active');
            showRegister.classList.remove('active');
        });

        showRegister.addEventListener('click', () => {
            registerForm.classList.add('active');
            loginForm.classList.remove('active');
            showRegister.classList.add('active');
            showLogin.classList.remove('active');
        });
    </script>
</body>
</html>
