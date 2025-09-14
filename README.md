# 🧹 Windows Cleaner Python Script

## 📌 Deskripsi
Script Python untuk membersihkan folder temporary & log Windows.  
Fitur utama:
- Membersihkan folder target (Temp, Prefetch, SoftwareDistribution, dll).  
- Progress bar **per folder** + **global**.  
- Log otomatis harian (`C:\CleanerLogs`).  
- Ringkasan total (berapa folder sukses/gagal & total MB dibersihkan).  

---

## ⚙️ Cara Pakai

### 1. Siapkan Python
Pastikan Python 3 sudah terinstal. Cek dengan:
```cmd
python --version
```

### 2. Simpan script
Simpan file `cleaner.py` di folder favoritmu, misalnya:  
```
C:\Scripts\wincleaner.py
```

### 3. Jalankan manual
Buka **Command Prompt**, lalu ketik:
```cmd
python C:\Scripts\wincleaner.py
```

### 4. Hasil
- Progress bar akan muncul di CMD.  
- Log detail tersimpan di:
  ```
  C:\CleanerLogs\cleaner_YYYY-MM-DD.log
  ```
- Ringkasan hasil ada di akhir log.  

---

## 🚀 Jalankan dengan Double Click (opsional)

Biar lebih praktis, bikin file `run_cleaner.bat` dengan isi:

```bat
@echo off
python "C:\Scripts\wincleaner.py"
pause
```

Simpan `run_cleaner.bat` di desktop → tinggal **double click** untuk menjalankan.

---

## ⚠️ Catatan
- Jalankan **sebagai Administrator** agar semua folder bisa dibersihkan.  
- Folder **Recycle Bin** tidak dibersihkan otomatis (manual saja).  
- Tidak ada modifikasi Registry (lebih aman).  

---

## 🛠️ Troubleshooting

### ❌ `python` tidak dikenali
- Kemungkinan Python belum ditambahkan ke **PATH**.  
- Solusi: jalankan dengan perintah lengkap, misalnya:
  ```cmd
  C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python310\python.exe C:\Scripts\wincleaner.py
  ```
- Atau tambahkan Python ke PATH saat instalasi.  

### ❌ Akses ditolak (`PermissionError`)
- Beberapa folder butuh hak akses admin.  
- Solusi: buka **Command Prompt sebagai Administrator**, lalu jalankan script.  

### ❌ Script jalan tapi tidak ada log
- Pastikan folder `C:\CleanerLogs` bisa dibuat (cek izin akses).  
- Atau ubah lokasi log di script (variabel `LOG_DIR`).  

### ❌ File `.bat` langsung tertutup
- Tambahkan `pause` di akhir file `.bat` agar jendela CMD tetap terbuka.  
