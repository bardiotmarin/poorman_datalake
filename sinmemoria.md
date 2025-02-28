# Minio & PostgreSQL Setup Guide

## 🚀 Minio Server Setup

### Linux/macOS
```sh
minio server ~/minio_data --console-address ":9001"
```

### Windows
```sh
C:\minio\minio.exe server C:\minio\data --console-address ":9001"
```

---

# Send Data to Minio

### Configure Minio Client (mc)
```sh
mc alias set local http://localhost:9000 minioadmin minioadmin
```

### Upload a File
```sh
mc cp submissions.csv local/poorman-datalake/
```

---

# Exec Pipeline

Execute your pipeline after uploading the data.

---

# pgAdmin

### Linux/macOS

#### Connect to PostgreSQL
```sh
psql -U postgres -h localhost -p 5434 -W
```

#### Switch to Database
```sql
\c music_dw
```

#### Show Table Details
```sql
\d submissions
```

#### Show Input Table
```sql
SELECT * FROM submissions;
```

#### Insert Fake Data for Manual Testing
```sql
INSERT INTO submissions (submission_date, artist_name, track_title, genre, submission_status, email)
VALUES ('2025-04-11', 'Artiste z', 'Chanson 98', 'pop', 'submit', 'artistez@example.com');
```

#### Exit PostgreSQL
```sh
\q
```

---

### Windows

#### Connect to PostgreSQL
```sh
psql -U postgres -h localhost -p 5434 -W
```

#### Switch to Database
```sql
\c music_dw
```

#### Show Table Details
```sql
\d submissions
```

#### Show Input Table
```sql
SELECT * FROM submissions;
```

#### Insert Fake Data for Manual Testing
```sql
INSERT INTO submissions (submission_date, artist_name, track_title, genre, submission_status, email)
VALUES ('2025-04-11', 'Artiste z', 'Chanson 98', 'pop', 'submit', 'artistez@example.com');
```

#### Exit PostgreSQL
```sh
\q
```
