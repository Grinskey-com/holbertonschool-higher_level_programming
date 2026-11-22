#!/usr/bin/python3
"""Flask app that displays product data from JSON or CSV files."""
import csv
import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items from items.json and render them as a list."""
    try:
        with open(os.path.join(BASE_DIR, 'items.json'), 'r') as f:
            data = json.load(f)
        items_list = data.get('items', [])
    except (OSError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


def read_json():
    """Return the list of products stored in products.json."""
    with open(os.path.join(BASE_DIR, 'products.json'), 'r') as f:
        return json.load(f)


def read_csv():
    """Return the list of products stored in products.csv."""
    products = []
    with open(os.path.join(BASE_DIR, 'products.csv'), 'r', newline='') as f:
        for row in csv.DictReader(f):
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    """Display products from a JSON or CSV file, optionally filtered by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template('product_display.html',
                               error='Wrong source')

    try:
        data = read_json() if source == 'json' else read_csv()
    except (OSError, ValueError, KeyError):
        return render_template('product_display.html',
                               error='Could not read data file')

    if product_id is not None:
        try:
            wanted = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error='Product not found')
        data = [p for p in data if p.get('id') == wanted]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
