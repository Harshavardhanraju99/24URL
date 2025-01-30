# 24URL Scanner

A Python script to scan a website URL and retrieve archived URLs from the Wayback Machine (web.archive.org) that match specific file extensions. The script checks the status codes of these URLs and allows the user to save the results to a file.

---

## Features

- **Automated Dependency Installation**: Checks and installs required Python packages automatically.
- **URL Validation**: Ensures the input URL is valid using the `validators` library.
- **Domain Extraction**: Extracts the domain from the provided URL and removes the `www.` prefix.
- **Wayback Machine Integration**: Queries the Wayback Machine's CDX API to retrieve archived URLs matching the domain and specific file extensions.
- **Concurrent URL Checking**: Uses `ThreadPoolExecutor` to check the status codes of retrieved URLs concurrently.
- **User-Friendly Interface**: Provides a clean and colored terminal output using the `colorama` library.
- **Save Results**: Allows the user to save the retrieved URLs to a file (`output.txt`).
- **Error Handling**: Gracefully handles interruptions and provides feedback for errors like timeouts or invalid URLs.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Install the required dependencies:
2.
 ```bash
pip install -r requirements.txt
Install the required dependencies:
Alternatively, the script will automatically check and install missing dependencies when run.
