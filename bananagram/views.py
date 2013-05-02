import json
import tempfile
import bananagram
from bananagram import app
from flask import (Flask, request, render_template, redirect, url_for,
    make_response)

app = Flask(__name__)

def get_word_list(string):
    return bananagram.trie.find_substrings(string)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/find', methods=['GET', 'POST'])
def find():
    """
    This is the view function to show all of the words.
    """
    if request.method == 'GET':
        return redirect(url_for('index'))
    if request.method == 'POST':
        string = request.form['string']
        word_list = get_word_list(string)
        context = dict(
            word_list=word_list,
            string=string)
    return render_template('index.html', word_list=word_list, string=string)
if __name__ == '__main__':
    # Generate the node on server startup
    app.run()


@app.route('/api', methods=['GET'])
def api():
    """
    This is the API endpoint for the application. The API outputs JSON that
    looks like this:

    {"word_list": ["he", "hole", "oh"], "string": "hello"}

    The API supports sorting by alphabetical order and by size.

    To sort by alphabetical order (asc/desc):
    http://localhost:5000/api?string=computer&alpha=asc

    To sort by size (asc/desc):
    http://localhost:5000/api?string=computer&size=asc

    To sort by size first then by alphabetical order:
    http://localhost:5000/api?string=computer&size=asc&alpha=desc
    """
    string = request.args.get('string', '')
    alpha = request.args.get('alpha', '')
    size = request.args.get('size', '')
    word_list = get_word_list(string)

    if alpha == 'asc':
        word_list.sort()
    elif alpha == 'desc':
        word_list.sort()
        word_list.reverse()
    if size == 'asc':
        word_list.sort(key=len)
    elif size == 'desc':
        word_list.sort(key=len, reverse=True)
    return json.dumps({'string': string, 'word_list': word_list})


@app.route('/xls', methods=['GET'])
def xls():
    """ This exports the list as an Excel spreadsheet. No sorting is applied """
    string = request.args.get('string', '')
    word_list = get_word_list(string)
    response = make_response(render_template(
        'word_list_xls.html', word_list=word_list, string=string))
    response.headers['Content-Type'] = "application/vnd.ms-excel"
    response.headers['Content-Disposition'] = "attachment; filename=word_list.xls"
    return response


@app.route('/txt', methods=['GET'])
def txt():
    """ This exports the list as a text file. No sorting is applied """
    string = request.args.get('string', '')
    word_list = get_word_list(string)
    response = make_response(render_template(
        'word_list_txt.html', word_list=word_list, string=string))
    response.headers['Content-Type'] = "text/plain"
    response.headers['Content-Disposition'] = "attachment; filename=word_list.txt"
    return response
