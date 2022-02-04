# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, json

# Flask modules
from flask   import render_template, request, jsonify
from jinja2  import TemplateNotFound

# App modules
from app      import app
from app.util import get_products, Product, load_product, load_product_by_slug

import stripe

# Stripe Credentials
stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
    "endpoint_secret": os.environ["STRIPE_ENDPOINT_SECRET"]
}

stripe.api_key = stripe_keys["secret_key"]

@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@app.route("/success")
def success():
    return render_template("payment-success.html")

@app.route("/cancelled")
def cancelled():
    return render_template("payment-cancelled.html")

@app.route("/create-checkout-session/<path>/")
def create_checkout_session(path):

    product = load_product_by_slug( path )

    domain_url = "http://localhost:5000/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - lets capture the payment later
        # [customer_email] - lets you prefill the email input in the form
        # For full details see https:#stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": product.name,
                    "quantity": 1,
                    "currency": 'usd',
                    "amount": product.price * 100,
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

# Product Index
@app.route('/products/', defaults={'path': 'index.html'})
def products_index(path):

    # Collect Products
    products = []
    featured_product = None
    
    # Scan all JSONs in `templates/products`
    for aJsonPath in get_products():  
        
        if 'featured.json' in aJsonPath:
            continue

        # Load the product info from JSON
        product = load_product( aJsonPath )
        
        # Is Valid? Save the object
        if product:     
            products.append( product )

    # Render Products Page
    return render_template( 'products/index.html', products=products, featured_product=load_product_by_slug('featured') )

# List Product
@app.route('/products/<path>/')
def product_info(path):

    product = load_product_by_slug( path )

    return render_template( 'products/template.html', product=product )


# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( path, segment=segment )
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
