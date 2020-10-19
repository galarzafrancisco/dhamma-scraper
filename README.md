# dhamma-scraper

Script to find out when the applications open.
Configured for the test date (27 Jan - 07 Feb). Dates can be changed on line 9 in main.py.
Entries will be printed and written to the file log.txt.


# Instructions

### 1. Clone this repo
```
git clone https://github.com/galarzafrancisco/dhamma-scraper.git
```

### 2. Install requirements
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
deactivate
```

### 3. Run the script
```
source env/bin/activate
python main.py
deactivate
```


# Pro tip - run in a Docker container

### 1. Build
```
./docker_build.sh
```

### 2. Run
```
./docker_run.sh
```

#
Made with love ❤️