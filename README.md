# API Test Automation Framework with Python

This TAF is written on `Python`.

## 🚀 Description:

Implemented basic CRUD (`POST`, `GET`, `PUT`, `DELETE`) functionality and defined other.

## 🚀 Prerequisites:

`requests` `pytest` `assertpy` `python-dotenv`

## 🚀 Project Structure:

```
msp360.com/
├─ client/
│  ├─ base_client.py
│  ├─ user_client.py
│─ data/
|  ├─ schema_user_created.json
│  ├─ schema_user_deleted.json
├─ tests/
│  │  ├─ test_user_crud.py
│  │  ├─ test_user_functional_positive.py
│  │  |─ test_user_functional_negative.py
├─ utils/
│  ├─ file_reader.py
├─ .gitignore
├─ config.py
├─ README.md
├─ tasks.txt
```

## 🚀 Test Execution:

- [Fork](https://github.com/...) and Clone the repository https://github.com/...
- Open [Pycharm](https://www.jetbrains.com/pycharm/) (or any IDE) > File > Open > Open the project where the repository is located.
- On the `Pycharm` terminal, navigate to the `tests` directory via `cd tests`
- On the `Pycharm` terminal, run the command: `python -m pytest -v`

## 🚀 Installation Steps:

- For Mac: Install `pipenv` via `homebrew`

```commandline
brew install pipenv
```

- For Windows: Install `pipenv` via `pip`

```commandline
pip install pipenv
```

- Create a home directory

```commandline
mkdir ~/.virtualenvs
```

- Add below in `~/.zshrc` or `~/.bash_profile` (if on Mac/Linux) or your Windows system variables

```commandline
export WORKON_HOME=~/virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

- Source the above changes

```commandline
source ~/.zshrc
```

- Create a new project using Python 3.9.12

```commandline
pipenv --python 3.9.12
```

- Activate virtualenv

```commandline
pipenv shell
```

- Install all dependencies in your virtualenv

```commandline
pipenv install
```
