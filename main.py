from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ToDoApp(App):
    def build(self):
        self.tasks = []  # Liste, um Aufgaben zu speichern

        layout = BoxLayout(orientation='vertical')

        self.task_input = TextInput(hint_text='Gib eine Aufgabe ein')
        add_button = Button(text='Hinzufügen', on_press=self.add_task)
        clear_button = Button(text='Löschen', on_press=self.clear_tasks)
        save_button = Button(text='Speichern', on_press=self.save_tasks)
        self.task_list = Label()

        layout.add_widget(self.task_input)
        layout.add_widget(add_button)
        layout.add_widget(clear_button)
        layout.add_widget(save_button)
        layout.add_widget(self.task_list)

        return layout

    def add_task(self, instance):
        task = self.task_input.text
        if task:
            self.tasks.append(task)
            self.update_task_list()

    def clear_tasks(self, instance):
        self.tasks = []
        self.update_task_list()

    def save_tasks(self, instance):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def update_task_list(self):
        task_text = "\n".join(self.tasks)
        self.task_list.text = task_text

if __name__ == '__main__':
    ToDoApp().run()
