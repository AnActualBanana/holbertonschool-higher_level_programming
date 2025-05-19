# 0x0C. Python - Network #1

This project continues the exploration of networking concepts in Python, focusing on using the `requests` and `urllib` libraries to interact with APIs, handle HTTP responses, and manipulate headers, errors, and JSON data.

## 📚 Learning Objectives

By the end of this project, you will be able to:

- Send HTTP requests with Python using both `urllib` and `requests`
- Fetch and parse response headers
- Handle HTTP error codes
- Submit form data via POST requests
- Work with JSON responses and dynamic APIs
- Use GitHub API tokens for authentication

## 🛠️ Project Structure

<details>
<summary>📂 Python Scripts</summary>

- `0-hbtn_status.py` — Fetches status from a given URL using `urllib`  
- `1-hbtn_header.py` — Retrieves the value of the `X-Request-Id` header from a response  
- `2-post_email.py` — Sends a POST request with an email parameter and displays the response  
- `3-error_code.py` — Handles HTTP error codes and prints response body  
- `4-hbtn_status.py` — Similar to task 0, but using `requests` library  
- `5-hbtn_header.py` — Retrieves the `X-Request-Id` header using `requests`  
- `6-post_email.py` — Sends POST request with an email using `requests`  
- `7-error_code.py` — Handles HTTP errors using `requests`  
- `8-json_api.py` — Sends a POST request to a dynamic API and parses the JSON response  
- `10-mygithub.py` — Uses GitHub API and Basic Auth to display the user ID  
- `10-my_github.py` — (Renamed duplicate of the above)

</details>

- `README.md` — This documentation

## 🔧 Requirements

- Python 3.x
- `requests` module (for tasks using it)
- PEP8 compliance
- No hardcoded URIs or tokens

## ▶️ Usage

Each script can be run individually using:

```bash
python3 script_name.py [arguments]
```

## Author
Logan McClain
