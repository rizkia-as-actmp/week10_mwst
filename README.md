# 🚀 Backend Framework

#### 📛 Nama : Rizkia Adhy Syahputra  
#### 🎓 NIM : 5220411051  

## 📋 Daftar Isi
- [Backend Framework](#backend-framework)
  - [A. ExpressJs](#a-expressjs)
    - [1. 📂 Buat direktori untuk menyimpan kode untuk expressjs](#1-buat-direktori-untuk-menyimpan-kode-untuk-expressjs)
    - [2. 🛠️ Init untuk node package manager](#2-init-untuk-node-package-manager)
    - [3. 📦 Install express](#3-install-express)
    - [4. ✍️ Buat file javascript untuk menampung kode express](#4-buat-file-javascript-untuk-menampung-kode-express)
    - [5. ✨ Kode Hello World](#5-kode-hello-world)
    - [6. ▶️ Running](#6-running)
    - [7. 📸 Hasil Running](#7-hasil-running)
  - [B. Flask](#b-flask)
    - [1. 📂 Buat direktori untuk menyimpan kode untuk flask](#1-buat-direktori-untuk-menyimpan-kode-untuk-flask)
    - [2. 🔄 Masuk ke direktori flask](#2-masuk-ke-direktori-flask)
    - [3. 🐍 Buat python environment](#3-buat-python-environment)
    - [4. 🔧 Gunakan python environment](#4-gunakan-python-environment)
    - [5. 📦 Install flask](#5-install-flask)
    - [6. ✍️ Buat file untuk kode flask](#6-buat-file-untuk-kode-flask)
    - [7. ✨ Kode Hello World](#7-kode-hello-world-1)
    - [8. ▶️ Running](#8-running)
    - [9. 📸 Hasil Running](#9-hasil-running)
- [🎉 Selesai](#selesai)

---

## A. ExpressJs 🟦
##### 1. 📂 Buat direktori untuk menyimpan kode untuk expressjs
```shell
mkdir express
```
##### 2. 🛠️ Init untuk node package manager 
```shell
npm init
```
Setelah menjalankan perintah di atas, Anda akan ditanya beberapa pertanyaan untuk mengisi informasi tentang project Node.js. Untuk percobaan ini, saya klik **enter-enter saja** karena untuk sekarang belum terlalu penting.

##### 3. 📦 Install express 
```shell
npm i express
```
##### 4. ✍️ Buat file JavaScript untuk menampung kode express 
```shell
touch index.js
```
Saya menamakannya `index.js` karena saat saya init project Node.js, saya setuju menggunakan `index.js` sebagai lokasi file utama.

##### 5. ✨ Kode Hello World
```javascript
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!, Perkenalkan saya Rizkia Adhy Syahputra, ini adalah expressJS')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```
Saya menggunakan kode dari dokumentasi resmi ExpressJS:  
[express hello world](https://expressjs.com/en/starter/hello-world.html "express hello world")

##### 6. ▶️ Running 
Gunakan perintah berikut untuk menjalankan aplikasi Express:
```shell
node index.js
```

##### 7. 📸 Hasil Running 
<img src=".md.d/run-express.png" width="600">

---

## B. Flask 🟧
##### 1. 📂 Buat direktori untuk menyimpan kode untuk flask
```shell
mkdir tugas_flask
```
##### 2. 🔄 Masuk ke direktori flask
```shell
cd tugas_flask
```
##### 3. 🐍 Buat python environment
Python environment digunakan untuk melakukan isolasi terhadap package Python dan versinya agar tidak memengaruhi sistem secara global.
```shell
python3 -m venv tugas_10_mwsc_pyvenv
```
##### 4. 🔧 Gunakan python environment
Sumberkan environment ke terminal yang sedang Anda gunakan:
```shell
source tugas_10_mwsc_pyvenv/bin/activate
```
##### 5. 📦 Install flask
Pasang Flask menggunakan `pip`:
```shell
pip install flask
```

##### 6. ✍️ Buat file untuk kode flask
```shell
touch app.py
```
Anda dapat menamai file ini sesuai keinginan, tetapi untuk tutorial ini, saya memilih `app.py`.

##### 7. ✨ Kode Hello World
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!, nama saya Rizkia Adhy Syahputra, hello flask</h1>"
```
Kode ini saya ambil dari dokumentasi resmi Flask:  
[flask hello world](https://flask.palletsprojects.com/en/stable/quickstart/)

##### 8. ▶️ Running 
Gunakan perintah berikut untuk menjalankan aplikasi Flask:
```shell
flask --app app.py run
```

##### 9. 📸 Hasil Running 
<img src=".md.d/run-flask.png" width="600">

---

# 🎉 Selesai
