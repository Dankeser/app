import customtkinter as ctk
import hashlib
import hmac
from typing import NoReturn

from main_frame import MainFrame
from popup_frame import PopUpFrame
from verschlüsselung_modul import VerschlüsselModul, hash_password


def add_user(name: str, username: str, hashed_password: str, instance: object) -> NoReturn:

    new_user = {'name': name,
                'username': username,
                'password': hashed_password,
                'content': None,
                'state': 'l'}
    instance.users.append(new_user)
    instance.update(instance.users)

class FrameChange:
    def change_the_frame(self,vorherige: object,naechste: object) -> NoReturn:
        vorherige.place_forget()
        naechste.place(anchor='center',relx=0.5,rely=0.5)

    def change_to_mainframe(self,vorherige: object) -> NoReturn:
        for i in vorherige.master.winfo_children():
            i.destroy()
        # in MainKlasse neue Frame definieren.
        vorherige.master.mainframe = MainFrame(vorherige.master,user_data_instance=self.user_instance)
        vorherige.master.mainframe.place(anchor='center',relx=0.5,rely=0.5,relwidth=1.0,relheight=1.0)

class LoginCheck:
    def g(self) -> NoReturn:
        scalex = (self.popup.cget('width')/2) / self.master.winfo_width()
        scaley = (self.popup.cget('height')/2) / self.master.winfo_height()
        self.popup.place(in_=self.master,relx=0.5,rely=0.5,anchor='center')

    # login_check benutzt password_check um sicherzustellen, dass richtige Passwort eingegeben wird.
    def login_check(self,benutzername: object, passwort: object) -> bool:
        if len(benutzername.get())==0:
            self.popup = PopUpFrame(self.master, 'Bitte geben Sie ihren Benutzername.')
            self.g()
            return False
        elif len(passwort.get())==0:
            self.popup = PopUpFrame(self.master, 'Bitte geben Sie ihren Passwort.')
            self.g()
            return False
        else:
            if len(benutzername.get()) < 5 or len(benutzername.get()) > 20:
                self.popup = PopUpFrame(self.master,'Die Lange von Benutzername darf nicht kleiner als 5 und grösser als 20 sein.')
                self.g()
                return False
            elif len(passwort.get()) < 5 or len(passwort.get()) > 20:
                self.popup = PopUpFrame(self.master,'Die Lange von Passwort darf nicht kleiner als 5 und grösser als 20 sein.')
                self.g()
                return False
            elif not self.password_check(benutzername.get(),passwort.get()):
                self.popup = PopUpFrame(self.master,'Passwort passt nicht.')
                self.g()
                return False
        return True

    def password_check(self,benutzername: str,passwort: str) -> bool:
        for index, i in enumerate(self.user_instance.users):
            if i.get('username') == benutzername:
                if hash_password(passwort) == i.get('password'):
                    self.user_instance.active_user_index = index
                    self.user_instance.user_key = VerschlüsselModul.my_key_generator(passwort)
                    return True
                return


class RegisterCheck:
    def g(self) -> NoReturn:
        scalex = (self.popup.cget('width')/2) / self.master.winfo_width()
        scaley = (self.popup.cget('height')/2) / self.master.winfo_height()
        self.popup.place(in_=self.master, relx=0.5,rely=0.5,anchor='center')

    #diese Parametern sind in Form von Objekt
    def register_check(self,vorname,benutzername,passwort,passwort2) -> bool:
        if len(vorname.get())==0:
            self.popup = PopUpFrame(self.master, 'Bitte geben Sie ihren Vorname.')
            self.g()
            return False
        elif len(benutzername.get())==0:
            self.popup = PopUpFrame(self.master, 'Bitte geben Sie ihren Benutzername.')
            self.g()
            return False
        elif len(passwort.get())==0:
            self.popup = PopUpFrame(self.master, 'Bitte geben Sie ihren Passwort')
            self.g()
            return False
        elif len(passwort2.get())==0:
            self.popup = PopUpFrame(self.master, 'Bitte geben Sie ihren Passwort wieder.')
            self.g()
            return False
        else:
            if len(vorname.get()) > 20:
                self.popup = PopUpFrame(self.master, 'Die Lange von Vorname darf nicht grösser als 20 sein.')
                self.g()
                return False
            elif len(benutzername.get()) < 5 or len(benutzername.get()) > 20:
                self.popup = PopUpFrame(self.master,'Die Lange von Benutzername darf nicht kleiner als 5 und grösser als 20 sein.')
                self.g()
                return False
            elif len(passwort.get()) < 5 or len(passwort.get()) > 20:
                self.popup = PopUpFrame(self.master,'Die Lange von Passwort darf nicht kleiner als 5 und grösser als 20 sein.')
                self.g()
                return False
            elif passwort.get() != passwort2.get():
                self.popup = PopUpFrame(self.master, 'Passwörter sind nicht gleich.')
                self.g()
                return False
            elif self.is_username_used_before(benutzername):
                self.popup = PopUpFrame(self.master, 'Es gibt schon so einer Benutzer.')
                self.g()
                return False
        return True

    def is_username_used_before(self,benutzername: object) -> bool:
        for i in self.user_instance.users:
            if i.get('username') == benutzername.get():
                return True
        return False

class SwitchMode:
    def __init__(self):
        if self.active_user is not None:
            self.state = self.active_user['mode']
        else:
            self.state = 'l'
            ctk.set_appearance_mode('light')

    def switch(self) -> NoReturn:
        if self.state == 'l':
            ctk.set_appearance_mode('dark')
            if self.active_user is not None:
                self.active_user['mode'] = 'd'
            self.state = 'd'
            return

        elif self.state == 'd':
            ctk.set_appearance_mode('light')
            if self.active_user is not None:
                self.active_user['mode'] = 'l'
            self.state = 'l'
            return