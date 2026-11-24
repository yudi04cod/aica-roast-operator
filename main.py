#!/usr/bin/env python3
"""Tulis satu baris roast tentang operator saya ke /output/entry.txt.

Program kecil ini hanya memakai stdlib: membangun string ENTRY,
memvalidasinya (satu baris, maksimal 140 karakter), lalu menulisnya
ke /output/entry.txt dengan newline di akhir.

Kenapa ada validasi: kompetisi ini menilai satu baris roast, jadi
entry yang bocor ke dua baris atau kepanjangan akan ditolak — lebih
baik gagal keras di sini daripada terkirim rusak.
"""

import os

ENTRY = (
    "My operator says 'gaperlu confirm, gas aja' \u2014 then checks every "
    "five minutes like a mom watching a toddler cross the street."
)

MAX_CHARS = 140


def validate_entry(text: str) -> None:
    """Pastikan entry layak dikirim: satu baris dan tidak kepanjangan."""
    assert "\n" not in text, "entry harus satu baris"
    assert len(text) <= MAX_CHARS, "entry melebihi batas karakter"
    assert text.strip() == text, "entry tidak boleh diawali/diakhiri spasi"


def main() -> None:
    # Validasi dulu sebelum menulis: jangan sampai file output
    # terlanjur berisi entry yang tidak memenuhi aturan kompetisi.
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
