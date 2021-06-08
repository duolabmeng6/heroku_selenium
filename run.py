from flask import Flask, send_file, make_response,request
import seleniumUtil
import io

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '测试一下 seleniumUtil 部署到 Heroku'


@app.route("/gethtml", methods=['get'])
def gethtml():
    url = request.args.get("url")
    html = seleniumUtil.gethtml(url)
    return html


@app.route("/getpng", methods=['get'])
def getpng():
    url = request.args.get("url")
    image_data = seleniumUtil.getpng(url)

    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/jpg'
    return response
    # 发送文件
    # return send_file(
    #     io.BytesIO(html),
    #     mimetype='image/png',
    #     as_attachment=True,
    #     attachment_filename='result.jpg'
    # )


if __name__ == '__main__':
    app.run(debug=True)
