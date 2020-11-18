from flask import Flask, render_template, request
from tweet import SentimentAnalysis

app = Flask(__name__)

# Main Homepage
@app.route('/')
def index():
    return render_template("index.html")

# Route for sending data
@app.route('/data', methods = ['POST'])
def data():
    if request.method == "POST":
        # Initialising variable
        # output1 = ''
        # Will print true if request is JSON
        print("Request is in JSON Format : %s" % request.is_json)
        
        # Getting content of JSON 
        inputData = request.get_json()

        # data variable contains info you want to process
        data = inputData['data']
        searchTerm = int(inputData['searchTerm'])

        print("Searched for : " + data + "\n"+ "No of Tweets : "  + str(searchTerm))
        # -->>
        #

        gatherInfo = SentimentAnalysis(data, searchTerm)
        sentimentAnalysisOutput = gatherInfo.DownloadData()
        
        # if data == 'JaiShreeRam':
        #     output1 = 'YESS'
        # else:
        #     output1 = 'NOOO'
        
        output = {
            'inputQuery': data,
            'inputLimit': str(searchTerm),
            'poll' : str(sentimentAnalysisOutput['poll']),
            'positive' : str(sentimentAnalysisOutput['positive']),
            'wpositive' : str(sentimentAnalysisOutput['wpositive']),
            'spositive' : str(sentimentAnalysisOutput['spositive']),
            'negative' : str(sentimentAnalysisOutput['negative']),
            'wnegative' : str(sentimentAnalysisOutput['wnegative']),
            'snegative' : str(sentimentAnalysisOutput['snegative']),
            'neutral' : str(sentimentAnalysisOutput['neutral'])
        }
        return output

# For any invalid URL
# @app.errorhandler(404)
# def not_found(e):
#     return render_template("404.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
    # default port is 5000, can change by
    # app.run(port=3000)
    # but if you change port number make sure also change it in index.html at line number 37