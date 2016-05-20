from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button


class NumberTextBox(Widget):
    label = ObjectProperty(None)
    value = NumericProperty(0)
    
class DataTable(Widget):
    data = ObjectProperty(None)

class MainForm(Widget):
    startamount = ObjectProperty(None)
    monthlyamount = ObjectProperty(None)
    apr = ObjectProperty(None)
    years = ObjectProperty(None)
    datatable = ObjectProperty(None)
    submit = Button()
    
    #years = ObjectProperty(None)
    #interest = ObjectProperty(None)
    def init_values(self):
        self.startamount.label = "Starting Amount"
        self.startamount.value = 1000
        
        self.monthlyamount.label = "Monthly Amount"
        self.monthlyamount.value = 100
 
        self.apr.label = "APR"
        self.apr.value = 10
        
        self.years.label = "Term (Years)"
        self.years.value = 20
        
        self.datatable.data = "Default"
        
        self.submit.on_press = self.on_submit
        
    
    def on_submit(self):
        self.datatable.data = \
        "Start: {} \nMonthly: {} \nAPR: {}\nYears: {}".format( \
        self.startamount.value, \
        self.monthlyamount.value, \
        self.apr.value, \
        self.years.value, \
        )
        
        
class AmmortApp(App):
    def build(self):
        form = MainForm()
        form.init_values()
        return form


if __name__ == '__main__':
    AmmortApp().run()