# 0x02. i18n

![91e1c50322b2428428f9](https://github.com/elyse502/alx-backend/assets/125453474/4274bad0-5d45-4ff0-8e8d-726442c6ea81)

# Resources🏗️
### Read or watch:
* [Flask-Babel](https://flask-babel.tkte.ch/)
* [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
* [pytz](https://sourceforge.net/directory/software-development/linux/)

# Learning Objectives 📖
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:
* Learn how to parametrize Flask templates to display different languages
* Learn how to infer the correct locale based on URL parameters, user settings or request headers
* Learn how to localize timestamps

# Requirements 🏛️
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* All your `*.py` files should be executable
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions and methods should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

# Tasks 📃
## 0. Basic Flask app: [0-app.py](0-app.py), [templates/0-index.html](templates/0-index.html)
First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

## 1. Basic Babel setup: [1-app.py](1-app.py), [templates/1-index.html](templates/1-index.html)
Install the Babel Flask extension:
```groovy
$ pip3 install flask_babel==2.0.0
```
Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.


## 2. Get locale from request: [2-app.py](2-app.py), [templates/2-index.html](templates/2-index.html)
Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

## 3. Parametrize templates: [3-app.py](3-app.py), [babel.cfg](babel.cfg), [templates/3-index.html](templates/3-index.html), [translations/en/LC_MESSAGES/messages.po](translations/en/LC_MESSAGES/messages.po), [translations/fr/LC_MESSAGES/messages.po](translations/fr/LC_MESSAGES/messages.po), [translations/en/LC_MESSAGES/messages.mo](translations/en/LC_MESSAGES/messages.mo), [translations/fr/LC_MESSAGES/messages.mo](translations/fr/LC_MESSAGES/messages.mo)
Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing
```groovy
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Then initialize your translations with
```groovy
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with
```groovy
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

| **msgid**	| **English**	| **French** |
| ----- | ------- | ------ |
| `home_title` |	`"Welcome to Holberton"` |	`"Bienvenue chez Holberton"` |
| `home_header`	| `"Hello world!"`	| `"Bonjour monde!"` |

Then compile your dictionaries with
```groovy
$ pybabel compile -d translations
```
Reload the home page of your app and make sure that the correct messages show up.

## 4. Force locale with URL parameter: [4-app.py](4-app.py), [templates/4-index.html](templates/4-index.html)
In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

Visiting `http://127.0.0.1:5000/?locale=fr` **should display this level 1 heading:**

<img width="254" alt="f958f4a1529b535027ce" src="https://github.com/elyse502/alx-backend/assets/125453474/3940de33-ce26-4575-9c48-1726b47c64fa">

## 5. Mock logging in: [5-app.py](5-app.py), [templates/5-index.html](templates/5-index.html)
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.
```groovy
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

| **msgid** |	**English** |	**French** |
| ----- | ------- | ------ |
| `logged_in_as` |	`"You are logged in as %(username)s."` |	`"Vous êtes connecté en tant que %(username)s."` |
| `not_logged_in` |	`"You are not logged in."` |	`"Vous n'êtes pas connecté."` |

Visiting `http://127.0.0.1:5000/` **in your browser should display this:**

<img width="213" alt="2c5b2c8190f88c6b4668" src="https://github.com/elyse502/alx-backend/assets/125453474/6df1964e-0124-4071-b720-75f3505b0780">

Visiting `http://127.0.0.1:5000/?login_as=2` **in your browser should display this:**

<img width="259" alt="277f24308c856a09908c" src="https://github.com/elyse502/alx-backend/assets/125453474/90f601c3-2113-4992-be40-b6d21d4846f7">






















