# [Soft UI](https://appseed.us/ui-kit/soft-ui-design-system) Jinja

Open-source **Jinja Template** provided by AppSeed on top of **[Soft UI](https://appseed.us/ui-kit/soft-ui-design-system)** Kit, a modern Bootstrap 5 design from Creative-Tim. The project might help beginners to code `simple presentation websites` on top of the existing codebase OR migrate the `production-ready` UI to a legacy Python-based project compatible with **Jinja Template Engine**: *Flask*, *Django*, *Bottle* of *FastAPI*. 

<br />

> Features:

- UI Kit: **Soft UI Kit** (Free Version) by **Creative-Tim**
- Render Engine: Flask / Jinja2
- Deployment scripts: Docker, Gunicorn/Nginx, HEROKU
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

> Links:

- [Soft UI Kit Jinja](https://jinja-soft-ui-free.appseed-srv1.com) - LIVE Demo
- More products built with [Soft UI Design](https://appseed.us/ui-kit/soft-ui-design-system) - provided by AppSeed

<br />

## [Soft UI](https://appseed.us/ui-kit/soft-ui-design-system)

Most complex and innovative Dashboard Made by Creative Tim: made of hundred of elements, designed blocks and fully coded pages, Soft UI Dashboard is ready to help you create stunning websites and webapps. 

Premium **Bootstrap 5 Design System** built by Creative-Tim - Soft UI Design System is built with over 300 frontend individual elements, like buttons, inputs, navbars, navtabs, cards or alerts, giving you the freedom of choosing and combining. All components can take variations in colour, that you can easily modify using SASS files and classes.

<br />

![Jinja Template - Starter provided by AppSeed.](https://raw.githubusercontent.com/app-generator/jinja-soft-ui-free/master/media/jinja-soft-ui-free-screen-contact.png)

<br />

## Build from sources

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/jinja-soft-ui-free.git
$ cd jinja-soft-ui-free
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the Jinja Template
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the UI in browser: http://127.0.0.1:5000/
```

<br />

## Code-base structure

The project has a simple structure, represented as bellow:

```bash
< PROJECT ROOT >
   |
   |-- app/__init__.py
   |-- app/
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- includes/                 # Page chunks, components
   |    |    |    |
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |
   |    |    |    |-- base.html            # Used by common pages like index, UI
   |    |    |    |-- base-fullscreen.html # Used by auth pages (login, register)
   |    |    |
   |    |  index.html                      # The default page
   |    |  login.html                      # Auth Login Page
   |    |  register.html                   # Auth Registration Page
   |    |  page-404.html                   # Error 404 page (page not found)
   |    |  page-500.html                   # Error 500 page (server error)
   |    |    *.html                        # All other pages provided by the UI Kit
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## Deployment

The project comes with a basic configuration for [Docker](https://www.docker.com/), [HEROKU](https://www.heroku.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution
---

The steps to start the template using Docker:

> Get the code

```bash
$ git clone https://github.com/app-generator/jinja-soft-ui-free.git
$ cd jinja-soft-ui-free
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

### [Heroku](https://www.heroku.com/)
---

Steps to deploy on **Heroku**

- [Create a FREE account](https://signup.heroku.com/) on Heroku platform
- [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) that match your OS: Mac, Unix or Windows
- Open a terminal window and authenticate via `heroku login` command
- Clone the sources and push the project for LIVE deployment

```bash
$ # Clone the source code:
$ git clone https://github.com/app-generator/jinja-soft-ui-free.git
$ cd jinja-soft-ui-free
$
$ # Check Heroku CLI is installed
$ heroku -v
heroku/7.25.0 win32-x64 node-v12.13.0 # <-- All good
$
$ # Check Heroku CLI is installed
$ heroku login
$ # this commaond will open a browser window - click the login button (in browser)
$
$ # Create the Heroku project
$ heroku create
$
$ # Trigger the LIVE deploy
$ git push heroku master
$
$ # Open the LIVE app in browser
$ heroku open
```

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## [Soft UI Design System](https://appseed.us/ui-kit/soft-ui-design-system) - UI Kit

Most complex and innovative Design System Made by Creative Tim. Soft UI Design System is built with over 70 frontend individual elements, like buttons, inputs, navbars, navtabs, cards or alerts, giving you the freedom of choosing and combining. All components can take variations in colour, that you can easily modify using SASS files and classes.

You will save a lot of time going from prototyping to full-functional code, because all elements are implemented. This Free Bootstrap 5 UK Kit is coming with prebuilt design blocks, so the development process is seamless, switching from our pages to the real website is very easy to be done.

<br />

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website

<br />

---
[Soft UI](https://appseed.us/ui-kit/soft-ui-design-system) Jinja - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
