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
```
$ npm install
```

4. Migrate database
```
(venv)$ python manage.py migrate
```

5. Preset
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
