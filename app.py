import service.wordListToJsonService as wordToJson
import service.httpRequestService as httpRequest
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wordListAddDb',methods=["GET"])
def getJsonList():
    try:
        wordList = wordToJson.createJsonFile()
        httpRequest.httpRequestForJsonWord(wordList)
        print("response success")
        return jsonify({"msg": "Başarılı"})
    except:
        print("response fail")
        return jsonify({"msg": "Hata"})

if __name__ == "__main__":
    print("içerde")
    app.run(debug=False)