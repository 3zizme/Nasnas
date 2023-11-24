Nasnas - Captcha Bypass Tool

Description:
Nasnas is a versatile Captcha Bypass Tool designed to automate the process of solving captcha challenges commonly used in web applications. This Python script leverages Google Cloud's Vision API to recognize and extract text from captcha images, making it a valuable tool for various web scraping and automation tasks.

Features:

Generates random session IDs for captcha solving.
Makes HTTP requests to specified URLs with customizable headers.
Utilizes Google Cloud's Vision API for captcha image text extraction.
Filters and saves extracted text based on user-defined criteria.
Extracts both strings and numbers from the captcha text.
Customizable to suit different captcha challenges and use cases.
Usage:

Set up Google Cloud: Enable the Vision API, create a service account key, and configure authentication.

Customize the Script: Modify the script to set your desired header values and other parameters.

Run the Script: Execute the script with command-line arguments, specifying the number of requests, target URLs, header values, desired text length, and text type extraction options.

View Results: The script will retrieve and extract text from captcha images, saving the filtered results in a text file for your reference.

Nasnas simplifies the process of bypassing captchas, making it a valuable tool for web developers, researchers, and automation enthusiasts.


**Installation:
**

Ensure you have Python installed on your computer. If not, you can download and install it from the official Python website (https://www.python.org/downloads/).
Install the required Python packages using pip. Open your command prompt or terminal and run the following commands:
pip install requests
pip install google-cloud-vision

**Google Cloud Setup:
**
You need to set up a Google Cloud project and enable the Vision API. Follow the Google Cloud documentation to create a project and enable the Vision API: https://cloud.google.com/vision/docs/setup


**Authentication:
**
After enabling the Vision API, you'll need to create a service account key and set up authentication. Follow the Google Cloud documentation for creating a service account key and set the environment variable to point to the key file. Here's an example command for setting the environment variable (replace your-key.json with your actual key file):
export GOOGLE_APPLICATION_CREDENTIALS="your-key.json"


**Running the Script:
**
Open your command prompt or terminal.

Navigate to the directory where your script is located using the cd command.

Run the script with the desired command-line arguments. Here's an example of how to run it:

python your_script_name.py -n 10 -u https://example.com/captcha -v PHPSESSID -l 5 -es


**-n: Number of requests to generate.
-u: URL to request. You can provide multiple URLs separated by spaces.
-v: Header value for the Cookie header.
-l: Desired number of characters in the extracted text.
-es: Extract strings from the extracted text (optional).
-en: Extract numbers from the extracted text (optional).
Replace your_script_name.py with the actual name of your script.**

**Results:
**
The script will generate random session IDs and make requests to the specified URL(s) with the given header value.
If the requests are successful, it will extract text from the captcha images and save the results to a file called captcha_results.txt in the same directory as your script.
You can open the captcha_results.txt file to view the extracted text.


