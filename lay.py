import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.image import Image

import sqlite3
from kivy.uix.popup import Popup
import re

from kivy.uix.screenmanager import ScreenManager,Screen

Builder.load_string("""

<ScreenTwo>:
    name: "start"
    canvas.before:
        Rectangle:
            pos: self.pos
            source:'bv.jpg'
            size: self.size
    GridLayout:
        rows:2
        BoxLayout:
            size_hint_y:None
            height:100
            spacing:5
            padding:5
            
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    pos:self.pos
                    size:self.size
                    source:"y.jpg"

            

                    
           


    BoxLayout:
        id:login_layout
        orientation:"vertical"
        size_hint:0.9,0.6
        padding:root.width*.02,root.height*.02
        spacing:min(root.width,root.height)*.02
        
        pos_hint:{"center_x":0.5,"center_y":0.5}
        canvas:
            
            Rectangle:
                size:self.size
                
                pos:self.pos
                
        Image:
            source:'ua.png'
            pos_hint: {'left':1, 'top':1}
            size:self.size


        BoxLayout:
            orientation:"horizontal"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            Button:
                text:"SIGN IN"
                background_color: (255,255,255,1)
                color: 0, 0, 0, 1
                halign: 'left'
                valign:'center'
               

            Button:
                text:"SIGN UP"
                background_color: (255,255,255,1)
                color: 0, 0, 0, 1
                
                on_press:
                    root.manager.transition.direction="left"
                    root.manager.transition.duration=0
                    root.manager.current="ScreenThree"
                        
                
                
                
        
            
        BoxLayout:
            orientation:"vertical"
            
                
            TextInput:
                pos_hint:{"center_x":0.5,"center_y":0.5}
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                hint_text:"User Name"
                background_color: 0,0,0,0  
                
                size_hint:(0.7,0.3)
                
                id:username
                multiline:False
                
                

        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            
                
            TextInput:
                pos_hint:{"center_x":0.5,"center_y":0.5}
                hint_text:"Password"
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                
                background_color: 0,0,0,0  
                
                size_hint:(0.7,0.3)
                id:password
                
                
                multiline:False
                password:True
                
                
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            padding:3,3
            Button:
                text:"LOGIN "
                pos_hint:{"center_x":0.5,"center_y":0.5}
                background_color: .2, .1, .73, 1
                padding:5,5
                size_hint:(0.7,0.3)
                on_press:root.do_login(username.text,password.text)
                
            
            Button:
                pos_hint:{"center_x":0.5,"center_y":0.5}
                text:"Forgot Password?"
                padding:5,5
                color:0,0,0,1
                background_color: (255,255,255,1)
                on_press:
                    root.manager.transition.direction="left"
                    root.manager.transition.duration=0
                    root.manager.current="ScreenOne"
##############################################################################################################

<ScreenOne>:
    canvas.before:
        Rectangle:
            pos: self.pos
            source:'bv.jpg'
            size: self.size

    GridLayout:
        rows:2
        
        BoxLayout:
            size_hint_y:None
            height:100
            spacing:20
            padding:10
            pos_hint:{"center_x":0.5,"center_y":0.5}
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    pos:self.pos
                    size:self.size
                    source:"y.jpg"
            Button:
                
                background_normal:"axc.jpg"
                size_hint_x:None
                
                width:150
                text:"[b]BACK[/b]"
                markup:True
                on_press:
                    root.manager.transition.direction="left"
                    root.manager.transition.duration=0
                    root.manager.current="ScreenTwo"
                    
    BoxLayout:
        id:login_layout
        orientation:"vertical"
        size_hint:0.9,0.6
        padding:root.width*.02,root.height*.02
        spacing:min(root.width,root.height)*.02
        
        pos_hint:{"center_x":0.5,"center_y":0.5}
        canvas:
            
            Rectangle:
                size:self.size
                
                pos:self.pos
                
        Image:
            source:'locc.jpg'
            pos_hint:{"center_x":0.5,"center_y":0.5}
            size_hint:(0.5,0.5)
        
        Label:
            text:"     Forgot your Password?\\nEnter your registered Email id\\n   to reset your password"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            color:0,0,0,1
            size_hint:(0.3,0.2)
        
        TextInput:
            id:reemail
            hint_text:"Email id"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            canvas.before:
                Line:
                    points: self.x + 20, self.y, self.x + self.width - 20, self.y
                    width: 1
                
            background_color: 0,0,0,0  
            multiline:False
            size_hint:(0.6,0.15)
        TextInput:
            id:pas
            hint_text:"Password"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            canvas.before:
                Line:
                    points: self.x + 20, self.y, self.x + self.width - 20, self.y
                    width: 1
            password:True    
            background_color: 0,0,0,0  
            multiline:False
            size_hint:(0.6,0.15)

        TextInput:
            id:repas
            hint_text:"Re-enter the same Password"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            canvas.before:
                Line:
                    points: self.x + 20, self.y, self.x + self.width - 20, self.y
                    width: 1
            password:True     
            background_color: 0,0,0,0  
            multiline:False
            size_hint:(0.6,0.15)
        Button:
            text:"RESET PASSWORD"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            background_color: .2, .1, .73, 1
            size_hint:(0.6,0.1)
            on_press:
                root.do_reset(reemail.text,pas.text,repas.text)
                

##############################################################################################################


<ScreenThree>:
    canvas.before:
        Rectangle:
            pos: self.pos
            source:'bv.jpg'
            size: self.size

    GridLayout:
        rows:2
        
        BoxLayout:
            size_hint_y:None
            height:100
            spacing:10
            padding:10
            pos_hint:{"center_x":0.5,"center_y":0.5}
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    pos:self.pos
                    size:self.size
                    source:"y.jpg"
                    
            Button:
                
                background_normal:"axc.jpg"
                size_hint_x:None
                width:150
                text:"[b]BACK[/b]"
                markup:True
                
                on_press:
                    root.manager.transition.direction="left"
                    root.manager.transition.duration=0
                    root.manager.current="ScreenTwo"
    BoxLayout:
        orientation:'vertical'
        padding:root.width*.02,root.height*.02
        
        
        
        size_hint:0.9,0.7
        pos_hint:{"center_x":0.5,"center_y":0.5}
        canvas:
            Rectangle:
                size:self.size
                pos:self.pos
                
         
                
            
                
                
                
        Label:
            text:"[b][u][size=80]Sign Up Form[/size][/u][/b]"
            size_hint:1,None
            color: (138,43,226)
            markup:'True'

        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            
            TextInput:
                pos_hint:{"center_x":0.5,"center_y":0.5}
                hint_text:"First Name"
                color:0,0,0,1
                background_color: 0,0,0,0 
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                id:fname
                size_hint:(0.7,0.3)
                multiline:False
                
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            
            TextInput:
                hint_text:"Last Name"
                text_size:self.size
                id:lname
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                background_color: 0,0,0,0 
                pos_hint:{"center_x":0.5,"center_y":0.5}
                size_hint:(0.7,0.3)
                multiline:False
                
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            
            TextInput:
                hint_text:"xyz@gmail.com"
                text_size:self.size
                id:emailid
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                background_color: 0,0,0,0 
                pos_hint:{"center_x":0.5,"center_y":0.5}
                size_hint:(0.7,0.3)
                multiline:False

        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            TextInput:
                hint_text:"Phone No"
                text_size:self.size
                id:mobileno
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                background_color: 0,0,0,0 
                pos_hint:{"center_x":0.5,"center_y":0.5}
                size_hint:(0.7,0.3)
                multiline:False

        

        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            
            TextInput:
                hint_text:"password"
                text_size:self.size
                id:passwd
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                background_color: 0,0,0,0 
                pos_hint:{"center_x":0.5,"center_y":0.5}
                size_hint:(0.7,0.3)
                multiline:False
                password:True
                
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            
            TextInput:
                hint_text:"confirm password"
                background_color: 0,0,0,0 
                canvas.before:
    
                    Line:
                        points: self.x + 20, self.y, self.x + self.width - 20, self.y
                        width: 1
                password:True
                size_hint:(0.7,0.3)
                pos_hint:{"center_x":0.5,"center_y":0.5}
                
                id:cpass
                multiline:False
                
        BoxLayout:
            orientation:'horizontal'
            padding:5,5
            spacing:10,10
            size_hint:(0.7,0.5)
            pos_hint:{"center_x":0.5,"center_y":0.5}
            
            Button:
                id:btn
                icon:'face'
                text:"SIGNUP"
                pos_hint:{"center_x":0.5,"center_y":0.5}
                background_color: .2, .1, .73, 1
                padding:5,5
                size_hint:(0.7,1)
                on_press:
                    root.do_register(fname.text,lname.text,emailid.text,mobileno.text,passwd.text,cpass.text)
                    
            
            """)
