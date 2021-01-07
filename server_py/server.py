from flask import Flask, Response, request, jsonify
from LinProg import *
from utils import generate_meta
import simplejson

app = Flask(__name__,
            static_url_path='', 
            static_folder='public',)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/post/data', methods=['GET', 'POST'])
def run():
    json_data = request.json
    data = create_matrix(json_data)
    results = solve(data, solver='highs-ds')
    print(results)
    results_dict = results.to_dict()
    results_dict['meta'] = generate_meta(json_data)
    return jsonify(simplejson.dumps(results_dict, ignore_nan=True, ensure_ascii=False))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
