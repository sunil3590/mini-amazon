from flask import Flask
app = Flask('mini-amazon')


@app.route('/')
def index():
    return "<h1>Welcome to Mini Amazon</h1>"


@app.route('/products/<name>')
def add_product(name):
    return '<h1>This is, {0}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
