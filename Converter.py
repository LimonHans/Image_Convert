CC_details = \
'''
#############################
#    Project:: Converter    #
#  Developed by HansLimon.  #
#                           #
#    Created: 2024/01/14    #
# Last modified: 2024/01/26 #
#############################
'''
import os
import sys
import json
import requests
from time import sleep
from win10toast import ToastNotifier

access_token = ''
file_type = {
    # image part
    'fax': 'image/fax',
    'gif': 'image/gif',
    'ico': 'image/x-icon',
    'jfif': 'image/jpeg',
    'jpe': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'net': 'image/pnetvue',
    'png': 'image/png',
    'rp': 'image/vnd.rn-realpix',
    'tif': 'image/tiff',
    'tiff': 'image/tiff',
    'wbmp': 'image/vnd.wap.wbmp',
    # pdf
}
not_support_file_type = [
    # image part
    'wbmp'
]

file_dir = ''
file_path = ''
file_name = ''
input_type = ''
output_type = ''

def upload_file():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    result = requests.post('https://api.freeconvert.com/v1/process/import/upload', headers=headers)
    #print("%s"%result.json()['errors'][0]['message'])
    print("[INFO] Send upload request", result.json())
    task_id = result.json()['id']

    payload = {
        'signature': result.json()['result']['form']['parameters']['signature']
    }
    files = [('file', (file_name, open(file_path, 'rb'), file_type[file_path[file_path.rfind('.') + 1:]]))]
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    result = requests.request('POST', result.json()['result']['form']['url'], headers=headers, data=payload, files=files)
    print("[INFO] Upload", result.json())

    return task_id
def convert_image(task_id):
    request_body = {
        'input': task_id,
        'input_format': input_type,
        'output_format': output_type
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    result = requests.request('POST', 'https://api.freeconvert.com/v1/process/convert', headers=headers, data=json.dumps(request_body))
    print("[INFO] Send convert_image requirements", result.json())

    return result.json()['id']
def export_file(task_id):
    request_body = {
        'input': [task_id],
        'filename': file_name
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    while True:
        result = requests.request('POST', 'https://api.freeconvert.com/v1/process/export/url', data=json.dumps(request_body), headers=headers)
        print("[INFO] Send export request", result.json())
        if result.json()['status'] != 'created': break
        else: sleep(1)
    return result.json()['dependsOn'][0]['result']['url']
def download_file(file_url):
    result = requests.request('GET', file_url)
    with open(os.path.join(file_dir, file_name + '.' + output_type), 'wb') as otp:
        otp.write(result.content)
def SelfConfig():
    with open(file_path, 'r') as token_file:
        access_token = token_file.readline().strip('\n')
    token_data = {'access_token': access_token}
    with open(os.path.join('Converter_Config.json'), 'w') as config_file:
        json.dump(token_data, config_file)

if __name__ == '__main__':
    print(CC_details)

    file_path = sys.argv[1]
    file_dir, file_name = os.path.split(file_path)
    input_type = file_name[file_name.rfind('.') + 1:]
    file_name = file_name[:file_name.rfind('.')]
    #print(f"file_path:{file_path},\nfile_dir:{file_dir},\nfile_name:{file_name},\ninput_type:{input_type}")

    if file_name == 'converter_token':
        SelfConfig()
        toaster = ToastNotifier()
        toaster.show_toast("Converter", "Successfully set up configuration", duration = 2)
        exit(0)
    else:
        with open('Converter_Config.json', 'r') as config_file:
            token_data = json.load(config_file)
            access_token = token_data['access_token']

    output_type = input(f"[INFO] Enter the conversion type:\n{input_type} -> ")
    while output_type in not_support_file_type or (not (output_type in file_type)):
        output_type = input(f"[Warning] Couldn't convert, please try other types.\nConvert from: {input_type} -> ")

    now_id = upload_file()
    now_id = convert_image(now_id)
    now_url = export_file(now_id)
    download_file(now_url)

    toaster = ToastNotifier()
    toaster.show_toast("Converter", "Conversion Finished",
                       #icon_path="custom.ico",
                       duration = 2)