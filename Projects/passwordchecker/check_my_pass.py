import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'error fetching:{res.status_code} check the api and try again!')
    return res
def get_password_leak_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h== hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # check password if it exists in API response
    sha1=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5,tail =sha1[:5],sha1[5:]
    response=request_api_data(first5)
    return get_password_leak_count(response,tail)

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f"{password} was found the {count} times you should probabluy change password")
        else:
            print(f'{password} was not found')
    return 'done'
if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))
