from flask import Flask, render_template, request
import forms
import math

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
    
@app.route("/distancia", methods=["GET","POST"])
def distancia():
    dis=""
    dis_form = forms.distaciaForm(request.form)
    if request.method=="POST":
        x1=dis_form.x1.data
        x2=dis_form.x2.data
        y1=dis_form.y1.data
        y2=dis_form.y2.data
        dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template("distancia.html", form=dis_form,dis=dis)


@app.route("/res", methods=["GET","POST"])
def res():
    min = 0
    max = 0
    res = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    b1=""
    b2=""
    b3=""
    temp=""
    res_form = forms.resForm(request.form)
    if request.method=="POST":
        c1=res_form.c1.data
        c2=res_form.c2.data
        c3=res_form.c3.data
        c4=res_form.c4.data
        if c4 == 0.1:
            temp = "Silver"
        else:
            temp = "Gold"

        
        b1 = res_form.c1.choices[int(c1)][1]
        
        b2 = res_form.c2.choices[int(c2)][1]

        b3 = res_form.c3.choices[len(c3)-1][1]
        

        res = int(str(c1) + str(c2))*int(c3)
        min = res - (res* float(c4))
        max = res + (res*float(c4))

    return render_template("resistencias.html", form=res_form,res=res,min=min,max=max,c1=c1,c2=c2,c3=c3,c4=c4,b1=b1,b2=b2,b3=b3,temp=temp)


if __name__=="__main__":
    app.run(debug=True)