from flask import Flask , render_template, request, jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/box")
def box():
    return render_template("box.html")

@app.route("/card")
def card():
    return render_template("card.html")

@app.route("/page4")
def page4():
    return render_template("page4.html")

@app.route("/page6")
def page6():
    return render_template("page6.html")

@app.route('/store', methods=['POST'])
def store_data():
    data = request.form.get('input_value')
    if data:
        # Store the data in a text file
        with open('data.txt', 'a') as file:
            file.write(data + '\n')
        return jsonify({'message': 'Data stored successfully'})
    return jsonify({'error': 'No data received'})

if __name__ == '__main__':
    app.run()