class ScreenOne(Screen,BoxLayout):
    def do_reset(self,reemailtext,pastext,repastext):
        reemail=reemailtext
        paste=pastext
        print(paste)
        conn=sqlite3.connect("mybase.db")
        cu=conn.cursor()
        
        find=("SELECT * FROM register WHERE emid=? ")
        print(find)
        cu.execute(find,[(reemail)])
        results=cu.fetchall()
        if (len(reemail)>0):
            
            
            if results:
                cu.execute('UPDATE register SET passwd=? WHERE emid = ?', (paste,reemail))
                conn.commit()
                for i in results:
                    
                    self.manager.transition.direction="left"
                    self.manager.transition.duration=0
                    self.manager.current="ScreenTwo"
            else:
                popup=Popup(title="login portal",content=Label(text="please enter registered email id"),size_hint=(0.8,0.3))
                popup.open()
        else:
            popup=Popup(title="login portal",content=Label(text="please enter Email id"),size_hint=(0.8,0.3))
            popup.open()
        conn.close()
        self.ids['reemail'].text = ""
        self.ids['pas'].text = ""
        self.ids['repas'].text = ""
        
            
        
                        





########################################################################################################################################

class ScreenTwo(Screen,GridLayout):
    def do_login(self,usernametext,passwordtext):
        useri=usernametext
        passwd=passwordtext
        conn=sqlite3.connect("mybase.db")
        cur=conn.cursor()
        
        cur.execute("CREATE TABLE  IF NOT EXISTS login(userid VARCHAR(40),passwrd VARCHAR(40))")
        cur.execute("INSERT INTO login(userid,passwrd) VALUES(?,?)",(useri,passwd))
        cur.execute("SELECT * FROM register")
        print(cur.fetchall())
        if(len(useri)>0 and len(passwd)>0):
            
        
            find=("SELECT * FROM register WHERE emid=? AND passwd=?")
            cur.execute(find,[(useri),(passwd)])
            results=cur.fetchall()
            if results:
                for i in results:
                    popup=Popup(title="login portal",content=Label(text="welcome "+i[0]+" " +i[1]),size_hint=(0.6,0.3))
                    popup.open()

            else:
                popup=Popup(title="login portal",content=Label(text="please enter correct userid and password"),size_hint=(0.8,0.3))
                popup.open()

        else:
            popup=Popup(title="login portal",content=Label(text="please enter userid and password"),size_hint=(0.8,0.3))
            popup.open()
            
            
                
            
        print("table created successfully")
        conn.close()
        
        self.ids['username'].text = ""
        self.ids['password'].text = ""

        
