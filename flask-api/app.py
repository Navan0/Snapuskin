import os
import shutil
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug import secure_filename
from distutils.dir_util import copy_tree


# Initialize the Flask application
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded files
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            filenames.append(filename)

    def text_num_split(item):
        for index, letter in enumerate(item, 0):
            if letter.isdigit():
                return [item[:index], item[index:]]
    app.config['UPLOAD_FOLDER'] = "uploads/"
    app.config['ROOT_FOLDER'] = "/"
    c_base = []
    # os.chdir(app.config['UPLOAD_FOLDER'])
    path, dirs, files = next(os.walk(app.config['UPLOAD_FOLDER']))
    for file in files:
        base1 = os.path.basename(file)
        base = os.path.splitext(base1)
        base = text_num_split(base[0])
        print(base[0])
        if base[0].strip():
            c_base.append(base[0])
    c_base = list(dict.fromkeys(c_base))

    for dic in c_base:
        os.mkdir(app.config['UPLOAD_FOLDER']+dic)
    for file in files:
        base1 = os.path.basename(file)
        base = os.path.splitext(base1)
        base = text_num_split(base[0])
        for dic in c_base:
            if base[0] in c_base:
                print(path+str(base1),app.config['UPLOAD_FOLDER']+base[0]+"/")
                # shutil.move(path+str(base1),app.config['UPLOAD_FOLDER']+base[0])
                shutil.copy(os.path.join(path, str(base1)), os.path.join(app.config['UPLOAD_FOLDER'], base[0]))
                print(os.path.join(path, str(base1)), os.path.join(app.config['UPLOAD_FOLDER'], base[0]))
        for bases in c_base:
            # os.makedirs(bases)
            # copy_tree(os.path.join(path, str(bases)),app.config['ROOT_FOLDER'])
            copy_tree(os.path.join(path, str(bases)), bases)

    print(c_base)
    shutil.rmtree(app.config['UPLOAD_FOLDER'])



    # for word in f.read().split():
    #     print(word)

    return render_template('upload.html', filenames=filenames)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run("0.0.0.0",5001,threaded=True,debug=True)
