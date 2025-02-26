import boto3
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine

# Configuration MinIO (S3 local)
MINIO_ENDPOINT = "http://localhost:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
BUCKET_NAME = "poorman-datalake"
FILE_KEY = "submissions.csv"

# Connexion à PostgreSQL (remplacez par vos identifiants)
DATABASE_URI = "postgresql+psycopg2://username:password@localhost:5432/music_dw"
engine = create_engine(DATABASE_URI)

# Étape 1 : Extraction des données depuis MinIO (S3 local)
print("Extraction des données depuis MinIO...")
s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
)
response = s3_client.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
data = response['Body'].read().decode('utf-8')

# Charger les données dans un DataFrame Pandas
df = pd.read_csv(StringIO(data))
print("Données brutes extraites :")
print(df)

# Étape 2 : Transformation des données (garder uniquement 'submit')
print("\nTransformation des données...")
df_transformed = df[df['submission_status'] == 'submit']
print("Données transformées :")
print(df_transformed)

# Étape 3 : Chargement dans PostgreSQL
print("\nChargement des données dans PostgreSQL...")
df_transformed.to_sql('submissions', engine, if_exists='append', index=False)
print("Chargement terminé avec succès.")
