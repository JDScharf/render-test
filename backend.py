from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (representing your table)
table_data = [
    {"column1": "objectID", "column2": "price", "column3": "season", "column4": "kind of scents", "column5": "where prefer to shop"},
    {"column1": "1", "column2": "10-50", "column3": "Summer", "column4": "Floral", "column5": "Online"}  
    # add the rest of your 50 rows here
]

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(table_data)

if __name__ == '__main__':
    app.run(debug=True)
