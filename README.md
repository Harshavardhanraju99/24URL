
Copy
# 24URL Scanner

A Python script to scan a website URL and retrieve archived URLs from the 24URL (web.archive.org) that match specific file extensions. The script checks the status codes of these URLs and allows the user to save the results to a file.

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
   git clone https://github.com/Harshavardhanraju99/24URL.git
   cd 24URL
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
Alternatively, the script will automatically check and install missing dependencies when run.

Usage
Run the script:

bash
Copy
python script_name.py
Enter a valid website URL when prompted:

Copy
[?] Enter the website URL (e.g., https://google.com): https://example.com
The script will:

Fetch archived URLs from the Wayback Machine.

Display the URLs and their status codes.

Ask if you want to save the results to output.txt.

Example Output
Copy
[i] Checking for required packages...

[+] colorama is already installed.
[+] requests is already installed.
[+] validators is already installed.

[?] Enter the website URL (e.g., https://google.com): https://example.com

[i] Loading, please wait...

Starting the Scan on: example.com

(01) Found: https://example.com/file.pdf - Status code: 200
 → URL: https://web.archive.org/web/*/https://example.com/file.pdf

(02) Found: https://example.com/document.docx - Status code: 404
 → URL: https://web.archive.org/web/*/https://example.com/document.docx

[*] Scanning Finished.
[*] Total Found: 2
[*] Time Taken: 5.23 seconds

[?] Do you want to save the URLs to output.txt? (y/n) [default: n]: y
[+] URLs saved to output.txt
Requirements
Python 3.x

Packages: colorama, requests, validators

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Push your branch and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer
This tool is intended for educational and ethical purposes only. Use it responsibly and ensure you comply with the terms of service of the Wayback Machine and any other services used.

Author
Harsha Vardhan Raju

GitHub: Harshavardhanraju99

Copy

---

### Steps to Add to Your Repository:
1. Save the above content in a file named `README.md`.
2. Place it in the root directory of your repository (`24URL`).
3. Commit and push the file to GitHub:
   ```bash
   git add README.md
   git commit -m "Add README.md"
   git push origin main
Now your repository will have a professional and informative README.md file! 🚀
