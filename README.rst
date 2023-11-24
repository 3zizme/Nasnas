.. _nasnas:

Nasnas - Captcha Bypass Tool
============================

.. image:: https://img.shields.io/github/license/abnmadhiii/Nasnas
   :target: https://github.com/abnmadhiii/Nasnas/LICENSE

.. image:: https://img.shields.io/github/stars/abnmadhiii/Nasnas
   :target: https://github.com/abnmadhiii/Nasnas/stargazers

.. image:: https://img.shields.io/github/forks/abnmadhiii/Nasnas
   :target: https://github.com/abnmadhiii/Nasnas/network/members

.. image:: https://img.shields.io/github/issues/abnmadhiii/Nasnas
   :target: https://github.com/abnmadhiii/Nasnas/issues

Overview
--------

Nasnas is a versatile Captcha Bypass Tool designed to automate the process of solving captcha challenges commonly used in web applications. This Python script leverages Google Cloud's Vision API to recognize and extract text from captcha images, making it a valuable tool for various web scraping and automation tasks.

Features
--------

- Generates random session IDs for captcha solving.
- Makes HTTP requests to specified URLs with customizable headers.
- Utilizes Google Cloud's Vision API for captcha image text extraction.
- Filters and saves extracted text based on user-defined criteria.
- Extracts both strings and numbers from the captcha text.
- Customizable to suit different captcha challenges and use cases.

Example Captcha
---------------
This example captcha image demonstrates the type of captcha that "Nasnas" can bypass. It consists of a distorted alphanumeric code designed to prevent automated bots from accessing a website or service. Captchas like this one are commonly used to verify that a user is human.

.. image:: https://i.ibb.co/CmpCqnm/captcha-2-KA6-To3bz-Quwt-ACP6fuc-HR0n-BD.png
   :alt: Image Description
   :width: 300
   :align: center
.. image:: https://i.ibb.co/XDFSfnN/image.png
   :alt: Image Description
   :width: 300
   :align: center
.. image:: https://i.ibb.co/7rKD7RC/simplecaptcha.jpg
   :alt: Image Description
   :width: 300
   :align: center
To test the "Nasnas" tool, you can use this sample captcha image along with your desired headers and parameters to see how it successfully bypasses captchas and extracts valuable information.



Usage
-----

.. image:: https://i.ibb.co/8MxP3YB/Screenshot-189.png
   :alt: Image Description
   :width: 600
   :align: center

1. **Set up Google Cloud**: Enable the Vision API, create a service account key, and configure authentication.

2. **Customize the Script**: Modify the script to set your desired header values and other parameters.

3. **Run the Script**: Execute the script with command-line arguments, specifying the number of requests, target URLs, header values, desired text length, and text type extraction options.

   Example:

   .. code-block:: shell

      PS C:\> python Nasnas.py -n 100 -u "https://example.com/captcha.php?type=block" -v "PHPSESSID" -l 5 -en

   Output:

   .. code-block:: shell

      PHPSESSID: 80JSAm1EKrQ, Filtered text: 59279
      PHPSESSID: ZFjR96LS0JV, Filtered text: 55355
      PHPSESSID: Py5wNWTweyL, Filtered text: 29278
      PHPSESSID: 5TtPXbbgzHZ, Filtered text: 35244
      PHPSESSID: J6UnU8fIsC8, Filtered text: 05181
      PHPSESSID: y6ftJNCgoJd, Filtered text: 00100
      PHPSESSID: ikqZmZ4fwjc, Filtered text: 30403
      PHPSESSID: lg9qzyJBkwr, Filtered text: 89759
      PHPSESSID: uD92b0VeVia, Filtered text: 79824
      PHPSESSID: xsPwhOE4sXJ, Filtered text: 50324
      PHPSESSID: PwlSgtSEVzp, Filtered text: 98906

4. **View Results**: The script will retrieve and extract text from captcha images, saving the filtered results in a text file for your reference.

Nasnas simplifies the process of bypassing captchas, making it a valuable tool for web developers, researchers, and automation enthusiasts.




Installation
------------

1. Clone the repository:

   .. code-block:: sh

      git clone https://github.com/abnmadhiii/Nasnas.git

2. Install the required Python packages:

   .. code-block:: sh

      pip install -r requirements.txt

Configuration
-------------

Before running the script, ensure that you have set up Google Cloud and configured the required authentication.

- Enable the Google Cloud Vision API for your project.
- Create a service account key and save it as a JSON file.
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your service account key file.

Example:

.. code-block:: sh

   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service_account_key.json"

Customize the script by editing the parameters such as header values and text extraction options according to your needs.

Running the Script
------------------

To run the script, use the following command:

.. code-block:: sh

   python nasnas.py -n <num_requests> -u <urls> -v <header_value> -l <length> [-es] [-en]

- `-n` or `--num-requests`: Number of requests to generate.
- `-u` or `--urls`: URLs to request (space-separated if multiple).
- `-v` or `--header-value`: Header value for Cookie.
- `-l` or `--length`: Desired number of characters.
- `-es` or `--extract-strings`: Extract strings (optional).
- `-en` or `--extract-numbers`: Extract numbers (optional).

View the `captcha_results.txt` file for the extracted and filtered results.



Acknowledgments
---------------

Special thanks to the open-source community and libraries that made this project possible and chatgpt :).

By: (https://twitter.com/3zizMe_)

Please feel free to report any issues or suggest improvements by opening an issue on GitHub.
