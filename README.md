# SundaPy 🐍

Basa pamrograman anu ditulis nganggo **Basa Sunda**, tapi mesinna tetep Python.
File `.sun` ditranspile (dirobah) heula jadi kode Python nu sah, terus dijalankeun.

## Conto kode (`examples/conto.sun`)

```
gawe sapa(ngaran):
    lamun ngaran == "":
        balik "Wilujeng sumping!"
    sanes:
        balik "Wilujeng sumping, " + ngaran + "!"

cetak(sapa("Sunda"))
```

## Instalasi (lokal, tacan di-publish ka PyPI)

1. Pastikeun Python >= 3.8 geus kainstal (`python3 --version`).
2. Clone/download repo ieu, terus asup ka foldernya:
   ```bash
   git clone https://github.com/USERNAME/sundapy.git
   cd sundapy
   ```
3. Install dina mode "editable" (nu ngahasilkeun perintah `sunda`):
   ```bash
   pip install -e .
   ```
   > Di Linux/Mac nu ngagunakeun sistem Python, mun aya error "externally-managed-environment", tambahkeun `--break-system-packages`, atawa nganggo virtualenv:
   > ```bash
   > python3 -m venv venv
   > source venv/bin/activate
   > pip install -e .
   > ```

## Ngagunakeun

Jalankeun langsung:
```bash
sunda run examples/conto.sun
```

Robah jadi file `.py` biasa (mun hoyong tempo hasil transpile-na):
```bash
sunda compile examples/conto.sun -o conto.py
```

## Kecap kunci nu geus disadiakeun

Tempo/robah dina `sundapy/keywords.py`. Sabagian conto:

| Sunda      | Python   |
|------------|----------|
| `lamun`    | `if`     |
| `sanes`    | `else`   |
| `salila`   | `while`  |
| `pikeun`   | `for`    |
| `gawe`     | `def`    |
| `balik`    | `return` |
| `leres`    | `True`   |
| `salah`    | `False`  |
| `cetak`    | `print`  |
| `impor`    | `import` |

Tinggal tambihan pasangan kecap-Sunda: kecap-Python di dictionary `KEYWORDS`
mun hoyong nambahan kosakata.

## Cara upload ka GitHub

```bash
cd sundapy
git init
git add .
git commit -m "Rilis mimiti SundaPy"
git branch -M main
git remote add origin https://github.com/USERNAME/sundapy.git
git push -u origin main
```

Ganti `USERNAME` jeung ngaran akun GitHub anjeun. Mun tacan aya repo di GitHub,
jieun heula repo kosong (tanpa README) ngaliwatan tombol "New repository".

## Kumaha ari cara gawe-na (transpiler)

`sundapy/transpiler.py` maca source `.sun` maké modul `tokenize` bawaan
Python — sanes ganti-string biasa (regex). Ku kituna, kecap anu aya di jero
string (`"lamun ieu di jero string"`) atawa komentar teu bakal katukang robah,
ngan kecap kunci nu bener-bener jadi token ngaran (NAME) anu dirobah.
