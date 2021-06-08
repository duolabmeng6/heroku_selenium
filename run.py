# from flask import Flask, send_file, make_response, request
from flask import Flask
# import test as t
# import io

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'Hello World! 123321'


# @my_awesome_app.route("/gethtml", methods=['get'])
# def gethtml():
#     url = request.args.get("url")
#     html = t.gethtml(url)
#     return html
#
#
# @my_awesome_app.route("/getpng", methods=['get'])
# def getpng():
#     url = request.args.get("url")
#     image_data = t.getpng(url)
#
#     response = make_response(image_data)
#     response.headers['Content-Type'] = 'image/jpg'
#     return response

    # return send_file(
    #     io.BytesIO(html),
    #     mimetype='image/png',
    #     as_attachment=True,
    #     attachment_filename='result.jpg'
    # )


if __name__ == '__main__':
    my_awesome_app.run()
