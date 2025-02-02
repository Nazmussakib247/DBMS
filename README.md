# Login System with Account Registration (Integrated with XAMPP)

This project demonstrates a simple **login and registration system** using **PHP** and **MySQL**. The data is stored in a database via **XAMPP**. Users can register an account, and the system will save the information in the database, allowing users to log in afterward.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [File Structure](#file-structure)

## Prerequisites

Before running this project, ensure you have the following installed:

- **XAMPP** (Apache, MySQL, PHP)
- A web browser (e.g., Chrome, Firefox)
- Basic knowledge of PHP and MySQL

## Installation

1. **Clone or Download the Repository**  
   Clone or download the repository into your `htdocs` directory inside your XAMPP installation folder (`C:\xampp\htdocs\`).

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   ```

2. **Start XAMPP Services**  
   Open XAMPP Control Panel and start both **Apache** and **MySQL** services.

## Database Setup

1. **Access phpMyAdmin**  
   Open your browser and go to `http://localhost/phpmyadmin/` to access the phpMyAdmin interface.

2. **Create a Database**  
   - In phpMyAdmin, click on **New** to create a new database.
   - Name the database (e.g., `userdb`).
   - Set the collation to **utf8_general_ci** and click **Create**.

3. **Create a Users Table**  
   After creating the database, create a table to store user information (e.g., username, email, and password). Use the following SQL query to create the table:

   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL,
       email VARCHAR(100) NOT NULL,
       password VARCHAR(255) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

4. **Configure Database Connection**  
   Open the `db.php` file and modify the database connection settings:

   ```php
   $servername = "localhost";
   $username = "root";
   $password = "";
   $dbname = "userdb";

   // Create connection
   $conn = new mysqli($servername, $username, $password, $dbname);

   // Check connection
   if ($conn->connect_error) {
       die("Connection failed: " . $conn->connect_error);
   }
   ```

## Usage

1. **Register an Account**  
   Open your browser and go to `http://localhost/your-folder-name/index.php` to access the registration form. Fill in the required fields (e.g., username, email, and password) to create a new account. The user details will be stored in the database.

2. **Login to the System**  
   After registration, go to the login form (in `index.php`) and log in with the registered username and password.

3. **Welcome Page**  
   After successful login, you will be redirected to the `welcome.php` page, which displays a simple welcome message.

## File Structure

```
/your-project-folder
│
├── index.php        # User registration and login form
├── db.php           # Database connection file
└── welcome.php      # Welcome page after successful login
```

- **`index.php`**: Contains the registration and login forms, along with the PHP code to handle form submissions.
- **`db.php`**: Contains the database connection logic.
- **`welcome.php`**: Displays a welcome message after successful login.
