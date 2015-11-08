##
## @Author: Geoffrey Bauduin <bauduin.geo@gmail.com>
##

from flask import Flask, request
from werkzeug import secure_filename
from process import Processer

app = Flask(__name__)

@app.route("/", methods=["GET"])
def status():
	return "true"
	
@app.route("/process", methods=["POST"])
def process():
	file = request.files['file']
	if file:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return "true"

app.config['UPLOAD_FOLDER'] = "./uploads/"

processer = Processer()

if __name__ == "__main__":	
	processer.compare("./example_dataset/step1/num_0.bmp")
	app.run()