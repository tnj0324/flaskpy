from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/")
def file_download():
    return ("<a href='/downloads/csco-daily.csv' download='csco-daily.csv'>ダウンロード</a>")

@app.route("/test")
def hogehoge():
    return ("<p>test</p>")

@app.route('/downloads/<path:filename>')
def download_file(filename):
    print(filename)
    return send_from_directory('data',
                               filename, as_attachment=True)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
