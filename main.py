from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from plyer import camera
import os

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "FolCam"
            elevation: 2
            right_action_items: [["folder-open", lambda x: app.file_manager_open()]]
            md_bg_color: 1, 0.1, 0.1, 1
        
        MDLabel:
            id: path_label
            text: "Select a folder to start"
            halign: "center"
            theme_text_color: "Hint"
            font_style: "H6"

    MDFloatingActionButton:
        icon: "camera"
        md_bg_color: 1, 0.1, 0.1, 1
        pos_hint: {"center_x": .85, "center_y": .1}
        on_release: app.capture_logic()
'''

class FolCam(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.path = "/sdcard"
        self.file_manager = MDFileManager(
            exit_manager=lambda x: self.file_manager.close(), 
            select_path=self.select_path
        )
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.file_manager.show(self.path)

    def select_path(self, path):
        if os.path.isdir(path):
            self.path = path
            self.root.ids.path_label.text = f"Folder: {os.path.basename(path)}"
        self.file_manager.close()

    def capture_logic(self):
        self.temp_file = os.path.join(self.path, "temp_folcam.jpg")
        camera.take_picture(filename=self.temp_file, on_complete=self.show_filename_dialog)

    def show_filename_dialog(self, *args):
        self.dialog = MDDialog(
            title="Save Photo As:",
            type="custom",
            content_cls=MDTextField(hint_text="Enter file name (without .jpg)"),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: self.dialog.dismiss()),
                MDFlatButton(text="SAVE", on_release=self.rename_and_save)
            ],
        )
        self.dialog.open()

    def rename_and_save(self, *args):
        file_name = self.dialog.content_cls.text
        if file_name:
            final_path = os.path.join(self.path, f"{file_name}.jpg")
            os.rename(self.temp_file, final_path)
        self.dialog.dismiss()

if __name__ == "__main__":
    FolCam().run()
