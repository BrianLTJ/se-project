# se-project
Software Engineering project

[![Build Status](https://travis-ci.com/BrianLTJ/se-project.svg?token=WsEWiDVxieXsRXPgytzk&branch=master)](https://travis-ci.com/BrianLTJ/se-project)

Currently kept in private.

## Set up

1. Create Python virtual env (Recommended)
 ```
 $ python3 -m venv /path/to/venv
 ```

2. Activate Venv
```
$ source /path/to/venv/bin/activate
```
Or in Windows
```
> venv\Script\activate.bat
```

3. Install packages
```
(venv) $ pip install -r requirements.txt
```


4. Migrate database
```
(venv)$ python manage.py migrate
```

5. Preset permissions and add Superuser for initial configurations
```
(venv) $ python preset.py
       0
       Create superuser
       Set permissions
```

6. Run server
```
(venv)$ python manage.py runserver
```

7. Open Browser and visit `http://localhost:8000` or `http://localhost:8000`

## For Developers
1. Install node packages
```
$ npm install
```

2. Make sure you can run gulp

3. Substitute product js lib with development lib
```
$ gulp dev
```