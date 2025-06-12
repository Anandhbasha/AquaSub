# %%
import ipywidgets as widgets
from IPython.display import display

#  Numeric Widgets
# IntSlider
slider = widgets.IntSlider(value=5, min=0, max=10)
display(slider)

# FloatSlider
float_slider = widgets.FloatSlider(value=2.5, min=0, max=5.0, step=0.1, description='Float:')
display(float_slider)

# IntText
int_text = widgets.IntText(value=42, description='IntText:')
display(int_text)

# BoundedIntText
bounded_int = widgets.BoundedIntText(
    value=10,
    min=5,
    max=15,
    step=1,
    description='Bounded Int:'
)
display(bounded_int)


# Play Widget (for animations)
play = widgets.Play(
    value=0,
    min=0,
    max=10,
    step=1,
    interval=500,  # milliseconds
    description="Press play"
)
display(play)


check = widgets.Checkbox(value=False, description='I agree')
display(check)

toggle = widgets.ToggleButton(value=False, description='ON/OFF')
display(toggle)

# Boolean Widgets
dropdown = widgets.Dropdown(
    options=['Python', 'Java', 'C++'],
    value='Python',
    description='Language:',
)
display(dropdown)

# Selection Widgets
radio = widgets.RadioButtons(
    options=['Male', 'Female', 'Other'],
    description='Gender:',
)
display(radio)

# String Widgets
text = widgets.Text(value='', placeholder='Enter name', description='Name:')
textarea = widgets.Textarea(placeholder='Enter comments here...', description='Comments:')
password = widgets.Password(description='Password:')
display(text, textarea, password)

# Date Picker
date_picker = widgets.DatePicker(
    description='Pick a Date',
    disabled=False
)
display(date_picker)

# Color Picker
color_picker = widgets.ColorPicker(
    concise=False,
    description='Pick a Color:',
    value='#ff0000'
)
display(color_picker)

# Container Widgets
slider1 = widgets.IntSlider(description='S1')
slider2 = widgets.IntSlider(description='S2')

box = widgets.VBox([slider1, slider2])
display(box)

accordion = widgets.Accordion(children=[text, textarea])
accordion.set_title(0, 'Name')
accordion.set_title(1, 'Comments')
display(accordion)

# Creating a GUI Application
name = widgets.Text(placeholder='Enter your name', description='Name:')
age = widgets.IntSlider(min=0, max=100, value=25, description='Age:')
btn = widgets.Button(description='Submit')
output = widgets.Output()

def on_btn_click(b):
    with output:
        output.clear_output()
        print(f"Hello {name.value}! You are {age.value} years old.")

btn.on_click(on_btn_click)

form = widgets.VBox([name, age, btn, output])
display(form)

#mini Example
name = widgets.Text(description='Name:')
age = widgets.IntSlider(min=0, max=100, value=25, description='Age:')
submit = widgets.Button(description='Submit')
output = widgets.Output()

def on_click(b):
    with output:
        output.clear_output()
        print(f"Hello {name.value}, you are {age.value} years old.")

submit.on_click(on_click)
display(name, age, submit, output)


# %%
