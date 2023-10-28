
import requests

with open('2022301004_AIML-3.pdf', 'r', encoding='utf-16') as f:
    file_content = f.read()
    files = {
        'file': ('filename.txt', file_content)
    }
    data = {
        'email': 'tejas@mail.com'
    }
    result = requests.post(
        f'https://7bf9-34-91-49-144.ngrok-free.app/upload_files', files=files, data=data)

    print(result.json())
