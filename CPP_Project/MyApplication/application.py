import os
#import key_config as keys
import boto3 
from flask import Flask, flash, render_template, request, redirect, send_file, url_for
from s3 import list_files, download_file, upload_file
from flask_bootstrap import Bootstrap
from welcome_pkg import welcome_properties #my library creation



app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "myapp-s3-011220"
bootstrap = Bootstrap(app)


dynamodb = boto3.resource('dynamodb')
articlesTable = dynamodb.Table('Articles')

from boto3.dynamodb.conditions import Key, Attr

@app.route('/')
def entry_point():
    return render_template('registration.html') #this is your landing page to Sign up
    #return 'Hello World!'


@app.route("/storage")
def storage():
   contents = list_files("myapp-s3-011220")
   return render_template('storage.html', contents=contents)
   
@app.route("/upload")
def upload():
    return render_template('upload.html') 

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    results = articlesTable.scan()
    contents = []
    
    for i in results['Items']:
        article = {}
        article['Headline'] = i['headline'] 
        article['Subline'] = i['subline']
        article['BodyText'] = i['body']
        contents.append(article)
    
    return render_template('main.html', contents=contents)
    
    
    
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/check',methods = ['post']) 
def check():
    if request.method=='POST':
        
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('users')
        response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])
        if password == items[0]['password']:
            #return redirect("/storage")
            welcome = welcome_properties.WelcomeMessage(name) #function from my library
            name = welcome.welcomeName()
            return render_template("upload.html",name = name)
    return render_template("login.html")


@app.route('/article',methods = ['post']) 
def article():
    if request.method=='POST':
        
        headline = request.form['headline']
        subline = request.form['subline']
        body = request.form['body']

        table = dynamodb.Table('Articles')
        table.put_item(
            Item={
                'headline': headline,
                'subline': subline,
                'body': body
            }
        )
        msg = "Thank you. Your article has been published."
    
    return render_template('form.html',msg = msg)
        
@app.route('/register', methods=['post', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('users')
        
        table.put_item(
                Item={
        'name': name,
        'email': email,
        'password': password
            }
        )
        msg = "Registration Complete. Please Login to your account"
    
        return render_template('login.html',msg = msg)
    return render_template('registration.html')
    

@app.route("/images", methods=['POST'])
def images():
    if request.method == "POST":
        if request.files['file']:
            f = request.files['file']
            f.save(f.filename)
            upload_file(f"{f.filename}", BUCKET)
            return redirect("/storage")



@app.route("/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)
