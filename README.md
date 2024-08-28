# Contact Book App

This is a simple Contact Book application built using Flask. It allows users to manage their contacts efficiently. This project was developed as part of the EcodeCamp Internship task.

## Key Features

- **Add Contacts**: Easily add new contacts with name, phone number, and email address.
- **Edit Contacts**: Update the details of existing contacts.
- **Delete Contacts**: Remove contacts from the database permanently.
- **Export Contacts**: Download the entire list of contacts as a CSV file.
- **Duplicate Prevention**: Ensures that no duplicate contacts are added by checking for the same phone number and email.
- **Responsive Design**: The app features a clean and responsive design, ensuring it works well on different devices.
- **Flash Messaging**: Provides user feedback via flash messages for actions like adding, editing, and deleting contacts.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed. You'll also need to install Flask and SQLAlchemy.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/contact_book_app.git
    cd contact_book_app
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Initialize the database**:

    ```bash
    python app.py
    ```

    The app will create the `contacts.db` database file.

### Running the Application

After setting up, you can run the application using:

```bash
python app.py
