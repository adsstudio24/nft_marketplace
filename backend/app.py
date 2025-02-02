from flask import Flask, request, jsonify

app = Flask(__name__)

nfts = []

@app.route('/nfts', methods=['GET'])
def get_nfts():
    return jsonify(nfts)

@app.route('/nfts', methods=['POST'])
def add_nft():
    data = request.json
    nfts.append(data)
    return jsonify({"message": "NFT додано!"})

if __name__ == '__main__':
    app.run(debug=True)
