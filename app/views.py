# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, json
import base64
import sqlite3
import sqlite3 as sql

# Flask modules
from flask   import render_template, request, jsonify, redirect, g, url_for
from jinja2  import TemplateNotFound
from flask_login import login_required, logout_user, current_user, login_user
from functools import wraps

from app.models import User
from . import db

# App modules
from app      import app
from app.util import get_products, Product, load_product, load_product_by_slug, load_json_product

import stripe

# Stripe Credentials
stripe_keys = {
    "secret_key"     : app.config['STRIPE_SECRET_KEY'     ] ,
    "publishable_key": app.config['STRIPE_PUBLISHABLE_KEY'] ,
    "endpoint_secret": app.config['STRIPE_SECRET_KEY'     ] ,
} 

stripe.api_key = stripe_keys["secret_key"]

###############################################
# AUTH 

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username=username, password=password)
        login_user(user=user, remember=True)
        return redirect('/')


    return render_template("pages/page-sign-in.html")

@app.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect('/')

@app.cli.command("create-user")
def create_user():
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    user = User(username=username, email=email, password=password)
    db.create_all()
    db.session.add(user)
    db.session.commit()

# AUTH 
###############################################

@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@app.route("/success")
def success():
    return render_template("ecommerce/payment-success.html")

@app.route("/cancelled")
def cancelled():
    return render_template("ecommerce/payment-cancelled.html")

@app.route("/create-checkout-session/<path>/")
def create_checkout_session(path):

    product = load_product_by_slug( path )

    domain_url = app.config['SERVER_ADDRESS']
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
@app.route('/',          defaults={'path': 'products/index.html'})
@app.route('/products/', defaults={'path': 'products/index.html'})
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
    return render_template( 'ecommerce/index.html', 
                            products=products, 
                            featured_product=load_product_by_slug('featured') )

# List Product
@app.route('/products/<path>/')
def product_info(path):

    try:
        product = load_product_by_slug( path )
        return render_template( 'ecommerce/template.html', product=product )
    except:
        return render_template( 'pages/page-404.html')

# App main route + generic routing
@app.route('/<path>')
def index(path):

    try:

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( 'pages/' + path )
    
    except TemplateNotFound:
        return render_template('pages/page-404.html'), 404


@app.route('/load-products/', methods=['GET', 'POST'])
@login_required
def load_product_json():
    json_data = []

    # load stripe product
    if request.method == "POST":
        products = stripe.Product.list(expand = ['data.default_price'])
        productdict = []
        for product in products:
            dict= {}
            dict['id'] = product['id']
            dict['name'] = product['name']
            dict['price'] = product["default_price"]["unit_amount"]/100
            dict['currency'] = product["default_price"]["currency"]
            dict['full_description'] = product["description"]
            dict['info'] = product["description"][0:30]

            for index, image in enumerate(product['images']):
                dict['img_main'] = image

            dict['img_card'] = ''
            dict['img_1'] = ''
            dict['img_2'] = ''
            dict['img_3'] = ''

            productdict.append(dict)
        
        for product in productdict:
            json_product = json.dumps( product, indent=4, separators=(',', ': ') )
            json_data.append(json_product)

    # load local product
    local_products = []
    for aJsonPath in get_products():  
        if 'featured.json' in aJsonPath:
            continue
        local_json = load_json_product(aJsonPath)
        local_products.append(json.dumps( local_json, indent=4, separators=(',', ': ') ))
    return render_template('ecommerce/create-product.html', json_data=json_data, local_products=local_products)


@app.route('/create-product/', methods=['GET', 'POST'])
@login_required
def create_new_product():
    if request.method == 'POST':
        product = request.form.get('product')
        name = json.loads(product)['name']
        slug = name.lower().replace(' ', '-')

        try:
            products = load_product_by_slug( slug )
            if products:
                return redirect('/load-products')
        except:
            outputFile = f'app/templates/products/{slug}.json'
            with open(outputFile, "w") as outfile: 
                outfile.write( product )
                outfile.close()
            return redirect('/load-products')
    else:
        return redirect('/load-products')


