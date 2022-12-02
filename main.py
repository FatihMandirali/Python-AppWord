import service.wordListToJsonService as wordToJson
import service.httpRequestService as httpRequest

wordList = wordToJson.createJsonFile()
httpRequest.httpRequestForJsonWord(wordList)