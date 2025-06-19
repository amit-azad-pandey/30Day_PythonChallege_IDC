from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

#make sure to install the kivy module 

Window.size = (550, 350)
Window.clearcolor = (0.98, 0.93, 0.89, 1)  

class TempApp(App):
    def build(self): #giving ui the design
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=18)

        
        title = Label(
            text="TEMPERATURE CONVERTER!",
            font_size=34,
            bold=True,
            halign='center',
            color=(0.68, 0.85, 0.90, 1)
        )
        title.bind(size=title.setter('text_size'))
        self.layout.add_widget(title)

        
        input_row = BoxLayout(orientation='horizontal', spacing=12, size_hint_y=None, height=40)

        input_label = Label(
            text="Enter temperature:",
            font_size=15,
            color=(0.3, 0.3, 0.3, 1),
            size_hint=(0.5, 0.5),
            halign='right',
            valign='middle'
        )
        input_label.bind(size=input_label.setter('text_size'))

        self.temp_input = TextInput(
            multiline=False,
            font_size=14,
            padding=[10, 10]
        )

        input_row.add_widget(input_label)
        input_row.add_widget(self.temp_input)
        self.layout.add_widget(input_row)

        
        button_row = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=50)

        self.c2f_btn = Button(
            text="Celsius to Fahrenheit",
            background_color=(0.6, 0.8, 0.7, 1),
            color=(1, 1, 1, 1)
        )
        self.f2c_btn = Button(
            text="Fahrenheit to Celsius",
            background_color=(0.6, 0.8, 0.7, 1),
            color=(1, 1, 1, 1)
        )

        self.c2f_btn.bind(on_press=self.convert_c2f)
        self.f2c_btn.bind(on_press=self.convert_f2c)

        button_row.add_widget(self.c2f_btn)
        button_row.add_widget(self.f2c_btn)
        self.layout.add_widget(button_row)

        
        self.result_label = Label(
            text="",
            font_size=26,
            bold=True,
            color=(0.4, 0.1, 0.4, 1),
            halign='center'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.layout.add_widget(self.result_label)

        
        self.endline = Label(
            text="",
            font_size=14,
            italic=True,
            color=(0.4, 0.4, 0.4, 1),
            halign='center'
        )
        self.endline.bind(size=self.endline.setter('text_size'))
        self.layout.add_widget(self.endline)

        return self.layout

    def highlight_button(self, active_button):
        self.c2f_btn.background_color = (0.6, 0.8, 0.7, 1)
        self.f2c_btn.background_color = (0.6, 0.8, 0.7, 1)
        active_button.background_color = (1, 0.8, 0.3, 1)

    def convert_c2f(self, instance):
        self.highlight_button(self.c2f_btn)
        try:
            value = float(self.temp_input.text)
            result = (value * 9/5) + 32
            self.result_label.text = f"{value}°C = {result:.2f}°F"
            self.endline.text = "The temperature is dressed up in Fahrenheit now!"
        except ValueError:
            self.result_label.text = ""
            self.endline.text = "Oops! Please enter a valid number."

    def convert_f2c(self, instance):
        self.highlight_button(self.f2c_btn)
        try:
            value = float(self.temp_input.text)
            result = (value - 32) * 5/9
            self.result_label.text = f"{value}°F = {result:.2f}°C"
            self.endline.text = "The Temperature is living its best Celsius life!"
        except ValueError:
            self.result_label.text = ""
            self.endline.text = "Oops! Please enter a valid number."

if __name__ == '__main__':
    TempApp().run()