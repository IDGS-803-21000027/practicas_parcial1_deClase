from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/default")
@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

        selected_operation = request.form.get("operacion")

        if selected_operation == "suma":
            result = int(num1) + int(num2)
        elif selected_operation == "resta":
            result = int(num1) - int(num2)
        elif selected_operation == "multiplicacion":
            result = int(num1) * int(num2)
        elif selected_operation == "division":
            result = int(num1)/int(num2)
        return "<h1>El resultado es: {}</h1>".format(str(result))

if __name__=="__main__":
    app.run(debug=True)