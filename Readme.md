## Naulkri.com Scraper based on search terms and location 
Python >=3.6

Usage:
``` 
    $ python naukri.py search-terms="space separated search terms" location=City depth=12
```
Parameters:
1. search-terms (mandatory) : Space separated search terms
2. location (mandatory)     : One word location for search
3. depth (optional)         : Number of pages to search for(Each page contain 19 listings)


### Python virtualenv setup (recommended)
```
    $ mkdir env && cd env
    $ pip install venv 
    $ python -m venv .
```
On Linux/Unix 
```
    $source env/bin/activate
```
On Windows
```
    > env\bin\activate
```

### Install packages from requirements.txt
```
    (env)$ pip install -r requirements.txt
```

