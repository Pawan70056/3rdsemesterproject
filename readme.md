# AcadamiConnect

This project is a Django web application for managing courses and collecting feedback.

## Features

### 1. User Authentication
- Allow users to register accounts securely.
- Enable users to log in and log out securely.
- Implement password reset functionality.

### 2. Account Settings
- Enable users to change their passwords.
- Allow users to delete their accounts securely.

### 3. Course Management
- Create, edit, and manage courses.
- Organize courses into chapters and sections.
- Upload and manage course content, such as lectures, quizzes, and assignments.

### 4. Feedback Collection
- Collect user feedback on course experiences.
- Implement rating systems or surveys to gather user opinions and suggestions.
- Analyze feedback to improve course content and user experience.

### 5. User Enrollment
- Allow users to enroll in courses of their choice.
- Implement enrollment features, including joining, dropping, or registering for courses.
- Track enrolled users and their progress within courses.

### 6. Messaging System
- Implement a notification system using toast messages for various events (success, error, etc.).
- Display different types of messages (e.g., success, error) with custom colors and styles.

### 7. User Interface (UI) Enhancements
- Utilize Bootstrap for responsive design.
- Implement tabs for easy navigation between account settings and security sections.
- Enhance the user experience with interactive elements (e.g., forms, buttons).

### 8. Security Measures
- Implement secure password hashing.
- Use Django's built-in authentication features to secure user data.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Pawan70056/3rdsemesterproject.git
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - **Linux/macOS**:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser (admin) account:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage courses, feedback, and users.
- Users can enroll in courses by navigating to the respective course pages and clicking on the enroll button.
- Feedback submission forms are available for users to provide their course experiences.

## Contributing

For now, this is our Assignment, we can surely work on this in future.

## License

This project is licensed under the [MIT License](LICENSE).
