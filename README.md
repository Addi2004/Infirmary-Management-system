# Infirmary Management System

Welcome to the Infirmary Management System project! This system is designed to manage the inventory of medical products, book appointments with doctors, and maintain patient records. It is built using Python and Streamlit for the frontend interface, and MySQL for the backend database.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

### For Patients
- Buy Medicine
- Book Appointment
- Display All Products

### For Doctors
- View Appointments
- View Patient Details

### For Managers
- Update Stock
- Display All Products

## Installation

### Prerequisites
- Python 3.x
- MySQL
- Streamlit

### Steps
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/infirmary-management-system.git
    cd infirmary-management-system
    ```

2. **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the MySQL database:**
    - Create a database named `infirmary`.
    - Create tables using the SQL commands in the project.

4. **Configure the database connection:**
    - Update the database connection details in `maintry2working.py`:
    ```python
    self.db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="infirmary"
    )
    ```

## Usage

### Running the Streamlit App

1. **Start the Streamlit server:**
    ```sh
    streamlit run app.py
    ```

2. **Open the app in your browser:**
    - Navigate to the URL provided by Streamlit, usually `http://localhost:8501`.

### Navigating the App
- **Patient:**
    - Choose "Patient" from the sidebar.
    - Select an action: Buy Medicine, Book Appointment, or Display All Products.
- **Doctor:**
    - Choose "Doctor" from the sidebar.
    - Select an action: View My Appointments or View Patient Details.
- **Manager:**
    - Choose "Manager" from the sidebar.
    - Enter the manager password to access management features like updating stock.

## Project Structure

```
infirmary-management-system/
│
├── app.py                     # Streamlit frontend interface
├── maintry2working.py         # Backend logic for the system
├── requirements.txt           # List of required Python packages
└── README.md                  # Project README file
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a new branch:**
    ```sh
    git checkout -b feature/your-feature
    ```
3. **Make your changes and commit:**
    ```sh
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```sh
    git push origin feature/your-feature
    ```
5. **Create a pull request**

## License

This project is licensed under the MIT License. See the LICENSE file for details.