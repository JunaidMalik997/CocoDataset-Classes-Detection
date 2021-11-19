from filestack import Client

class FileSharer:

    def __init__(self, filepath, api_key='AGuAj1ssTGmkPEJ2S13zfz'):
        self.api_key=api_key
        self.filepath=filepath

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        # print(new_filelink)
        return new_filelink.url