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
def trade_execute(data: str) -> str:
    response: dict = json.loads(data)
    indicator_a: str = response['data']['indikator_a_valid']
    indicator_b: str = response['data']['indikator_b_valid']
    false_breakout: list = response['data']['false_breakouts']
    dataset_1: set = set(int(number) for number in indicator_a.strip().split(', '))
    dataset_2: set = set(int(number) for number in indicator_b.strip().split(', '))
    dataset_3: set = set(int(number) for number in false_breakout)
    first_data_process: set = dataset_1.intersection(dataset_2)
    end_data_process: set = first_data_process.difference(dataset_3)
    new_data: list = sorted(end_data_process)
    return f"Trade ID yang siap dieksekusi: {new_data}"

print(trade_execute(raw_trade_log))


# --- EKSEKUSI ---
# final_trades = validate_trades(raw_trade_log)
# print(f"Trade ID yang siap dieksekusi: {final_trades}")

# Ekspektasi Output Terminal: 
# Membaca log transaksi...
# (Jeda 1 detik)
# Validasi selesai!
# Trade ID yang siap dieksekusi: [520, 525]