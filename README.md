<p align="center">
  <br>
  <img src="https://github.com/banaxou/dark-sherlock/blob/main/img%2Fdarksherlock.png" width="550" alt="Dark Sherlock">
  <br><br>
  <b>Username intelligence across the dark web</b>
  <br>
  <span>Search usernames across 40+ dark web forums</span>
  <br><br>
</p>

<p align="center">
  <a href="https://threatactorusernames.com/"><img src="https://img.shields.io/badge/Website-red?style=for-the-badge" alt="Website"></a>
  &nbsp;
  <a href="https://pypi.org/project/dark-sherlock/"><img src="https://img.shields.io/badge/PyPI-red?style=for-the-badge" alt="PyPI"></a>
  &nbsp;
  <a href="https://threatactorusernames.com/forums-list"><img src="https://img.shields.io/badge/Forums-red?style=for-the-badge" alt="Forums list"></a>
</p>

---

## About

**Dark Sherlock** is a CSINT tool built to search for usernames across **40+ dark web forums**.

It is designed to make username research faster by checking multiple forums from a single command.

---

## Installation

Install Dark Sherlock with:

```bash
pip install dsherlock
or
git clone https://github.com/banaxou/dark-sherlock/
cd dark-sherlock
python3 dark_sl.py
```

> **Note:** Make sure you are installing the official Dark Sherlock package.  
> Be careful with packages using similar names.

---

## Usage

### Username

```bash
dsherlock zero
```

Search for a single username.

### Multiple usernames

```bash
dsherlock -u zero sherlock
```

Search for multiple usernames in a single request.

### JSON output

```bash
dsherlock zero --json
```

Save the results to a JSON file.

### TXT output

```bash
dsherlock zero --txt
```

Save the results to a TXT file.

### Help

Display the available options with:

```bash
dark-sl -h
```

or:

```bash
dsherlock -h
```

### Output

```bash
dsherlock -h
usage: dsherlock [username] [-u USERNAME] [--json] [--txt]

Dark Sherlock - Username CSINT Tool : Find Usernames Across Dark web ;) v1.0

positional arguments:
  usernames             Username to check

options:
  -h, --help            show this help message and exit
                        Show this help message and exit
  -u, --user USERS [USERS ...]
                        Username target |
                        Double username target
  --json                Save results in JSON
                        file + display normal
                        output
  --txt                 Save results in TXT
                        file
```

---

## Why are there two packages?

Dark Sherlock provides two packages:

`dark-sl`

and

`dsherlock`

Both commands are identical and provide the same functionality.

The two commands exist to prevent confusion with fake or fraudulent packages impersonating Dark Sherlock.

---

## info

Dark Sherlock searches across **40+ dark web forums**.

• [Website](https://threatactorusernames.com/)  
• [Forum List](https://threatactorusernames.com/forums-list)  
• [FAQ](https://threatactorusernames.com/faq)

---

## Donate crypto

Sol:
```
BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2
```

Dark Sherlock relies on the forum information and research provided by [Threat usernames](https://threatactorusernames.com/).

---

## License

MIT License

Copyright © 2026 ovax
