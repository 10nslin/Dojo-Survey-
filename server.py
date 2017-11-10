from flask import Flask, render_template, request, redirect,session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
  print "Got Post Info"
  session['name']= request.form['name']
  session['comment']= request.form['comment']
  session['language']= request.form['language']
  session['location']= request.form['location']

  if len(session['name'])< 1:
    flash("Name cannot be empty!")
    return redirect('/')
  elif len(session['comment'])< 2:
    flash("Comment field cannot be empty")
    return redirect('/')
  elif len(session['comment'])> 120:
    flash("Please Keep this comments 120 Characters.")
    return redirect('/')
  else:
    return render_template("result.html")

  return redirect('/')

app.run(debug=True) 