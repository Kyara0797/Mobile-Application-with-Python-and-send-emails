from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.image import Image

import yagmail

Window.size = (300, 600)

gmail_password = "ardgymwonqcxnpan"
food_menu = {
    "tacos": 12,
    "tamales": 10,
    "chicken rice": 16,
    "stewed meat": 20,
    "paella": 35
}

def send_email(total):
    sender_email = 'kyara.avalose@gmail.com'
    yag = yagmail.SMTP(sender_email, gmail_password)
    yag.send(
        to="kyara.avalose@gmail.com",
        subject="Restaurant Bill",
        contents=f"The total bill amount is: ${total}"
    )
    
    confirmation_popup = Popup(
        title='Confirmation',
        content=Label(
            text='Email sent successfully',
            color=(0, 0, 0, 1)
        ),
        size_hint=(None, None),
        size=(300, 150),
        background='message.png',
        title_color=(0.67, 0.349, 0.235, 1)
    )
    
    confirmation_popup.open()
    Clock.schedule_once(confirmation_popup.dismiss, 5)

def show_summary_popup(list_layout):
    widgets = list_layout.children
    prices = []
    for i in range(0, len(widgets) - 2, 2):
        if widgets[i].text != 'PRICE':
            price_text = widgets[i].text.replace('$', '')
            prices.append(float(price_text))

    total = sum(prices)

    popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

    total_label = Label(
        text=f"Total to pay: ${total}",
        height=30,
        color=(0, 0, 0, 1)
    )
    popup_layout.add_widget(total_label)

    popup = Popup(
        title="Food Bill",
        content=popup_layout,
        size_hint=(0.8, 0.8),
        background="background.png",
        title_color=(0.647, 0.349, 0.235, 1)
    )

    send_email_button = Button(
        text="Send Email",
        height=40,
        size_hint_y=None,
        background_color=(1, 0.5, 0, 1),
        color=(1, 1, 1, 1)
    )
    popup_layout.add_widget(send_email_button)

    close_button = Button(
        text="Close",
        height=40,
        size_hint_y=None,
        background_color=(1, 0.5, 0, 1),
        color=(1, 1, 1, 1)
    )
    popup_layout.add_widget(close_button)

    close_button.bind(on_press=popup.dismiss)
    send_email_button.bind(on_press=lambda instance: send_email(total))

    popup.open()

def remove_last_food(list_layout):
    if len(list_layout.children) > 2:
        list_layout.remove_widget(list_layout.children[0])
        list_layout.remove_widget(list_layout.children[0])

def add_food(selected_food, list_layout):
    if selected_food and selected_food in food_menu:
        food_label = Label(
            text=f"{selected_food}",
            size_hint_y=None,
            height=40,
            font_size=16,
            color=(0, 0, 0, 1)
        )

        price_label = Label(
            text=f"${food_menu[selected_food]}",
            size_hint_y=None,
            height=40,
            font_size=16,
            color=(0, 0, 0, 1)
        )

        list_layout.add_widget(food_label)
        list_layout.add_widget(price_label)

def build_gui():
    main_layout = BoxLayout(
        orientation='vertical',
        padding=[10, 200, 10, 10],
        spacing=10
    )

    with main_layout.canvas.before:
        main_layout.bg_rect = Rectangle(
            source="main.png",
            size=Window.size,
            pos=main_layout.pos
        )

    def update_bg_rect(instance, value):
        main_layout.bg_rect.size = main_layout.size
        main_layout.bg_rect.pos = main_layout.pos

    main_layout.bind(size=update_bg_rect, pos=update_bg_rect)

    spinner_layout = BoxLayout(
        orientation='horizontal',
        size_hint=(1, 0.1),
        spacing=5
    )

    food_spinner = Spinner(
        text="Select a food",
        values=list(food_menu.keys()),
        size_hint=(0.92, 1),
        color=(1, 1, 1, 1),
        font_size=16
    )

    spinner_icon = Image(
        source="arrow_down.png",
        size_hint=(0.08, 1)
    )

    spinner_layout.add_widget(food_spinner)
    spinner_layout.add_widget(spinner_icon)
    main_layout.add_widget(spinner_layout)

    with spinner_layout.canvas.before:
        Color(0.8, 0.8, 0.8, 1)
        spinner_layout.bg_rect = Rectangle(
            size=spinner_layout.size,
            pos=spinner_layout.pos
        )

    def update_spinner_bg(instance, value):
        spinner_layout.bg_rect.size = spinner_layout.size
        spinner_layout.bg_rect.pos = spinner_layout.pos

    spinner_layout.bind(size=update_spinner_bg, pos=update_spinner_bg)

    add_button = Button(
        text="Add Food",
        size_hint_y=None,
        height=70,
        font_size=16,
        background_color=(1, 0.5, 0, 1),
        color=(1, 1, 1, 1)
    )
    main_layout.add_widget(add_button)

    remove_button = Button(
        text="Remove Food",
        size_hint_y=None,
        height=70,
        font_size=16,
        background_color=(1, 0.5, 0, 1),
        color=(1, 1, 1, 1)
    )
    main_layout.add_widget(remove_button)

    show_summary_button = Button(
        text="Show Summary",
        size_hint_y=None,
        font_size=16,
        height=70,
        background_color=(1, 0.5, 0, 1),
        color=(1, 1, 1, 1)
    )
    main_layout.add_widget(show_summary_button)

    scroll_view = ScrollView(size_hint=(1, 0.5))
    food_list_layout = GridLayout(cols=2, size_hint_y=None)

    with food_list_layout.canvas.before:
        Color(0.9, 0.9, 0.9, 1)
        food_list_layout.bg_rect = Rectangle(
            size=food_list_layout.size,
            pos=food_list_layout.pos
        )

    def update_food_bg(instance, value):
        food_list_layout.bg_rect.size = food_list_layout.size
        food_list_layout.bg_rect.pos = food_list_layout.pos

    food_list_layout.bind(size=update_food_bg, pos=update_food_bg)
    food_list_layout.bind(minimum_height=food_list_layout.setter('height'))

    scroll_view.add_widget(food_list_layout)
    main_layout.add_widget(scroll_view)

    header_food = Label(
        text="FOOD",
        size_hint_y=None,
        height=40,
        color=(0, 0, 0, 1),
        bold=True,
        font_size=18
    )

    header_price = Label(
        text="PRICE",
        size_hint_y=None,
        height=40,
        color=(0, 0, 0, 1),
        bold=True,
        font_size=18
    )

    food_list_layout.add_widget(header_food)
    food_list_layout.add_widget(header_price)

    add_button.bind(on_press=lambda instance: add_food(food_spinner.text, food_list_layout))
    remove_button.bind(on_press=lambda instance: remove_last_food(food_list_layout))
    show_summary_button.bind(on_press=lambda instance: show_summary_popup(food_list_layout))

    return main_layout

class RestaurantApp(App):
    def build(self):
        return build_gui()

RestaurantApp().run()
