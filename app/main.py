from flask import Flask, redirect, render_template, request, jsonify, url_for
from app.database import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flavors')
def flavors():
    conn = get_db_connection()
    flavors = conn.execute('SELECT * FROM seasonal_flavors').fetchall()
    conn.close()
    return render_template('flavors.html', flavors=flavors)

@app.route('/cart')
def cart():
    conn = get_db_connection()
    cart = conn.execute('SELECT * FROM cart').fetchall()
    conn.close()
    return render_template('cart.html', cart=cart)

@app.route('/allergens')
def allergens():
    conn = get_db_connection()
    allergens = conn.execute('SELECT * FROM allergens').fetchall()
    conn.close()
    return render_template('allergens.html', allergens=allergens)

@app.route('/flavors/add', methods=['POST'])
def add_flavor():
    new_flavor = request.form
    name = new_flavor['name']
    description = new_flavor['description']
    availability = new_flavor['availability']

    conn = get_db_connection()
    conn.execute('INSERT INTO seasonal_flavors (name, description, availability) VALUES (?, ?, ?)',
                 (name, description, availability))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Flavor added'}), 201

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    new_item = request.form
    product_name = new_item['product_name']

    conn = get_db_connection()
    conn.execute('INSERT INTO cart (product_name) VALUES (?)', (product_name,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Item added to cart'}), 201

@app.route('/allergens/add', methods=['POST'])
def add_allergen():
    new_allergen = request.form
    name = new_allergen['name']

    conn = get_db_connection()
    conn.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Allergen added'}), 201

@app.route('/search_flavors')
def search_flavors():
    query = request.args.get('query', '')
    conn = get_db_connection()
    flavors = conn.execute('SELECT name FROM seasonal_flavors WHERE name LIKE ?', ('%' + query + '%',)).fetchall()
    conn.close()
    return jsonify([{'name': flavor['name']} for flavor in flavors])

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    conn = get_db_connection()

    if request.method == 'POST':
        new_ingredient = request.form
        name = new_ingredient['name']
        quantity = new_ingredient['quantity']

        conn.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        conn.close()
        return redirect(url_for('inventory'))

    ingredients = conn.execute('SELECT * FROM ingredients').fetchall()
    conn.close()
    return render_template('inventory.html', Ingredients=ingredients)
if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
