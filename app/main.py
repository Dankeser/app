import customtkinter as ctk
from login_frame import LoginFrame
from register_frame import RegisterFrame
from main_frame import MainFrame
from user_data_manager import UserDataLoader
from mytoolbox import SwitchMode
from property_class import PropertyMixin

class MainKlasse(ctk.CTk, SwitchMode, PropertyMixin):
    def __init__(self,user_data_instance):
        super().__init__()
        self.users_instance = user_data_instance
        self.title('Login Screen')
        self.minsize(width=1000,height=700)

        self.loginframe = LoginFrame(self,self.users_instance)
        self.loginframe.place(anchor='center',relx=0.5,rely=0.5)

        self.registerframe = RegisterFrame(self,self.users_instance)



ctk.set_widget_scaling(1.25)
ctk.set_window_scaling(1.25)
ctk.DrawEngine.preferred_drawing_method='polygon_shapes'
myinstance=UserDataLoader()
myapp=MainKlasse(user_data_instance=myinstance)
myapp.protocol("WM_DELETE_WINDOW", lambda: myapp.quit())
myapp.mainloop()