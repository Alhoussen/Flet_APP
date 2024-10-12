import flet as ft
import time

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text
        self.on_click = on_click

def main(page: ft.Page):

    def ok_clicked(e):
        print("OK clicked")

    def cancel_clicked(e):
        print("Cancel clicked")

    page.add(
        MyButton(text="OK", on_click=ok_clicked), 
        MyButton(text="Cancel", on_click=cancel_clicked),
        )

ft.app(main)

























# def main(page: ft.Page):
#     # def btn_click(e):
#     #     if not txt_name.value:
#     #         txt_name.error_txt = "Please enter your name"
#     #         page.update
#     #     else:
#     #         name = txt_name.value
#     #         page.clean()
#     #         page.add(ft.Text(f"Hello, {name}!"))

#     # txt_name = ft.TextField(label="Your name")
#     # page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))
#     def button_clicked(e):
#         output_text.value = f"Dropdown value is:  {color_dropdown.value}"
#         page.update()

#     output_text = ft.Text()
#     submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
#     color_dropdown = ft.Dropdown(
#         width=100,
#         options=[
#             ft.dropdown.Option("Red"),
#             ft.dropdown.Option("Green"),
#             ft.dropdown.Option("Blue"),
#         ],
#     )
#     page.add(color_dropdown, submit_btn, output_text)



# ft.app(main)
