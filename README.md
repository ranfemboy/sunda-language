# SundaPy 🐍

A tiny programming language that lets you write code using **Sundanese words**
(a language from West Java, Indonesia) instead of English. Under the hood it's
still Python — SundaPy just translates the words for you before running it.

You don't need to know Python to try this. Just follow the steps below.

## What code looks like (`examples/conto.sun`)

```
gawe sapa(ngaran):
    lamun ngaran == "":
        balik "Wilujeng sumping!"
    sanes:
        balik "Wilujeng sumping, " + ngaran + "!"

cetak(sapa("Sunda"))
```

Running it prints: `Wilujeng sumping, Sunda!`

## How to install it

**Step 1 — Make sure Python is installed**

Open your terminal and type:
```bash
python3 --version
```
If you see a version number (3.8 or higher), you're good. If not, download
Python from [python.org](https://www.python.org/downloads/) first.

**Step 2 — Get this project onto your computer**

If you downloaded the folder as a zip, just unzip it and open a terminal
inside that folder. If you're getting it from GitHub instead:
```bash
git clone https://github.com/ranfemboy/sunda-language.git
cd sunda-language
```

**Step 3 — Install it**
```bash
pip install -e .
```
This creates a new command called `sunda` that you can use anywhere.

> If you see an error mentioning "externally-managed-environment", just run:
> ```bash
> pip install -e . --break-system-packages
> ```

## How to use it

Run the example program:
```bash
sunda run examples/conto.sun
```

Want to write your own program? Create a new file ending in `.sun`
(for example `mycode.sun`), write Sundanese code inside it using the word
list below, then run:
```bash
sunda run mycode.sun
```

## Word list (Sundanese → what it means)

| Sundanese  | Meaning (like English) |
|------------|-------------------------|
| `lamun`    | if                      |
| `sanes`    | else                    |
| `salila`   | while                   |
| `pikeun`   | for                     |
| `gawe`     | def (make a function)   |
| `balik`    | return                  |
| `leres`    | True                    |
| `salah`    | False                   |
| `cetak`    | print                   |
| `impor`    | import                  |

Want to add more Sundanese words? Open the file `sundapy/keywords.py` and
add your own word on the left, matching it to the English/Python word on
the right.
