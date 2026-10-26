<p align="center">
  <br>
  <img src="https://github.com/banaxou/dark-sherlock/blob/main/img%2Fdarksherlock.png" width="550" alt="Dark Sherlock">
  <br><br>
  <b>Username intelligence across the dark web</b>
  <br>
  <span>Search usernames across 40+ dark web forums</span>
  <br><br>
</p>

[Dark Sherlock 1.1](https://pypi.org/project/dark-sherlock/) [ by ovax &](https://instagram.com/banaxou) [cti](https://x.com/cti__Updates)

<p align="center">
  <a href="https://threatactorusernames.com/"><img src="https://img.shields.io/badge/Website-red?style=for-the-badge" alt="Website"></a>
  &nbsp;
  <a href="https://pypi.org/project/dark-sherlock/"><img src="https://img.shields.io/badge/PyPI-red?style=for-the-badge" alt="PyPI"></a>
  &nbsp;
  <a href="https://threatactorusernames.com/forums-list"><img src="https://img.shields.io/badge/Forums-red?style=for-the-badge" alt="Forums list"></a>
</p>

![tuto](https://media.licdn.com/dms/image/v2/D4E22AQESS3e7ISbakA/feedshare-image-high-res/B4EaEf8W3ZGkAU-/0/1791537278662?e=2147483647&v=beta&t=oliUYRCeK0JSHDkt098qU07xn4WBenwbWLCpHCQUHd4)


---

## About

**Dark Sherlock** is a CSINT tool built to search for usernames across **40+ dark web forums**.

It is designed to make username research faster by checking multiple forums from a single command.

---

## Installation

Install Dark Sherlock with pip | git:

```bash
pip install dsherlock
or
git clone https://github.com/banaxou/dark-sherlock/
cd dark-sherlock/scripts
pip install -r requirements.txt
python3 dark_sl.py
```

> **Note:** Make sure you are installing the official Dark Sherlock package.  
> Be careful with packages using similar names | And use a VPN! A Tor connection will be added soon



## Star History

<a href="https://www.star-history.com/?repos=banaxou%2Fdark-sherlock&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=banaxou/dark-sherlock&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=banaxou/dark-sherlock&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=banaxou/dark-sherlock&type=date&legend=top-left" />
 </picture>
</a>

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

Dark Sherlock - Username CSINT Tool : Find Usernames Across Dark web ;) v1.1

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
