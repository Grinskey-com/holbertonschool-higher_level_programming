#!/usr/bin/python3
"""Flask app that displays product data from JSON, CSV or SQLite."""
import csv
import json
import os
import sqlite3

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


def read_sql():
    """Return the list of products stored in the products.db database."""
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'products.db'))
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


@app.route('/products')
def products():
    """Display products from JSON, CSV or SQL, optionally filtered by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html',
                               error='Wrong source')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()
    except sqlite3.Error:
        return render_template('product_display.html',
                               error='Database error')
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
