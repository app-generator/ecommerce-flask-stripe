# [Flask & Stripe](https://blog.appseed.us/flask-stripe-open-source-mini-ecommerce/) `Mini eCommerce`

**[Open-source eCommerce Starter](https://github.com/app-generator/rocket-ecommerce)** that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **Flask & Stripe**.

<br />

## Features

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                          | [Rocket eCommerce](https://appseed.us/product/rocket-ecommerce/django/) | [Custom Development](https://appseed.us/custom-development/) |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ Stack: **Flask**, `Bootstrap`      | ✅ Stack: **Django**, `TailwindCSS`              | **Everything in PRO**, plus:         |
| ✓ Payments: **Stripe**                | ✅ Payments: **Stripe**                          | ✅ **1mo Custom Development**       | 
| ✓ Minimal Bootstrap Design            | ✅ **Stripe Products Import**                    | ✅ **Team**: PM, Developer, Tester  |
| ✓ No Database                         | ✅ **Local Products Customization**              | ✅ Weekly Sprints                   |
| -                                     | ✅ **Categories**, TAGS                          | ✅ Technical SPECS                  |
| -                                     | ✅ Multi-product **Checkout**                    | ✅ Documentation                    |
| -                                     | ✅ **Discounts Page**                            | ✅ **30 days Delivery Warranty**    |
| -                                     | ✅ **Analytics**                                 | -                                    |
| -                                     | ✅ **Transactions Tracking**                     |  -                                   |
| -                                     | ✅ **Zero Configuration**                        |  -                                   |
| -                                     | ✅ **FIGMA** Project                             |  -                                   |
| -                                     | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/) |  -                |
| ------------------------------------  | ------------------------------------              | ------------------------------------|
| -                                     | 🚀 [LIVE Demo](https://rocket-ecommerce.onrender.com/) | 🛒 `Order`: **[$3,999](https://appseed.gumroad.com/l/rocket-package)** (GUMROAD) |  

<br />

![Flask & Stripe Mini eCommerce - Open-Source Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/196479738-be20d203-df44-47ce-a124-d3ed426ef622.jpg)

<br />

## Start in `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/ecommerce-flask-stripe.git
$ cd ecommerce-flask-stripe
```

<br />

> 👉 **Step 2** - Add STRIPE secrets in `Dockerfile`

```Dokerfile
# Stripe Secrets 
ENV STRIPE_SECRET_KEY      <YOUR_STRIPE_SECRET_KEY>
ENV STRIPE_PUBLISHABLE_KEY <YOUR_STRIPE_PUBLISHABLE_KEY>
```

<br />

> 👉 **Step 3** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Manual Build

> 👉 Rename `env.sample` to `.env`

- Edit `STRIPE_SECRET_KEY` - provided by Stripe Platform
- Edit `STRIPE_PUBLISHABLE_KEY` - provided by Stripe Platform

<br />

> 👉 Install dependencies

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Start the App

```bash
$ flask run
```

<br />

> 👉 Access the products and initiate a payment

**IMPORTANT**: Make sure your Stripe account is running in `TEST Mode` and Use Test CC provided by Stripe:

- **CC Number**: `4242 4242 4242 4242`
- Any data for the rest of the fields  

<br />

## Create a new Product

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

> Sample product page generated for [Air ZOOM Pegasus](./app/templates/products/product-air-zoom-pegasus.json), assets loaded from [here](./app/static/products/product-air-zoom-pegasus)

<br />

![Flask Stripe Sample - Air ZOOM Pegasus (sample Product](https://user-images.githubusercontent.com/51070104/152586940-2f3b31fb-f067-487a-98ca-26d9e1936514.png)

<br />

## Codebase Structure

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

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
[Flask Stripe Sample](https://blog.appseed.us/flask-stripe-open-source-mini-ecommerce/) - Free sample provided by [AppSeed](https://appseed.us).
