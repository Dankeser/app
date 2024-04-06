import customtkinter as ctk

class PopUpFrame(ctk.CTkFrame):
    def __init__(self,master,satz:str):
        super().__init__(master,fg_color=('gray55','gray55'),corner_radius=0)

        self.exit=ctk.CTkButton(self,text='x',width=20,command=self.exit_callback,corner_radius=0,fg_color='red',hover='red',)
        self.exit.grid(row=0,column=0,sticky='e',pady=2,padx=2)

        self.text=ctk.CTkLabel(self,text=satz,wraplength=400,text_color="gray90")
        self.text.grid(row=1,column=0,padx=10,pady=10)

    def exit_callback(self):
        self.place_forget()
