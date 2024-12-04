from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

class MainScreen(Screen):
    def convert_units(self):
        try:
            gram_value = float(self.ids.gram_input.text) if self.ids.gram_input.text else 0
            liter_value = float(self.ids.liter_input.text) if self.ids.liter_input.text else 0
            meter_value = float(self.ids.meter_input.text) if self.ids.meter_input.text else 0
            celsius_value = float(self.ids.celsius_input.text) if self.ids.celsius_input.text else 0
            hour_value = float(self.ids.hour_input.text) if self.ids.hour_input.text else 0

            kilogram_value = gram_value / 1000
            milliliter_value = liter_value * 1000
            kilometer_value = meter_value / 1000
            fahrenheit_value = (celsius_value * 9/5) + 32
            minute_value = hour_value * 60

            self.ids.kg_output.text = f"{kilogram_value:.2f} kg"
            self.ids.ml_output.text = f"{milliliter_value:.2f} ml"
            self.ids.km_output.text = f"{kilometer_value:.2f} km"
            self.ids.fahrenheit_output.text = f"{fahrenheit_value:.2f} °F"
            self.ids.minute_output.text = f"{minute_value:.2f} min"
        except ValueError:
            self.ids.kg_output.text = "Erro"
            self.ids.ml_output.text = "Erro"
            self.ids.km_output.text = "Erro"
            self.ids.fahrenheit_output.text = "Erro"
            self.ids.minute_output.text = "Erro"

class UnitConverterApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        padding: [10, 50, 10, 10]
        spacing: 10

        MDTextField:
            id: gram_input
            hint_text: "Gramas"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: liter_input
            hint_text: "Litros"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: meter_input
            hint_text: "Metros"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: celsius_input
            hint_text: "Celsius"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: hour_input
            hint_text: "Horas"
            input_filter: 'float'
            multiline: False

        MDRaisedButton:
            text: "Converter"
            on_press: root.convert_units()

        MDLabel:
            id: kg_output
            text: "0 kg"
            halign: "center"

        MDLabel:
            id: ml_output
            text: "0 ml"
            halign: "center"

        MDLabel:
            id: km_output
            text: "0 km"
            halign: "center"

        MDLabel:
            id: fahrenheit_output
            text: "0 °F"
            halign: "center"

        MDLabel:
            id: minute_output
            text: "0 min"
            halign: "center"
'''

if __name__ == '__main__':
    UnitConverterApp().run()
