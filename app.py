from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from scraper import scrape
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv("MONGO_URI")
mongo = PyMongo(app)
db = mongo.db
PRODUCTS = db[os.getenv("PRODUCTS")]
COLLECTION = db[os.getenv("COLLECTION")]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price', methods=['POST'])
def get_price():
    try:
        product_url = request.form.get('product_url')
        platform = request.form.get('platform')

        if not product_url or not platform:
            raise ValueError("Product URL and platform are required")

        product_name, price = asyncio.run(scrape(product_url, platform))
        
        if product_name is None or price is None:
            return jsonify({"error": "Failed to fetch price"}), 500

        # Fetch product details from MongoDB
        product_details = PRODUCTS.find_one({"url": product_url})
        
        if product_details:
            previous_price = product_details.get("previous_price", "N/A")
            lowest_price = product_details.get("lower", "N/A")
            highest_price = product_details.get("upper", "N/A")
        else:
            previous_price = lowest_price = highest_price = "N/A"

        return render_template(
            'product.html', 
            product_name=product_name, 
            price=price,
            previous_price=previous_price,
            lowest_price=lowest_price,
            highest_price=highest_price
        )

    except Exception as e:
        print(f"Error in get_price: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
