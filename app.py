from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/test-get', methods=['GET'])
def test_get():
    data = {'Request Type':'GET',
            'Purpose':f'Tanush API "GET" Request Testing'}
    return jsonify(data)

@application.route('/test-post', methods=['POST'])
def test_post():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    application.run()