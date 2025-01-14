from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.form
    
    # Prepare the data for PatentSafe
    ps_data = {
        'authorId': data['username'],
        'url': data['url']
    }
    
    submit_url = f"{data['server'].rstrip('/')}/submit/http_retrieval"
    
    try:
        response = requests.post(
            submit_url,
            json=ps_data
        )
        response.raise_for_status()
        return jsonify({'success': True, 'message': response.text})
    except requests.exceptions.RequestException as e:
        return jsonify({'success': False, 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 