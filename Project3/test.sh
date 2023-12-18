#!/bin/bash

# Function to check if Flask server started successfully
check_server_running() {
    if ! ps -p $1 > /dev/null
    then
        echo "Failed to start Flask server. Exiting."
        exit 1
    fi
}

# Start the Flask server in the background
echo "Starting Flask server..."
python app.py &
SERVER_PID=$!

# Allow server a few seconds to start
sleep 5

# Check if server started successfully
check_server_running $SERVER_PID

# Run Newman tests
echo "Running Newman tests..."
if newman run path/to/your/postman_collection.json -e path/to/your/environment.json; then
    echo "Newman tests passed successfully."
else
    echo "Newman tests failed."
    kill $SERVER_PID
    exit 1
fi

# Shut down Flask server
echo "Shutting down Flask server..."
kill $SERVER_PID
