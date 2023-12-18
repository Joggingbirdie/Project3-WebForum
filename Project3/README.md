Name: Zhenbin Zhang Stevens ID:20018578

Flask Web Forum API Documentation
Overview

In this project, I created a backend for a web forum using Flask. This application enables user registration and login, and allows users to create, read, update, delete, and list forum posts. It's designed to provide a simple yet effective way for users to interact with the forum.
Setup and Running the Application

First, make sure Python and Flask are installed:

pip install Flask

To run the server, enter the following command in your terminal:

python app.py

API Endpoints
User Registration

    URL: /register
    Method: POST
    Body:
        username: String (required)
        password: String (required)
    Success Response:
        Code: 201
        Content: { msg: "User registered successfully" }
    Error Response:
        Code: 400
        Content: { err: "Missing username or password" } or { err: "Username already taken" }

User Login

    URL: /login
    Method: POST
    Body:
        username: String (required)
        password: String (required)
    Success Response:
        Code: 200
        Content: { token: "user_token" }
    Error Response:
        Code: 403
        Content: { err: "Invalid username or password" }

[... include other endpoints here ...]
Running Tests

I dedicated significant time to testing each API endpoint. Using Postman, I created a series of tests to ensure correct behavior for both successful operations and error cases. For automated testing, I set up Newman with Postman, which allowed me to run these tests in an automated fashion, ensuring that any changes to the code didn't break existing functionality.
Known Issues

    Currently, there is a minor bug in the user login system where tokens are not invalidated after a certain period. This is on my roadmap to fix in the next update.

Development Notes

I spent about 19 hours developing this project. One of the biggest challenges was ensuring robust error handling for the API endpoints. By testing each endpoint with various scenarios, I was able to identify and fix issues, leading to a more resilient application.
Extensions Implemented

    Threaded Discussions: I implemented an extension for threaded discussions. Users can now reply to existing posts, creating a thread. This feature enriches user interaction by allowing more structured conversations.

    User Profiles: Another extension added was user profiles. Users can now add more information to their profiles, such as a bio and a profile picture. This feature makes the forum more personal and engaging.

    Moderation Tools: To enhance forum management, I included moderation tools. Selected users can moderate discussions, delete inappropriate posts, and ban users who violate forum rules.

    Search Functionality: I also added a search functionality that allows users to search for posts based on keywords. This feature enhances the user experience by making it easier to find relevant discussions.

    Data Analytics Dashboard: Lastly, a data analytics dashboard for admins was implemented. It provides insights into user engagement and popular topics, helping in the strategic planning of forum content.