@app.route('/update-product/<path>/', methods=['GET', 'POST'])
@login_required
def update_product(path):
    if request.method == 'POST':
        product = request.form.get('product')
        featured = request.form.get('featured')

        print(request.form.get('price'))

        # main image
        main_image = request.files.get('main_image', "")
        main_img = ''
        if main_image:
            main_img = base64.b64encode(main_image.read()).decode()
        elif request.form.get('main_img_link'):
            main_img = request.form.get('main_img_link')
        else:
            main_img = json.loads(product)['img_main']

        
        # card image
        card_image = request.files.get('card_image', "")
        card_img = ''
        if card_image:
            card_img = base64.b64encode(card_image.read()).decode()
        elif request.form.get('card_img_link'):
            card_img = request.form.get('card_img_link')
        else:
            card_img = json.loads(product)['img_card']
        
        # image 1
        image_1 = request.files.get('image_1', "")
        img_1 = ''
        if image_1:
            img_1 = base64.b64encode(image_1.read()).decode()
        elif request.form.get('img1_link'):
            img_1 = request.form.get('img1_link')
        else:
            img_1 = json.loads(product)['img_1']

        # image 2
        image_2 = request.files.get('image_2', "")
        img_2 = ''
        if image_2:
            img_2 = base64.b64encode(image_2.read()).decode()
        elif request.form.get('img2_link'):
            img_2 = request.form.get('img2_link')
        else:
            img_2 = json.loads(product)['img_2']

        # image 3
        image_3 = request.files.get('image_3', "")
        img_3 = ''
        if image_3:
            img_3 = base64.b64encode(image_3.read()).decode()
        elif request.form.get('img3_link'):
            img_3 = request.form.get('img3_link')
        else:
            img_3 = json.loads(product)['img_3']

        prod = {
            'id': json.loads(product)['id'],
            'name': json.loads(product)['name'],
            'currency': json.loads(product)['currency'],
            'price': request.form.get('price'),
            'full_description': request.form.get('full_description'),
            'info': request.form.get('info'),
            'img_main': main_img,
            'img_card': card_img,
            'img_1': img_1,
            'img_2': img_2,
            'img_3': img_3,
        }

        try:
            if featured:
                outputFile = f'app/templates/products/featured.json'
            else:
                outputFile = f'app/templates/products/{path}.json'

            with open(outputFile, "r+") as outfile:
                outfile.seek(0)
                outfile.write(json.dumps(prod, indent=4, separators=(',', ': ')))
                # messages.success(request, 'Product updated!')
                outfile.truncate()
            return redirect('/load-products')
        except:
            # messages.error(request, "You can't update product id or name!")
            return redirect('/load-products')  
    else:
        return redirect('/load-products')


@app.route('/delete-product/<path>/', methods=['GET', 'POST'])
@login_required
def delete_product(path):
    try:
        outputFile = f'app/templates/products/{path}.json'
        os.remove(outputFile)
        # messages.success(request, "Product Deleted!")
        return redirect('/load-products')
    except:
        # messages.error(request, "You can't delete the product.")
        return redirect('/load-products')  




# Custom Filter
@app.template_filter('product_name')
def product_name(obj):
    return json.loads(obj)['name']

@app.template_filter('product_price')
def product_price(obj):
    return json.loads(obj)['price']

@app.template_filter('product_description')
def product_description(obj):
    return json.loads(obj)['full_description']

@app.template_filter('product_info')
def product_info(obj):
    return json.loads(obj)['info']

@app.template_filter('product_main_image')
def product_main_image(obj):
    return json.loads(obj)['img_main']

@app.template_filter('product_card_image')
def product_card_image(obj):
    return json.loads(obj)['img_card']

@app.template_filter('product_image1')
def product_image1(obj):
    return json.loads(obj)['img_1']

@app.template_filter('product_image2')
def product_image2(obj):
    return json.loads(obj)['img_2']

@app.template_filter('product_image3')
def product_image3(obj):
    return json.loads(obj)['img_3']


@app.template_filter('product_slug')
def product_slug(obj):
    name = json.loads(obj)['name']
    slug = name.lower().replace(' ', '-')
    return slug

@app.template_filter('starts_with')
def starts_with(obj):
    if obj.startswith('http'):
        return True
    return False

@app.template_filter
def is_logged_in():
    if current_user.is_authenticated:
        return True
    return False