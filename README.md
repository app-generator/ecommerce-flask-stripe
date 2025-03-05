# Flask & Stripe `Mini eCommerce`

**Open-source eCommerce Starter** that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **Flask & Stripe**.

- [Flask mini eCommerce](https://github.com/app-generator/ecommerce-flask-stripe) sources (this repo)
- [Rocket eCommerce](https://app-generator.dev/product/rocket-ecommerce/django/) - **PRO Version**
  - ✅ Stripe Integration
  - ✅ Checkout, Discounts Page
  - ✅ Tags, Categories
  - ✅ Analytics
  - ✅ Generated Sitemap 
  
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

## Need More? Go PRO with [Rocket eCommerce](https://app-generator.dev/product/rocket-ecommerce/django/)

Production-ready eCommerce CMS integrated with Stripe, Analytics, Discounts Page, Docker and CI/CD support - Actively supported by [App-Generator](https://app-generator.dev/).

| Status | Item | info | 
| --- | --- | --- |
| ✅ | Stack | Django, Tailwind, React |
| ✅ | Payments | Stripe |
| ✅ | Categories | YES |
| ✅ | Tags | YES |
| ✅ | Checkout | YES |
| ✅ | Discounts Page | YES |
| ✅ | Products Import | Stripe |
| ✅ | Products Local Customization | YES |
| ✅ | Analitycs | Weekly, Monthly, Year `Sales` |
| ✅ | Transactions Tracking | YES |
| ✅ | Docker | YES |
| ✅ | CI/CD | Render |

![Rocket eCommerce - Production-ready eCommerce CMS integrated with Stripe, Analytics, Discounts Page, Docker and CI/CD support.](https://github.com/user-attachments/assets/5db5841f-6802-4dfa-8ce7-46cf14435c5a)

<br />

---
Flask & Stripe `Mini eCommerce` - Open-source eCommerce Starter provided by [App-Generator](https://app-generator.dev/).
