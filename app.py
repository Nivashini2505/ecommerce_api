from flask import Flask, request, jsonify, render_template

from models import db, Product

print("=" * 60)
print("APP.PY LOADED - THIS IS THE UPDATED VERSION")
print("=" * 60)

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


# =========================
# ADD PRODUCT
# =========================

@app.route('/products', methods=['POST'])
def add_product():
    try:
        with open('error_log.txt', 'a') as f:
            f.write("=" * 60 + "\n")
            f.write("REQUEST STARTED\n")
            f.flush()

        if not request.is_json:
            return jsonify({
                "error": "Content-Type must be application/json"
            }), 400

        data = request.get_json()

        with open('error_log.txt', 'a') as f:
            f.write(f"Got JSON data: {data}\n")
            f.flush()

        if not data:
            return jsonify({
                "error": "Request body cannot be empty"
            }), 400

        name = data.get("name")
        price = data.get("price")
        quantity = data.get("quantity")

        with open('error_log.txt', 'a') as f:
            f.write(f"name={name}, price={price}, quantity={quantity}\n")
            f.flush()

        # VALIDATIONS

        if name is None or price is None or quantity is None:
            return jsonify({
                "error": "All fields are required"
            }), 400

        if not isinstance(name, str):
            return jsonify({
                "error": "Name must be string"
            }), 400

        if len(name.strip()) == 0:
            return jsonify({
                "error": "Name cannot be empty"
            }), 400

        if not isinstance(price, (int, float)):
            return jsonify({
                "error": "Price must be number"
            }), 400

        if price <= 0:
            return jsonify({
                "error": "Price must be greater than 0"
            }), 400

        if not isinstance(quantity, (int, float)) or (isinstance(quantity, float) and quantity != int(quantity)):
            with open('error_log.txt', 'a') as f:
                f.write(f"Quantity validation failed: isinstance={isinstance(quantity, (int, float))}, float_check={isinstance(quantity, float) and quantity != int(quantity)}\n")
                f.flush()
            return jsonify({
                "error": "Quantity must be integer"
            }), 400

        quantity = int(quantity)

        with open('error_log.txt', 'a') as f:
            f.write(f"After conversion: quantity={quantity}\n")
            f.flush()

        if quantity < 0:
            return jsonify({
                "error": "Quantity cannot be negative"
            }), 400

        existing_product = Product.query.filter_by(name=name).first()

        if existing_product:
            return jsonify({
                "error": "Product already exists"
            }), 409

        product = Product(
            name=name.strip(),
            price=price,
            quantity=quantity
        )

        with open('error_log.txt', 'a') as f:
            f.write(f"Created product object\n")
            f.flush()

        db.session.add(product)
        
        with open('error_log.txt', 'a') as f:
            f.write(f"Added to session\n")
            f.flush()

        db.session.commit()

        with open('error_log.txt', 'a') as f:
            f.write(f"Committed to database\n")
            f.flush()

        return jsonify({
            "message": "Product added successfully",
            "product": product.to_dict()
        }), 201
    except Exception as e:
        with open('error_log.txt', 'a') as f:
            f.write(f"EXCEPTION CAUGHT: {str(e)}\n")
            import traceback
            f.write(traceback.format_exc())
            f.flush()
        return jsonify({
            "error": f"Server error: {str(e)}"
        }), 500


# =========================
# GET ALL PRODUCTS
# =========================

@app.route('/products', methods=['GET'])
def get_products():

    products = Product.query.all()

    return jsonify({
        "count": len(products),
        "products": [product.to_dict() for product in products]
    })


# =========================
# GET SINGLE PRODUCT
# =========================

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):

    product = db.session.get(Product, id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify(product.to_dict())


# =========================
# UPDATE PRODUCT
# =========================

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):

    product = db.session.get(Product, id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    if not request.is_json:
        return jsonify({
            "error": "Content-Type must be application/json"
        }), 400

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body cannot be empty"
        }), 400

    # Update price if provided
    if 'price' in data:
        price = data.get('price')
        if not isinstance(price, (int, float)):
            return jsonify({
                "error": "Price must be number"
            }), 400
        if price <= 0:
            return jsonify({
                "error": "Price must be greater than 0"
            }), 400
        product.price = price

    # Update quantity if provided
    if 'quantity' in data:
        quantity = data.get('quantity')
        if not isinstance(quantity, (int, float)) or (isinstance(quantity, float) and quantity != int(quantity)):
            return jsonify({
                "error": "Quantity must be integer"
            }), 400
        quantity = int(quantity)
        if quantity < 0:
            return jsonify({
                "error": "Quantity cannot be negative"
            }), 400
        product.quantity = quantity

    # Update name if provided
    if 'name' in data:
        name = data.get('name')
        if not isinstance(name, str):
            return jsonify({
                "error": "Name must be string"
            }), 400
        if len(name.strip()) == 0:
            return jsonify({
                "error": "Name cannot be empty"
            }), 400
        product.name = name.strip()

    db.session.commit()

    return jsonify({
        "message": "Product updated successfully",
        "product": product.to_dict()
    }), 200


# =========================
# DELETE PRODUCT
# =========================

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):

    product = db.session.get(Product, id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "message": "Product deleted successfully"
    })


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)