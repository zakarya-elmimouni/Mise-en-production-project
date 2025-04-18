import pandas as pd
import s3fs


class S3DataLoader:
    def __init__(self, bucket: str, endpoint_url: str = "https://minio.lab.sspcloud.fr"):
        self.bucket = bucket
        self.endpoint_url = endpoint_url
        self.fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": endpoint_url})

    def load_csv(self, file_path: str) -> pd.DataFrame:
        # Chargement du CSV depuis S3
        with self.fs.open(f"s3://{self.bucket}/{file_path}") as f:
            df = pd.read_csv(f)

        # Affichage recap
        print(f"\nRésumé du fichier: {file_path}")
        print("-" * 50)
        print(f"Nombre de lignes: {df.shape[0]}")
        print(f"Nombre de variables: {df.shape[1]}")
        print("-" * 50)
        print()

        return df
