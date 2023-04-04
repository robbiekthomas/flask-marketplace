from flask import Flask, render_template, jsonify

app = Flask(__name__)

ITEMS = [
  {
    'id': 1,
    'title': 'Paddle',
    'price': 29.99,
    'description': 'beautiful rowing paddle'
  },
   {
    'id': 2,
    'title': 'Canoe',
    'price': 2999.99,
    'description': 'Brand new wooden conoe'
  },
   {
    'id': 3,
    'title': 'Life Jacket',
    'price': 14.99,
    'description': 'slightly used life jacket, medium sized'
  },
     {
    'id': 4,
    'title': 'Kayak',
    'price': 1899.99,
    'description': 'white water kayak, slightly used'
  },
]


@app.route("/")
def hello_world():
    return render_template('home.html', items=ITEMS)

@app.route("/api/items")
def list_items():
  return jsonify(ITEMS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)