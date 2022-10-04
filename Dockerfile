FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Used by Stripe for callback URL 
# for successful payment and cancelled
ENV SERVER_ADDRESS http://localhost:5085/

# Stripe Secrets 
ENV STRIPE_PUBLISHABLE_KEY pk_test_51HlWtGGLLd1X07VUPujufXrN8JHjn76lzLOZ16zjo895ffZCC4JwcAAipINEC0CVFxjFGmHr1YxRf96JbhPiUeVU00uhxqX2uL
ENV STRIPE_SECRET_KEY      sk_test_51HlWtGGLLd1X07VUIwU3iPZAK9mGdR8GtwSUAAkkyoOl3KpE4BWyIU3BX4mAcofaRrTFQIh4jFPSJHHk1njpwKMC00q3tPjAe7

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY env.sample .env

COPY . .

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
