import requests

def open_read_file_using_with(file):
    try:
        with open(file, 'r') as open_file:
            for line in open_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print('File cannot be found. Please check your inputs', errmsg)
    finally:
        print('\n Execution completed')

def write_to_file(file, postcode):
    try:
        with open(file, 'a') as opened_file:
            request_postcode = requests.get('http://api.postcodes.io/postcodes/' + postcode)
            postcode = request_postcode.json()

            postcode_item = (postcode['result']['postcode'])
            opened_file.write(postcode_item + '\n')

    except FileNotFoundError:
        print('File not found')