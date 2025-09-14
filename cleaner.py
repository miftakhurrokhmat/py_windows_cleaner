# cleaner.py
# Script utama untuk membersihkan temporary files di Windows
# (Isi detail script sudah ada dari percakapan sebelumnya)
print("Windows Cleaner Script - placeholder")

import os
import shutil
import getpass
import datetime
import sys

# ===================== CONFIG =====================
LOG_DIR = r"C:\CleanerLogs"
LOG_FILE = os.path.join(LOG_DIR, f"cleaner_{datetime.date.today()}.log")
# ==================================================

TARGET_FOLDERS = [
    r"C:\Windows\Temp",
    fr"C:\Users\{getpass.getuser()}\AppData\Local\Temp",
    r"C:\Windows\Prefetch",
    r"C:\Windows\SoftwareDistribution\Download",
    r"C:\ProgramData\Microsoft\Windows\WER",
    r"C:\Windows\Minidump",
    r"C:\Windows\Logs",
    r"C:\Windows\System32\LogFiles"
]

# Statistik global
total_deleted_size = 0
folders_cleaned = 0
folders_failed = 0

def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def write_log(message):
    ensure_log_dir()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def get_size(path):
    """Hitung ukuran file/folder dalam byte"""
    total = 0
    if os.path.isfile(path):
        try:
            total = os.path.getsize(path)
        except:
            pass
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for name in files:
                try:
                    total += os.path.getsize(os.path.join(root, name))
                except:
                    pass
    return total

def show_progress(current, total, bar_length=30, prefix=""):
    """Tampilkan progress bar sederhana"""
    percent = 0 if total == 0 else current / total
    filled = int(bar_length * percent)
    bar = "#" * filled + "-" * (bar_length - filled)
    sys.stdout.write(f"\r{prefix} [{bar}] {percent*100:.0f}% ({current}/{total})")
    sys.stdout.flush()
    if current == total:
        print()  # baris baru setelah selesai

def clear_folder(path, global_idx, global_total):
    global total_deleted_size, folders_cleaned, folders_failed
    if os.path.exists(path):
        items = os.listdir(path)
        total_items = len(items)
        write_log(f"Membersihkan: {path} (total {total_items} item)")
        for idx, item in enumerate(items, start=1):
            item_path = os.path.join(path, item)
            try:
                size = get_size(item_path)
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                    total_deleted_size += size
                    write_log(f"  ✔ Dihapus: {item_path} ({size/1024/1024:.2f} MB)")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    total_deleted_size += size
                    write_log(f"  ✔ Folder dihapus: {item_path} ({size/1024/1024:.2f} MB)")
            except Exception as e:
                write_log(f"  ✘ Gagal hapus {item_path} -> {e}")

            # Progress bar per folder
            show_progress(idx, total_items, prefix=f"Folder {global_idx}/{global_total}")

        if total_items == 0:
            show_progress(1, 1, prefix=f"Folder {global_idx}/{global_total}")
        folders_cleaned += 1
    else:
        write_log(f"Folder {path} tidak ditemukan.")
        show_progress(1, 1, prefix=f"Folder {global_idx}/{global_total}")
        folders_failed += 1

def main():
    write_log("=== Mulai proses pembersihan ===")
    total_folders = len(TARGET_FOLDERS)
    for i, folder in enumerate(TARGET_FOLDERS, start=1):
        clear_folder(folder, i, total_folders)
        # Global progress bar (folder level)
        show_progress(i, total_folders, prefix="Progress global")

    # Ringkasan akhir
    write_log("=== RINGKASAN ===")
    write_log(f"Total folder ditargetkan : {total_folders}")
    write_log(f"Folder berhasil dibersihkan : {folders_cleaned}")
    write_log(f"Folder gagal / tidak ditemukan : {folders_failed}")
    write_log(f"Total dibersihkan : {total_deleted_size/1024/1024:.2f} MB")
    write_log("=== Pembersihan selesai ===\n")

if __name__ == "__main__":
    main()
