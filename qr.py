# file: qr.py
from flask import Flask, request, send_file, jsonify
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "QR Code API is running. Use /generate_qr?url=<your_url> to download a QR code image."
    })

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing "url" query parameter'}), 400

    qr_img = qrcode.make(url)
    buffer = io.BytesIO()
    qr_img.save(buffer, format="PNG")
    buffer.seek(0)

    # Force download with a dynamic filename
    filename = f"qr_code.png"
    return send_file(
        buffer,
        mimetype='image/png',
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
