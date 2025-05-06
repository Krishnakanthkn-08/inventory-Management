from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Admin@localhost:5432/inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Product Model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class ProductLocation(db.Model):
    __tablename__ = 'product_locations'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    product = db.relationship('Product', backref='locations')

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product')
def product():
    return render_template('product_maintain.html')

@app.route('/location')
def location():
    products = Product.query.all()
    return render_template('product_location.html', products=products)

@app.route('/movement')
def movement():
    return render_template('savelocation.html')

@app.route("/report")
def report():
    products = Product.query.all()
    report_data = []

    for product in products:
        try:
            # Safeguard against None values
            price = product.price if product.price is not None else 0.0
            quantity = product.quantity if product.quantity is not None else 0
            total_value = price * quantity
        except Exception as e:
            total_value = 0.0  # If any exception occurs, total_value will be 0

        report_data.append({
            'name': product.name,
            'price': float(price),
            'quantity': quantity,
            'total_value': total_value
        })

    return render_template("report.html", report_data=report_data)


    # return render_template("report.html", report_data=report_data)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
   
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    new_product = Product(name=name, quantity=quantity, price=price)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_location', methods=['POST'])
def add_location():
    product_id = request.form['product_id']
    location = request.form['location']

    new_location = ProductLocation(product_id=product_id, location=location)
    db.session.add(new_location)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
