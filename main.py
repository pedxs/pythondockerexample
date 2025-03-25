import os
from flask import Flask, jsonify
import functions_framework

# Create a Flask app instance
app = Flask(__name__)

@functions_framework.http
def main(request):
    """Simple Hello World function for Cloud Run CI/CD demonstration.
    
    Args:
        request: HTTP request object.
        
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`.
    """
    # Get environment variables (useful for showing configuration in Cloud Run)
    environment = os.environ.get('ENVIRONMENT', 'development')
    
    # Return a simple JSON response
    return jsonify({
        "message": "Hello World!",
        "environment": environment,
        "service": "Cloud Run CI/CD Demo",
        "endpoints": {
            "/": "Returns this welcome message"
        }
    })

if __name__ == "__main__":
    # Development server - Not used in production
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))