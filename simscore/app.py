from flask import Flask, request #import main Flask class and request object
from sentence_Sim_v3 import calculate_sim

app = Flask(__name__) #create the Flask app


@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_sim():
    if request.method == 'POST': #this block is only entered when the form is submitted
        s1 = request.form.get('s1')
        s2 = request.form['s2']
        ans = calculate_sim(s1, s2)
        return '''<h1>The Similarity score is: {}</h1>'''.format( str(ans) )

    #run whether GET or POST
    return '''<form method="POST">
                  Enter sentences to get similarity<br><br>
                  Sentence #1: <br>
                  <textarea rows="3" cols="80" name="s1" > </textarea> <br> <br>
                  Sentence #2: <br>
                  <textarea rows="3" cols="80" name="s2" > </textarea> <br>
                  <br>
                  <input type="submit" value="Submit"><br>
              </form>
            '''

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') #run app in debug mode