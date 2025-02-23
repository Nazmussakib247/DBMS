Deadlock-Free Resource Allocation System

Project Overview

This project implements a Deadlock-Free Resource Allocation System using the Banker's Algorithm. The system ensures safe resource allocation while preventing deadlocks. The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

Features

Implements Banker's Algorithm for deadlock-free resource allocation.

User-friendly GUI built with HTML, CSS, and JavaScript.

Real-time computation of safe sequences.

Displays allocation results dynamically.

Installation Guide

Prerequisites

Ensure you have the following installed on your system:

Python (>= 3.7)

Flask

pip (Python package manager)

Installation Steps

Clone the Repository:

git clone https://github.com/Nazmussakib247/Deadlock-Free-Resource-Allocation.git
cd Deadlock-Free-Resource-Allocation

Create a Virtual Environment (Optional but Recommended):

python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

Install Dependencies:

pip install -r requirements.txt

Run the Flask Application:

python app.py

Access the Web Application:
Open your browser and go to:

http://127.0.0.1:5000

Usage Guide

Enter the number of processes and resources.

Provide the allocation and maximum resource matrix.

Click the 'Compute Safe Sequence' button to check if a safe sequence exists.

View the results dynamically in the UI.

Folder Structure

Deadlock-Free-Resource-Allocation/
│-- app.py
│-- static/
│   ├── style.css
│   ├── script.js
│-- templates/
│   ├── index.html
│-- requirements.txt
│-- README.md
│-- instruction.txt

Contribution

Feel free to contribute to this project by submitting pull requests or reporting issues.

License

This project is licensed under the MIT License.

