import json
import time
import functools
from typing import Callable

# Data simulasi dari server (berwujud String JSON)
raw_trade_log = """
{
    "session": "NY_Open",
    "data": {
        "indikator_a_valid": " 501, 505, 510, 520, 525 ",
        "indikator_b_valid": " 520, 505, 515, 525, 530 ",
        "false_breakouts": ["505"]
    }
}
"""

# TUGAS 1: Buat Decorator @trade_logger
# Wajib menampung hasil fungsi utamanya sebelum melakukan return akhir!
# Jangan lupa anotasi tipe argumen dan return-nya.



# TUGAS 2: Fungsi Utama
# Eksekusi Type Annotations yang TEPAT (parsed json adalah dict).
# Gunakan Sets untuk irisan dan selisih, lalu kembalikan hasilnya sebagai list.



# --- EKSEKUSI ---
# final_trades = validate_trades(raw_trade_log)
# print(f"Trade ID yang siap dieksekusi: {final_trades}")

# Ekspektasi Output Terminal: 
# Membaca log transaksi...
# (Jeda 1 detik)
# Validasi selesai!
# Trade ID yang siap dieksekusi: [520, 525]