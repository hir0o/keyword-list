from flask import Flask, request
import json
import pke
app = Flask(__name__)
extractor = pke.unsupervised.MultipartiteRank()
@app.route("/",methods=["POST"])
def root():
    text = request.json['text']
    extractor.load_document(input=text, language='ja', normalization=None)
    extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
    extractor.candidate_weighting(threshold=0.74, method='average', alpha=1.1)
    res = extractor.get_n_best(10)
    result = json.dumps(res, ensure_ascii=False)
    return result
