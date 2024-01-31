from wtforms import Form
from wtforms import IntegerField,FloatField

class distaciaForm(Form):
    x1 = IntegerField('x1')
    x2 = IntegerField('x2')
    y1 = IntegerField('y1')
    y2 = IntegerField('y2')
    dis=FloatField('dis')