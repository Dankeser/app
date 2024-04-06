import customtkinter as ctk

from mytoolbox import FrameChange, RegisterCheck
from mytoolbox import add_user, hash_password

class RegisterFrame(ctk.CTkFrame, FrameChange, RegisterCheck):
    def __init__(self,master,user_data_instance:object):
        super().__init__(master)
        self.master=master
        self.user_instance = user_data_instance
        self.active_user=None
        self.popup=None
        self.grid_columnconfigure((0,1),weight=1)
        self.label=ctk.CTkLabel(self,text='Registirieren',font=ctk.CTkFont(size=20))
        self.label.grid(row=0,column=0,columnspan=2,pady=20)

        self.vorname_label=ctk.CTkLabel(self,text='Vorname:',anchor='w')
        self.vorname_label.grid(row=1,column=0,padx=10,pady=(10,0))

        self.vorname=ctk.CTkEntry(self)
        self.vorname.grid(row=2,column=0,padx=10)
        self.vorname_label.configure(width=self.vorname.cget('width'))

        self.benutzername_label=ctk.CTkLabel(self,text='Benutzername:',anchor='w')
        self.benutzername_label.grid(row=3,column=0,padx=10,pady=(10,0))

        self.benutzername=ctk.CTkEntry(self)
        self.benutzername.grid(row=4,column=0,padx=10)
        self.benutzername_label.configure(width=self.benutzername.cget('width'))

        self.passwort_label=ctk.CTkLabel(self,text='Passwort:',anchor='w')
        self.passwort_label.grid(row=5,column=0,padx=10,pady=(10,0))

        self.passwort=ctk.CTkEntry(self,show='*')
        self.passwort.grid(row=6,column=0,padx=10)
        self.passwort_label.configure(width=self.passwort.cget('width'))

        self.passwort2_label=ctk.CTkLabel(self,text='Passwort wiedergeben:',anchor='w')
        self.passwort2_label.grid(row=5,column=1,padx=10,pady=(10,0))

        self.passwort2=ctk.CTkEntry(self,show='*')
        self.passwort2.grid(row=6,column=1,padx=10)
        self.passwort2_label.configure(width=self.passwort.cget('width'))

        self.submit=ctk.CTkButton(self,text='Konto erstellen',command=self.submit_callback)
        self.submit.grid(row=7,column=0,padx=(10,0),pady=30)

        self.zurueck = ctk.CTkButton(self, text='zurückgehen', fg_color='red', hover_color='red',command=lambda: self.change_the_frame(self, self.master.loginframe),width=50)
        self.zurueck.grid(row=7, column=1, padx=10, pady=30,sticky='e')

    def submit_callback(self):
        if self.popup is not None:
            if self.popup.winfo_ismapped():
                return
            else:
                if self.register_check(self.vorname, self.benutzername, self.passwort, self.passwort2):
                    add_user(name=self.vorname.get(), username=self.benutzername.get(), hashed_password=hash_password(self.passwort.get()),instance=self.user_instance)
                    self.change_the_frame(self, self.master.loginframe)
                    #es besagt zwar, dass hier nicht erreichbar ist, aber ist es jedoch falsch.

        else:
            if self.register_check(self.vorname, self.benutzername, self.passwort, self.passwort2):
                add_user(name=self.vorname.get(),username=self.benutzername.get(), hashed_password=hash_password(self.passwort.get()),instance=self.user_instance)
                self.change_the_frame(self, self.master.loginframe)
                #hier ist erreichbar.