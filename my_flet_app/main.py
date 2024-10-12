import flet as ft
import time
import asyncio

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text
        self.on_click = on_click


class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1

def main(page: ft.Page):
    page.add(Countdown(120), Countdown(60))

ft.app(main)











# class Task(ft.Row):
#     def __init__(self, text):
#         super().__init__()
#         self.text_view = ft.Text(text)
#         self.text_edit = ft.TextField(text, visible=False)
#         self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
#         self.save_button = ft.IconButton(
#             visible=False, icon=ft.icons.SAVE, on_click=self.save
#         )
#         self.controls = [
#             ft.Checkbox(),
#             self.text_view,
#             self.text_edit,
#             self.edit_button,
#             self.save_button,
#         ]

#     def edit(self, e):
#         self.edit_button.visible = False
#         self.save_button.visible = True
#         self.text_view.visible = False
#         self.text_edit.visible = True
#         self.update()

#     def save(self, e):
#         self.edit_button.visible = True
#         self.save_button.visible = False
#         self.text_view.visible = True
#         self.text_edit.visible = False
#         self.text_view.value = self.text_edit.value
#         self.update()

# def main(page):

#     page.adaptive = True

#     page.appbar = ft.AppBar(
#         leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),
#         title=ft.Text("Adaptive AppBar"),
#         actions=[
#             ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))
#         ],
#         bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
#     )

#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationBarDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Bookmark",
#             ),
#         ],
#         border=ft.Border(
#             top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
#         ),
#     )

#     page.add(
#         ft.SafeArea(
#             ft.Column(
#                 [
#                     ft.Checkbox(value=False, label="Dark Mode"),
#                     ft.Text("First field:"),
#                     ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
#                     ft.Text("Second field:"),
#                     ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
#                     ft.Switch(label="A switch"),
#                     ft.FilledButton(content=ft.Text("Adaptive button")),
#                     ft.Text("Text line 1"),
#                     ft.Text("Text line 2"),
#                     ft.Text("Text line 4"),
#                     # MyButton(text="OK"),
#                 ]
#             )
#         )
#     )


# ft.app(main)


























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
