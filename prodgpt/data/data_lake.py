from google.cloud import storage


class DataLake:
    def __init__(
        self,
        bucket_name: str
    ):
        storage_client = storage.Client()

        self.bucket_name = bucket_name
        self.bucket = storage_client.bucket(bucket_name)

    def is_file_exists(self, path: str) -> bool:
        blob = self.bucket.blob(path)
        return blob.exists()

    def upload_single_file(
        self,
        src_path: str,
        dest_path: str
    ):
        blob = self.bucket.blob(dest_path)
        blob.upload_from_filename(src_path)
        return blob

    def retrieve_single_file(self, path: str) -> str:
        blob = self.bucket.blob(path)
        return blob.download_as_string()

    def delete_single_file(self, path: str):
        blob = self.bucket.blob(path)
        return blob.delete()

    def download(self, src_path: str, dest_path: str):
        blob = self.bucket.blob(src_path)
        return blob.download_to_filename(dest_path)
