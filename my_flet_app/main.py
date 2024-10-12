import flet as ft
import time


def main(page: ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_txt = "Please enter your name"
            page.update
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")
    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))



ft.app(main)
