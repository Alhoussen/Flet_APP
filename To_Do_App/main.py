from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK= 'eb06ff'

    categories_card = Row(
        scroll='auto'
    )
    categories = ['Bussines','Famille','Friends']
    for category in categories:
        categories_card.controls.append(
            Container(
                bgcolor=BG, height=110,width=170,
                border_radius=20,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=2),
                            content=
                            Container(
                                bgcolor=PINK,

                            )

                        )
                    ]
                )  
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),  
                Text(
                    value="Comment va tu, Fatoumata ?"
                ),
                Text(value='CATEGORIES'),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                )
            ]     
        )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                height=850,
                width=400,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )
    container = Container(
        width=500,
        height=800,
        bgcolor=BG,
        border_radius=35,,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    page.add(container)

app(target=main)





























# 
# import flet as ft

# class Task(ft.Column):
#     def __init__(self, task_name, task_delete):
#         super().__init__()
#         self.task_name = task_name
#         self.task_delete = task_delete
#         self.display_task = ft.Checkbox(value=False, label=self.task_name)
#         self.edit_name = ft.TextField(expand=1)

#         self.display_view = ft.Row(
#             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,
#             controls=[
#                 self.display_task,
#                 ft.Row(
#                     spacing=0,
#                     controls=[
#                         ft.IconButton(
#                             icon=ft.icons.CABIN_OUTLINED,
#                             tooltip="Modifier la liste",
#                             on_click=self.edit_clicked,
#                         ),
#                         ft.IconButton(
#                             ft.icons.DELETE_OUTLINED,
#                             tooltip="Supprimer",
#                             on_click=self.delete_clicked,
#                         ),
#                     ],
#                 ),
#             ],
#         )

#         self.edit_view = ft.Row(
#             visible=False,
#             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,
#             controls=[
#                 self.edit_name,
#                 ft.IconButton(
#                     icon=ft.icons.DONE_OUTLINE_OUTLINED,
#                     icon_color=ft.colors.GREEN,
#                     tooltip="Update To-Do",
#                     on_click=self.save_clicked,
#                 ),
#             ],
#         )

#         self.controls = [self.display_view, self.edit_view]
#     def edit_clicked(self, e):
#         self.edit_name.value = self.display_task.label
#         self.display_view.visible = False
#         self.edit_view.visible = True
#         self.update()

#     def save_clicked(self, e):
#         self.display_task.label = self.edit_name.value
#         self.display_view.visible = True
#         self.edit_view.visible = False
#         self.update()

#     def delete_clicked(self, e):
#         self.task_delete(self)


# class TodoApp(ft.Column):
#     # application's root control is a Column containing all other controls
#     def __init__(self):
#         super().__init__()
#         self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
#         self.tasks = ft.Column()
#         self.width = 600
#         self.controls = [
#             ft.Row(
#                 controls=[
#                     self.new_task,
#                     ft.FloatingActionButton(
#                         icon=ft.icons.ADD, on_click=self.add_clicked
#                     ),
#                 ],
#             ),
#             self.tasks,
#         ]

#     def add_clicked(self, e):
#         task = Task(self.new_task.value, self.task_delete)
#         self.tasks.controls.append(task)
#         self.new_task.value = ""
#         self.update()

#     def task_delete(self, task):
#         self.tasks.controls.remove(task)
#         self.update()

# def main(page: ft.Page):
#     page.adaptive = True
#     page.title = "To-Do App"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.update()

#     # create application instance
#     todo = TodoApp()
#     todo2 = TodoApp()

#     # add application's root control to the page
#     page.add(todo, todo2)

# ft.app(main)