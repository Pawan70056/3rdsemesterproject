# AcadamiConnect

This project is a Django web application for managing courses and collecting feedback.

## Features

- **Course Management**: Create, edit, and manage courses, chapters, and content.
- **Feedback Collection**: Gather user feedback on course experiences.
- **User Enrollment**: Allow users to enroll in courses.

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
