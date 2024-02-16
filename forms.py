from wtforms import Form
from wtforms import IntegerField,FloatField,SelectField,RadioField, StringField
from wtforms import validators

class distaciaForm(Form):
    x1 = IntegerField('x1')
    x2 = IntegerField('x2')
    y1 = IntegerField('y1')
    y2 = IntegerField('y2')
    dis=FloatField('dis')

class resForm(Form):
    # Define choices for SelectField
    CHOICES_SELECT1 = [('0', 'Black'), ('1', 'Brown'), ('2', 'Red'), ('3', 'Orange'), ('4', 'Yellow'), ('5', 'Green'), ('6', 'Blue'), ('7', 'Purple'), ('8', 'Grey'), ('9', 'White')]
    CHOICES_SELECT2 = [('1', 'Black'), ('10', 'Brown'), ('100', 'Red'), ('1000', 'Orange'), ('10000', 'Yellow'), ('100000', 'Green'), ('1000000', 'Blue'), ('10000000', 'Purple'), ('100000000', 'Grey'), ('1000000000', 'White')]

    # Define choices for RadioField
    CHOICES_RADIO = [('0.05', 'Gold'), ('0.1', 'Silver')]

    c1 = SelectField('c1', choices=CHOICES_SELECT1)
    c2 = SelectField('c2', choices=CHOICES_SELECT1)
    c3 = SelectField('c3', choices=CHOICES_SELECT2)
    c4 = RadioField('c4', choices=CHOICES_RADIO)

class diccionarioForm(Form):
    ingles = StringField('Ingles', [
        validators.DataRequired(message='El campo se necesita'),
        validators.length(min=2, max=10,message='Ingresa una palabra entre 2 y 10 caracteres')
    ])
    espanol = StringField('Espanol', [
        validators.DataRequired(message='El campo se necesita'),
        validators.length(min=2, max=10,message='Ingresa una palabra entre 2 y 10 caracteres')
    ])

class traduccionForm(Form):
    traduccion = StringField('Buscar', [
        validators.DataRequired(message='El campo se necesita'),
        validators.length(min=2, max=10,message='Ingresa una palabra entre 2 y 10 caracteres')
    ])

    elecciones = [('1', 'Ingles'), ('0', 'Espanol')]
    radio = RadioField('Lenguaje', choices=elecciones)