#############################################################################################################################################
class ScreenThree(Screen,BoxLayout):
    
        
        
        
    def do_register(self,firsttext,lasttext,emailtext,mobiletext,passwordtext,copasstext):
        fname=firsttext
        lname=lasttext
        email=emailtext
        mobileno=mobiletext
        password=passwordtext
        conpass=copasstext
        conn=sqlite3.connect("mybase.db")
        cu=conn.cursor()
        
        cu.execute("CREATE TABLE IF NOT EXISTS register(name VARCHAR(30),lastname VARCHAR(30),emid VARCHAR(40),phoneno NUMERIC,passwd VARCHAR(30),cpasswd VARCHAR(30))")
        find=("SELECT * FROM register WHERE emid=?")
        cu.execute(find,[(email)])
        
            
        if(len(fname)>0 and len(lname)>0 and len(email)>0 and len(mobileno)>0 and len(password)>0 and len(conpass)>0):
            if cu.fetchall():
                popup=Popup(title="ERROR", content=Label(text="user already registered"),size_hint=(0.6,0.3))
                popup.open()
                self.manager.transition.direction="right"
                self.manager.transition.duration=0
                self.manager.current="ScreenTwo"
            else:
            
            
                
                print(cu.fetchall())
                
                if not re.match("^[A-Za-z]*$", fname):
                    popup=Popup(title="REGISTRATION PORTAL", content=Label(text="enter valied first name"),size_hint=(0.6,0.3))
                    popup.open()
                elif not re.match("^[A-Za-z]*$", lname):
                        popup=Popup(title="REGISTRATION PORTAL", content=Label(text="enter valied last name"),size_hint=(0.6,0.3))
                        popup.open()

                    
                elif not re.match("^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]", email):
                        popup=Popup(title="REGISTRATION PORTAL", content=Label(text="enter valied emailid"),size_hint=(0.6,0.3))
                        popup.open()
                    
                elif not re.match("^[0-9]*$", mobileno):
                        popup=Popup(title="REGISTRATION PORTAL", content=Label(text="enter valied mobile no"),size_hint=(0.6,0.3))
                        popup.open()
                    
                elif not re.match("^[A-Za-z0-9]*$", password):
                        popup=Popup(title="REGISTRATION PORTAL", content=Label(text="enter valied password"),size_hint=(0.6,0.3))
                        popup.open()
                
                    
                    
                    
                elif not re.match("^[A-Za-z0-9]*$", password):
                        popup=Popup(title="REGISTRATION PORTAL", content=Label(text="enter valied confirm  password"),size_hint=(0.6,0.3))
                        popup.open()
                    
                elif (password==conpass):
                        cu.execute("INSERT INTO register(name,lastname,emid,phoneno,passwd,cpasswd) VALUES(?,?,?,?,?,?)",(fname,lname,email,mobileno,password,conpass))
                        cu.execute("SELECT * FROM register")
                        conn.commit()
                        print("regis")
                        popup=Popup(title="REGISTRATION PORTAL", content=Label(text="Registration completed\nkindly login now"),size_hint=(0.6,0.3))
                        popup.open()
                        self.manager.transition.direction="right"
                        self.manager.transition.duration=0
                        self.manager.current="ScreenTwo"
                   
                else:
                    popup=Popup(title="ERROR", content=Label(text="please enter same password"),size_hint=(0.6,0.3))
                    popup.open()
                            
                
            

            
        else:
            popup=Popup(title="ERROR", content=Label(text="please enter your details"),size_hint=(0.6,0.3))
            popup.open()
            print("fields")
        conn.close()
        self.ids['fname'].text = ""
        self.ids['lname'].text = ""
        self.ids['emailid'].text = ""
        self.ids['mobileno'].text = ""
        self.ids['passwd'].text = ""
        self.ids['cpass'].text = ""


####################################################################################################################################


    
                    

        
        
            
        

    
screen_manager=ScreenManager()

screen_manager.add_widget(ScreenTwo(name="ScreenTwo"))
screen_manager.add_widget(ScreenThree(name="ScreenThree"))
screen_manager.add_widget(ScreenOne(name="ScreenOne"))



class MyApp(App):
    
    title="LOGIN PORTAL"
    icon="cords.jpg"
   


    def build(self):
        return screen_manager
     

    
        

if __name__ == '__main__':
    MyApp().run()
