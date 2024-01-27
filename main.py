from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/cinepolis")
def cine():
    return render_template("cinepolis.html")

@app.route("/procesar", methods=["GET", "POST"])
def procesar():
    if request.method=="POST":
        nom = str(request.form.get("nombre"))
        canCom = int(request.form.get("cantidadCompradores"))
        
        Tar = str(request.form.get("pagoRadio"))
        canBol = int(request.form.get("cantidadBoletos"))

        if canCom == 0:
            return "No se puede realizar la operación. La cantidad de compradores es 0."

        if float(canBol) / float(canCom) > 7: 
            return "No se pueden comprar {} boletos, el máximo por persona es 7".format(str(canBol))
        else:
            if float(canBol) > 5:
                canPag = float(canBol) * 12 * 0.85
            elif float(canBol) > 2:
                canPag = float((float(canBol) * 12)) * 0.90
            else:
                canPag = (float(canBol) * 12)
        if Tar == "si":
            canPag = float(canPag) * 0.90
    return render_template("cinepolis.html", canPag=canPag, nom=nom)
         



@app.route("/")
def formulario():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

        selected_operation = request.form.get("operacion")

        if selected_operation == "suma":
            result = float(num1) + float(num2)
        elif selected_operation == "resta":
            result = float(num1) - float(num2)
        elif selected_operation == "multiplicacion":
            result = float(num1) * float(num2)
        elif selected_operation == "division":
            result = float(num1)/float(num2)
        return "<h1>El resultado es: {}</h1>".format(str(result))

if __name__=="__main__":
    app.run(debug=True)