import requests

def get_post_code(postcode):
    # try:
        request_postcode = requests.get('http://api.postcodes.io/postcodes/' + postcode)
        converted_postcode = request_postcode.json()
        postcode = (converted_postcode['result']['postcode'])
        return postcode
    # except ConnectionError:
    #     print('Not a valid URL')

def write_to_file(file, postcode_item):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(postcode_item + '\n')

    except FileNotFoundError:
        print('File not found')