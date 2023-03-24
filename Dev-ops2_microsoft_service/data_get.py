from flask import Flask, request, jsonify
import datetime
import item as us

app = Flask(__name__)


@app.route('/g_items', methods=['GET'])
def item():
    _item = us.item_name()
    return jsonify(_item)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2005, debug=True) 