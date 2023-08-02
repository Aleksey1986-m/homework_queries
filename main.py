# dz № 2
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for file in path_to_file:
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'path': file}
            headers = {'Authorization': token}
            res = requests.get(url, params=params, headers=headers)
            url_for_upload = res.json().get('href', '')
            with open(file, 'rb') as f:
                requests.put(url_for_upload, files={'file': f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ['кубики.png']
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
