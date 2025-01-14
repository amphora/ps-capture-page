#!/usr/bin/env python3

import argparse
import requests

def parse_arguments():
    parser = argparse.ArgumentParser(description='Capture a web page in PatentSafe')
    
    # Required arguments
    parser.add_argument('--server', 
                       required=True,
                       help='The URL of your PatentSafe server')
    parser.add_argument('--username',
                       required=True,
                       help='Your PatentSafe username')
    parser.add_argument('url',
                       metavar='URL_TO_CAPTURE',
                       help='The URL of the webpage to capture')
        
    args = parser.parse_args()
        
    return args

def main():
    args = parse_arguments()
    
    # Prepare the data for the POST request body
    data = {
        'authorId': args.username,
        'url': args.url
    }
    
    submit_url = f"{args.server.rstrip('/')}/submit/http_retrieval"
    
    try:
        # Make the POST request with data in the body instead of params
        response = requests.post(
            submit_url,
            json=data,  # Changed from params to json to send in request body
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        # Print the response
        print(response.text)
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        exit(1)

if __name__ == '__main__':
    main()

