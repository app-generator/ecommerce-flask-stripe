# Flask Stripe Sample

Open-source mini `eCommerce` project that loads the products from `JSON` files saved in the [templates](https://github.com/app-generator/sample-flask-stripe/tree/master/app/templates/products) directory (no database required) and uses a decent UI for page styling - Powered by **Flask**.

<br />

> Features:

- Payments via `Stripe`
- Automatic products discovery from `templates\products` directory 
- UI Kit: **Soft UI Kit** (Free Version) by **Creative-Tim**
- `Deployment`: **Docker**

<br />

> Links:

- [Video Presentation](https://www.youtube.com/watch?v=JDtigUqW_MM) - published on yTube
- 👉 Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup). 

<br />

https://user-images.githubusercontent.com/51070104/193888196-bfb20cd1-7248-4a42-ba97-6d67f14c5e40.mp4

<br />

## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ # Get the code
$ git clone https://github.com/app-generator/sample-flask-stripe.git
$ cd sample-flask-stripe
```

<br />

> **Step 2** - Add STRIPE secrets in `Dockerfile`

```Dokerfile
# Stripe Secrets 
ENV STRIPE_SECRET_KEY      <YOUR_STRIPE_SECRET_KEY>
ENV STRIPE_PUBLISHABLE_KEY <YOUR_STRIPE_PUBLISHABLE_KEY>

```

<br />

> **Step 3** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ Quick Start

- Rename `env.sample` to `.env`
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
$ cd sample-flask-stripe
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

> Sample product page generated for [Air ZOOM Pegasus](https://github.com/app-generator/sample-flask-stripe/blob/master/app/templates/products/product-air-zoom-pegasus.json), assets loaded from [here](https://github.com/app-generator/sample-flask-stripe/tree/master/app/static/products/product-air-zoom-pegasus)

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
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |-- base.html            # Used by common pages like index, UI
   |    |    |    |-- base-fullscreen.html # Used by auth pages (login, register)
   |    |    |
   |    |    |-- products/                        # Define your products here
   |    |    |    |-- nike-goalkeeper-match.json  # Sample product
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## ✨ Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
[Soft UI](https://appseed.us/ui-kit/soft-ui-design-system) Jinja - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
