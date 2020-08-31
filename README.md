# EMERGENCY PHONE NUMBERS
#### Basic Static Flask Website - Made with ❤️ in Flask By Alvison Hunter Arnuero - August 31st, 2020.

Welcome to the __Emergency Phone Numbers__, my first flask static website. This readme file will give you an overview of the characteristics I put together when building this website. *This project is still undergoing construction but I hope I have more time in the upcoming weekend to advance with it and put some missing features that I have planned to add soon.*

## Basic Features
- Basic Routing
- 404 error handling
- development env startup
- User login/logout template
- Modern user interface
- Bootstrap 4 CSS framework
- Limited custom css/js
- Easily customizable

Upcoming feature: We will add the email functionality based in Flask Email, a great

***
## Setup

Make sure to have Python 3.6 or newer, and pip installed.

#### Get virtualenv
```bash
$ pip install virtualenv
```
#### Create a virtual environment. You can use any name you want, I usually use "venv" as the below command:
```bash
$ python3 -m venv venv
```

#### Proceed to activate this environment with the below command.
```bash
$ source bin/activate
```

Now you have activated your virtual environment and your teminal should display its name as so:
```bash
$(venv)
```

#### Now, Clone the repository into your local environment folder
```bash
$ git clone https://github.com/AlvisonHunterArnuero/emergency-numbers
$ cd emergency-numbers
```

#### To run this application yourself, please install its requirements first:
```bash
$ pip install -r sample_app/requirements.txt
```

#### Run the application with the below command.
```bash
$ export FLASK_APP=sample_app
$ flask run
```

#### Optionally you can set FLASK_ENV=development like this:
```bash
$ FLASK_APP=app.py FLASK_ENV=development flask run
```

You’ll see output similar to this:

```bash
$ FLASK_APP=app.py FLASK_ENV=development flask run
 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 169-197-047
```

Afterwards, point your browser to http://127.0.0.1:5000/ or the localhost:5000, then check out the source code with your favorite editor. I use Visual Studio Code and Sublime sometimes. Any feedback in regards this code will certainly come handy, thanks for the support, folks!

<p align="center">
🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
</p>
