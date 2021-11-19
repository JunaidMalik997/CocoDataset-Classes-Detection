import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask.views import MethodView
from werkzeug.utils import secure_filename
from files.testmain import CocoDataset
from files.shareFile import FileSharer

app=Flask(__name__)

UPLOAD_FOLDER='static/images/'

app.secret_key='super secret key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class ImageUpload(MethodView):

    def get(self):
        return render_template('index.html')

    def allowed_file(self, fileName):
        return '.' in fileName and fileName.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

    def post(self):
        target=os.path.join(APP_ROOT, 'static/images/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file=request.files['file']
        if file.filename=='':
            flash('No Image Selected for Upload')
            return redirect(request.url)
        if file and self.allowed_file(file.filename):
            filename=secure_filename(file.filename)
            flash('Image Successfully Uploaded and Displayed Below')
            destination = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(destination)

            coco = CocoDataset()
            file = coco.detection(destination)
            savedDetection = 'myfile.jpg'
            file.save(target + savedDetection)
            print('Successful Execution.')

            fileSharer=FileSharer(target+savedDetection)

            return render_template('index.html', upload=True, savedDetection=savedDetection, fileSharer=fileSharer)
        else:
            flash('Allowed Image Types are png, jpg, jpeg, gif')
            return redirect(request.url)

class Cococlasses(MethodView):

    def get(self):
        class_names=['person','bicycle','car','motorbike','aeroplane', 'bus','train','truck','boat','traffic light','fire hydrant',
         'stop sign','parking meter','bench','bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe',
         'backpack','umbrella','handbag','tie','suitcase','frisbee','skis','snowboard','sports ball','kite','baseball bat',
         'baseball glove','skateboard','surfboard','tennis racket','bottle','wine glass','cup','fork','knife','spoon',
         'bowl','banana','apple','sandwich','orange','broccoli','carrot','hot dog','pizza','donut','cake','chair','sofa',
         'pottedplant','bed','diningtable','toilet','tvmonitor','laptop','mouse','remote','keyboard','cell phone','microwave',
         'oven','toaster','sink','refrigerator','book','clock','vase','scissors','teddy bear','hair drier','toothbrush']
        return render_template('classnames.html', class_names=class_names)

@app.errorhandler(413)
def page_not_found(error):
    return redirect(url_for("homepage")), 413

app.add_url_rule('/', view_func=ImageUpload.as_view('homepage'))
app.add_url_rule('/cococlasses', view_func=Cococlasses.as_view('cococlasses_page'))

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

#<a href="{{(fileSharer.share())}}">View Image in Full Size</a>