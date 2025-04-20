import pandas as pd
from src.data.load_data import S3DataLoader

def test_fake_load_local_csv(tmp_path):
    # Simule un fichier CSV local
    csv_content = "feature1,feature2,target\n1,2,3\n4,5,6"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content)

    # Mock simple pour test local sans S3
    loader = S3DataLoader(bucket="dummy")
    df = pd.read_csv(file_path)

    assert not df.empty
    assert list(df.columns) == ["feature1", "feature2", "target"]
