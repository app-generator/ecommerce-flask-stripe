# Flask Stripe Sample

Open-source sample provided by [AppSeed](https://appseed.us). The project is a simple `eCommerce` app that loads the products from `JSON` files saved in the [templates](https://github.com/app-generator/flask-soft-ui-design-stripe/tree/master/app/templates/products) directory (no database required). 

<br />

> Features:

- Payments via `Stripe`
- Automatic products discovery from `templates` directory 
- UI Kit: **Soft UI Kit** (Free Version) by **Creative-Tim**
- `Deployment`: **Docker**, Gunicorn/Nginx, HEROKU
- 👉 Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup). 

<br />

> Links:

- 👉 [Flask Stripe Sample](#) - LIVE Demo (coming soon)
- 👉 More products built with [Soft UI Design](https://appseed.us/ui-kit/soft-ui-design-system) - provided by AppSeed

<br />

![Flask Stripe Sample - Open-Source project crafted by AppSeed (GIF animated presentation).](https://user-images.githubusercontent.com/51070104/152642786-d584d817-691e-4079-8663-3c212ef6328a.gif)

<br />

## ✨ Quick Start

- Rename `.env.sample` to `.env`
  - Edit `STRIPE_SECRET_KEY` - provided by Stripe Platform
  - Edit `STRIPE_PUBLISHABLE_KEY` - provided by Stripe Platform
- Install dependencies
- Start the App
  - `$ flask run` 
- Access the products and initiate a payment
  - **IMPORTANT**: Make sure your Stripe account running in TEST Mode
  - Use Test CC data:
    - CC Number: `4242 4242 4242 4242`
    - Any data for the rest of the fields  

<br />

## ✨ Build from sources

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/sample-flask-stripe.git
$ cd jsample-flask-stripe
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

## ✨ Create a new Product

- Go to `app/templates/products` directory
- Create a new `JSON` file with data:
  - `name`: Used in product page & Cards
  - `price`: Used for payment
  - `currency`: Used for payment
  - `info`: used in cards 
  - `short_description`: used in product page
  - `full_description`: used in product page
- Create Media Files
  - Go to `master/app/static/products` 
  - Create a directory using the same name as for `JSON` file
    - Create `card.jpg`: 500x335px
    - Create `cover.jpg`: 2100x1400px
- Start or refresh the app
  - The new product should be listed in the `products/` page
  - Product page is available at address:
    - `http://localhost:5000/products/<SLUG>/` where the SLUG is the name of the JSON file 
  
<br />

> Sample product page generated for [Air ZOOM Pegasus](https://github.com/app-generator/flask-soft-ui-design-stripe/blob/master/app/templates/products/product-air-zoom-pegasus.json), assets loaded from [here](https://github.com/app-generator/flask-soft-ui-design-stripe/tree/master/app/static/products/product-air-zoom-pegasus)

<br />

![Flask Stripe Sample - Air ZOOM Pegasus (sample Product](https://user-images.githubusercontent.com/51070104/152586940-2f3b31fb-f067-487a-98ca-26d9e1936514.png)

<br />

## ✨ Code-base structure

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

## ✨ Deployment

The project comes with a basic configuration for [Docker](https://www.docker.com/), [HEROKU](https://www.heroku.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Heroku](https://www.heroku.com/)
---

Steps to deploy on **Heroku**

- [Create a FREE account](https://signup.heroku.com/) on Heroku platform
- [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) that match your OS: Mac, Unix or Windows
- Open a terminal window and authenticate via `heroku login` command
- Clone the sources and push the project for LIVE deployment

```bash
$ # Clone the source code:
$ git clone https://github.com/app-generator/sample-flask-stripe.git
$ cd sample-flask-stripe
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

## ✨ Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website

<br />

---
[Soft UI](https://appseed.us/ui-kit/soft-ui-design-system) Jinja - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
