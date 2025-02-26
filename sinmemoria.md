minio server ~/minio_data --console-address ":9001"

#send data to monio 
mc alias set local http://localhost:9000 minioadmin minioadmin
mc cp submissions.csv local/poorman-datalake/

exec pipeline

#pgadmin

