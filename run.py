from flask import Flask
app = Flask('mini-amazon')


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/')
def index():
    return "<h1>Welcome to Mini Amazon</h1>"


@app.route('/say-hello/<name>')
def add_product(name):
    return '<h1>Hello, {0}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
