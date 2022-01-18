from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('tela.kv')

class MeuAplicativo (App):
    def build(self):
        return GUI
    def on_start(self):
        self.root.ids['valor1'].text = 'Hora Extra 30 %'
        self.root.ids['valor2'] = 'Hora Extra 40 %'
        self.root.ids['valor3'] = 'Hora Extra 50 %'
        self.root.ids['valor4'] = 'Hora Extra 100 %'
MeuAplicativo ().run()
