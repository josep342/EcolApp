import sqlite3
import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color,Rectangle
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout 
from kivy.lang import Builder
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.metrics import *
from kivy.graphics import *

from datetime import datetime
import requests
import math
import geocoder
import folium

from kivymd.uix.textfield import MDTextField
import random
import webbrowser
import os
import geopy

#Window.clearcolor="white"

KV='''

FloatLayout:

    size_hint: 1, 1
    #pos_hint: {'center_x': 0.0,'center_y': 0.0}
    MDTopAppBar:
        title: "GeoIp"
        pos_hint: {'center_x': 0.5,'y': 0.89}
        size_hint:1,.11
        left_action_items: [["menu", lambda x: app.seplier(self)]]
        right_action_items: [["dots-vertical", lambda x: app.affmenu(self)]]

    


'''


class AccueilApp(MDApp):

    def build(self):

        global b1,b2,b3,b4,b5,btaction,cadregauche,latitre,cadre,etat,idtheme,nomtheme,typetheme,datervdtheme,nomconcerne,tel,typelab,labrdv,jourr,ann,moiss
        global adressresp,labgps,altitude,longitude,benregistrer,combrecherche,lbdate,iddtheme,idthemeloc,combrechercheloc,typelabloc,typethemeloc
        global altloc,longloc,btnimagetemp,nbrheur,distance,btnimgetat,labtemp,altactuell,longactuell,btngpsloc,modulcatioloc,amplitudeloc,precisionloc
        global vitessloc,btntracerloc,bsetting,latitretrafic,imgtete,tabtrafic,libreexport,combodattrafic,labdatetrafic,combtypetrafic,labtypetrafic
        global trechresptrafic,comboresptrafic,bexportrafic,bmenu1,bmenu2,bmenu1rien,bmenu2rien,t1trafic,t2trafic,t3rechtrafic,comborechupdatetheme
        global btnsetting,btnsetteingdelelte,iddst,codepays,labtypetransport,moyentransport,distanceheure,titinfoperso
        global btnsavpersoninfo,iminfoperson,distheure
        global ic1,ic2,ic3,ic4,ic5
        global bsettingretour,etatsetting,trien1,trien2

        etatsetting="1"

        etat = 0
        iddtheme=0
        iddst=0
        distheure=0

        altactuell=0.0
        longactuell=0.0

        libreexport=False

        apii="f46395584b3818ad2ae1e65ed8b800f3"
        
        # definition de la taille de l ecran
        #wid=36
        #heigh=90

        #screenwidth, screenheight=Window.size
        #new_width=int(screenwidth*(wid/100))
        #new_height=int(screenheight*(heigh/100))
        #Window.size=(new_width,new_height)

        gg=geocoder.ip('me')

        codepays=gg.country

        

        #tete=Rectangle(pos=(100,100),size=(200,100))

        self.theme_cls.primary_palette = "Orange"
        #self.theme_cls.theme_style = "Dark"


        cadre=Builder.load_string('''
        
RelativeLayout:
    pos_hint: {'x': 0,'y': 0.0}
    size_hint:1,1
                                  
    canvas:
        Color:
            rgb:192/255,192/255,192/255
        Rectangle:
            pos:self.pos
            size:self.size
                                  
    
        
''')
       
        cadregauche=Builder.load_string('''


FloatLayout:
    pos_hint: {'x': 0,'y': 0.27}
    size_hint:0,0

    canvas:
        Color:
            rgb:192/255,192/255,192/255
        Rectangle:
            pos:self.pos
            size:self.size
                                        
         
        ''')
        
        global img1, img2,img3, img4,imgg


        imgtete=Image(source="photot.jpg", size_hint=(0,0), pos_hint={'x':0,'y':0})

        img1=Image(source="house-icon_34406.png", size_hint=(0,0), pos_hint={'x':0.02,'y':0.82})
        img2=Image(source="wifi_wireless_internet_location_pointer_icon_124599.ico", size_hint=(0,0), pos_hint={'x':0.02,'y':0.72})
        img3=Image(source="calendar-5983133_960_720.png", size_hint=(0,0), pos_hint={'x':0.02,'y':0.62})
        img4=Image(source="adminn.png", size_hint=(0,0), pos_hint={'x':0.02,'y':0.52})

        imgg=Image(source="storage.ico", size_hint=(0,0), pos_hint={'center_x':0.5,'y':0})

        ic1=Builder.load_string('''
MDIcon:
    icon:"bed-single"
    pos_hint:{'x':.05,'y':0.86} 
    size_hint:0.07,0.1 
    theme_text_color:'Custom'
    text_color:'orange'  
                                
''')       
        
        b1=Builder.load_string('''
Button:
    size_hint:0,0.1
    pos_hint:{'x':.2,'y':0.85}
    color:'black'
    background_color:[0,0,0,0]
    border:(0,0,0,0)
    font_size:"22"
    markup:True
                            
    canvas.before:
        Color:
            rgb:192/255,192/255,192/255
        Rectangle:
            pos:self.pos
            size:self.size
        
''')
        b1.bind(on_release=self.accueil)

        ic2=Builder.load_string('''
MDIcon:
    icon:"bed-single"
    pos_hint:{'x':.05,'y':0.71} 
    size_hint:0.07,0.1 
    theme_text_color:'Custom'
    text_color:'orange'  
                                
''')

        b2=Builder.load_string('''

Button:
    size_hint:0,0.1
    pos_hint:{'x':.2,'y':0.7}
    color:'black'
    background_color:[0,0,0,0]
    font_size:"22"
    markup:True  
                               
    canvas.before:
        Color:
            rgb:192/255,192/255,192/255
        Rectangle:
            pos:self.pos
            size:self.size

''')
        b2.bind(on_release=self.ajout)

        ic3=Builder.load_string('''
MDIcon:
    icon:"bed-single"
    pos_hint:{'x':.05,'y':0.56} 
    size_hint:0.07,0.1 
    theme_text_color:'Custom'
    text_color:'orange'  
                                
''')
        b3=Builder.load_string('''
Button:
    size_hint:0,0.1
    pos_hint:{'x':.2,'y':0.55}
    color:'black'
    background_color:[0,0,0,0]
    font_size:"22"
    markup:True
                               
    canvas.before:
        Color:
            rgb:192/255,192/255,192/255
        Rectangle:
            pos:self.pos
            size:self.size
            

''')
        b3.bind(on_release=self.modificationtheme)

        ic4=Builder.load_string('''
MDIcon:
    icon:"bed-single"
    pos_hint:{'x':.05,'y':0.41} 
    size_hint:0.07,0.1 
    theme_text_color:'Custom'
    text_color:'orange'  
                                
''')
        b4=Builder.load_string('''
Button:
    size_hint:0,0.1
    pos_hint:{'x':.2,'y':0.4}
    color:'black'
    background_color:[0,0,0,0]
    font_size:"22"
    markup:True
                               
    canvas.before:
        Color:
            rgb:192/255,192/255,192/255
        Rectangle:
            pos:self.pos
            size:self.size
                               
''')
        b4.bind(on_release=self.localisation)

        ic5=Builder.load_string('''
MDIcon:
    icon:"bed-single"
    pos_hint:{'x':.05,'y':0.26} 
    size_hint:0.07,0.1 
    theme_text_color:'Custom'
    text_color:'orange'  
                                
''')
        
        b5=Builder.load_string('''
Button:
    size_hint:(0,0.1)
    pos_hint:{'x':.2,'y':0.25}
    color:'black'
    background_color:[0,0,0,0]
    font_size:"22"
    markup:True
                               
    canvas.before:
        Color:
            rgb:192/255,192/255,192/255
        Rectangle:
            pos:self.pos
            size:self.size

''')
        b5.bind(on_release=self.trafic)
       
        #btaction=Button(background_normal='menu.jpg' , size_hint=(0,0),pos_hint={'x':0,'y':0})
        #btaction.bind(on_press=self.seplier)

        # les outils de la page d'acceueil

        latitre=Label(text="[b]ACCUEIL[/b]",markup=True,size_hint=(0.5,0.08),font_size='20sp', pos_hint={'center_x':0.5,'y':0.8}, color="black")
       
        lb=Label(text="askyas_dev.v 01", pos_hint={'center_x':0.5,'y':0},size_hint=(0.2,0.1), color='black', font_size='10sp')

        bsetting=Builder.load_string('''
MDIconButton:
    icon:"youtube-studio"
    pos_hint:{'x':0.87,'y':0.8}
    size_hint:0.1,0.1 
    theme_text_color:'Custom'
    text_color:'black' 

''')
        
        bsetting.bind(on_press=self.settingparameters)

        bsettingretour=Builder.load_string('''
MDIconButton:
    icon:"arrow-left-circle"
    pos_hint:{'x':0.05,'y':0.8}
    size_hint:0.1,0.1 
    theme_text_color:'Custom'
    text_color:'black' 

''')
         
        bsettingretour.bind(on_release=self.retoursetting)

        # les outils de la page ajout et modificaiton

        trien1 = MDTextField(hint_text="Code BNB",password=True,disabled=True,font_size='17sp',line_color_normal='black', pos_hint={'x':0.05, 'y':0.7},size_hint=(0.4,0.1))
        trien2 = MDTextField(hint_text="1.2 Ghz",font_size='16sp', disabled=True,line_color_normal='black', pos_hint={'x':0.55, 'y':0.7},size_hint=(0.4,0.1))

        idtheme = MDTextField(hint_text="ID_Theme",password=True,disabled=True,font_size='17sp',line_color_normal='black', pos_hint={'x':0.05, 'y':0.62},size_hint=(0.4,0.1))
        nomtheme = MDTextField(hint_text="Libellé",font_size='16sp',line_color_normal='black', pos_hint={'x':0.55, 'y':0.62},size_hint=(0.4,0.1))


        combrecherche=Builder.load_string(

        """
Spinner:
    text:"Choisir"
    pos_hint:{'x':0.05, 'y':0.58}
    size_hint:(0.3,0.04)
    background_color:[0,0,0,0]
    color:"white"

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
        """)

        combrecherche.bind(on_release=self.rechidtheme)
        combrecherche.bind(text=self.affchois)

        typelab=Label(text="[b]Type[/b]",markup=True,size_hint=(0.2,0.08), pos_hint={'x':0.37,'y':0.56}, color="black")
       
        typetheme=Builder.load_string(

        """
Spinner:
    text:"Chosir"
    pos_hint:{'x':0.55, 'y':0.58}
    size_hint:(0.4,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]

        """)
        #typetheme.bind(text=self.affchois)
        typetheme.bind(on_release=self.chargetheme)
        typetheme.bind(text=self.affidtheme)

        labrdv=Label(text="[b]Rendez-vous[/b]",markup=True,size_hint=(0.3,0.15), pos_hint={'x':0.05,'y':0.48}, color="black")

        ann=Builder.load_string(
            """
Spinner:
    text:"AAAA"
    pos_hint:{'x':0.05, 'y':0.46}
    size_hint:(0.3,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
""")
        
        ann.bind(on_release=self.charganne)

        moiss=Builder.load_string(

        """
Spinner:
    text:"MM"
    pos_hint:{'x':0.42, 'y':0.46}
    size_hint:(0.2,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
        """)
        moiss.bind(on_release=self.chargemois)
        
        jourr=Builder.load_string(
        """
Spinner:
    text:"JJ"
    pos_hint:{'x':0.7, 'y':0.46}
    size_hint:(0.25,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]

        """)
        
        jourr.bind(on_release=self.chargejour)
        #datervdtheme

        nomconcerne = MDTextField(hint_text="Resp concerné",font_size='16sp',line_color_normal='black', pos_hint={'x':0.05, 'y':0.34},size_hint=(0.4,0.1))
        tel = MDTextField(hint_text="Téléphone",font_size='16sp',line_color_normal='black', pos_hint={'x':0.55, 'y':0.34},size_hint=(0.4,0.1))
        adressresp = MDTextField(hint_text="Son adresse Résidentielle",font_size='16sp',line_color_normal='black', pos_hint={'x':0.05, 'y':0.25},size_hint=(0.9,0.1))
        
        labgps=Label(text="[b]GPS[/b]",markup=True,size_hint=(0.2,0.15), pos_hint={'center_x':0.5,'y':0.18}, color="black",font_size='10sp')
        altitude = MDTextField(hint_text="Lattitude",disabled=True,font_size='16sp',line_color_normal='black', pos_hint={'x':0.05, 'y':0.15},size_hint=(0.4,0.1))
        longitude = MDTextField(hint_text="Longitude",disabled=True,font_size='16sp',line_color_normal='black', pos_hint={'x':0.55, 'y':0.15},size_hint=(0.4,0.1))
        
        lbdate=Label(size_hint=(0.35,0.15), pos_hint={'x':0.1,'y':0.03}, color="black",font_size='14sp')
        
        benregistrer=Builder.load_string(
        """ 
Button:
    text:"[b]Suivant[/b]"
    markup:True
    pos_hint:{'x':0.55, 'y':0.08}
    size_hint:(0.4,0.05)
    color:'white'
    background_color:[0,0,0,0]

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
            
        """)
        
        benregistrer.bind(on_release=self.numerisergps)

        
        # les outils de la page de localisation 

        idthemeloc = MDTextField(hint_text="Theme",font_size='17sp',line_color_normal='black', pos_hint={'x':0.05, 'y':0.62},size_hint=(0.4,0.1))
        combrechercheloc=Builder.load_string(
        """
Spinner:
    text:"Choisir"
    pos_hint:{'x':0.55, 'y':0.64}
    size_hint:(0.4,0.04)
    background_color:[0,0,0,0]
    color:"white"

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
        """)
        
        
        combrechercheloc.bind(on_release=self.recidtheloc)
        combrechercheloc.bind(text=self.affinfoloc)

        typelabloc=Label(text="[b]Type[/b]",markup=True,size_hint=(0.2,0.08), pos_hint={'x':0.37,'y':0.54}, color="black")
       
        typethemeloc=Builder.load_string(
        """
Spinner:
    text:"Chosir"
    pos_hint:{'x':0.55, 'y':0.56}
    size_hint:(0.4,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
    
        """)
        typethemeloc.bind(on_release=self.chargedistincttype)

        longloc= MDTextField(hint_text="Longitide",font_size='17sp',disabled=True,line_color_normal='black', pos_hint={'x':0.05, 'y':0.46},size_hint=(0.4,0.1))
        altloc= MDTextField(hint_text="Lattitude",font_size='17sp',disabled=True,line_color_normal='black', pos_hint={'x':0.55, 'y':0.46},size_hint=(0.4,0.1))
       
        distance= MDTextField(hint_text="Distance",font_size='17sp',disabled=True,line_color_normal='black', pos_hint={'x':0.05, 'y':0.38},size_hint=(0.4,0.1))
        nbrheur= MDTextField(hint_text="Temps ",font_size='17sp',disabled=True,line_color_normal='black', pos_hint={'x':0.55, 'y':0.38},size_hint=(0.4,0.1))

        btnimagetemp=Builder.load_string('''
Button:
    background_normal:'temperature.jpg'
    size_hint:(0.2,0.12)
    pos_hint:{'x':0.55,'y':0.25}
   

    canvas.before:
        Color:
            rgb:11/255,11/255,11/255
        Rectangle:
            pos:self.pos
            size:self.size

        
''')

        labtemp=Label(text="[b][/b]",markup=True,size_hint=(0.2,0.08), pos_hint={'x':0.75,'y':0.28},color="black", font_size='14sp')

        btnimgetat=Builder.load_string('''
Button:
    background_normal:''
    background_color:[0,0,0,0]
    size_hint:(0.3,0.12)
    pos_hint:{'x':0.08,'y':0.25}   
    
    canvas.before:
        Color:
            rgb:11/255,11/255,11/255
        Rectangle:
            pos:self.pos
            size:self.size
                            
                                           
        ''')
        
        
        btnimgetat.bind(on_release=self.changeimg)

        btngpsloc=Button(background_normal='position.jpg', size_hint=(0.2,0.15), pos_hint={'x':0.8,'y':0.7})
        btngpsloc.bind(on_release=self.closegps)

        modulcatioloc= MDTextField(hint_text="Modulation",text="Frequence",font_size='12sp',disabled=True,line_color_normal='black', pos_hint={'x':0.05, 'y':0.15},size_hint=(0.3,0.06))
        amplitudeloc= MDTextField(hint_text="Synchronisation",text="Logarithmique",font_size='12sp',disabled=True,line_color_normal='black', pos_hint={'x':0.4, 'y':0.15},size_hint=(0.3,0.06))
        precisionloc=MDTextField(hint_text="Précision",text="Double",font_size='12sp',disabled=True,line_color_normal='black', pos_hint={'x':0.75, 'y':0.15},size_hint=(0.2,0.06))
        
        vitessloc=MDTextField(hint_text="Frequence",text="1.3 Ghz",font_size='12sp',disabled=True,line_color_normal='black', pos_hint={'x':0.05, 'y':0.07},size_hint=(0.2,0.06))
        
        btntracerloc=Builder.load_string(
        """
Button:
    text:"[b]Tracer[/b]"
    markup:True
    size_hint:(0.3,0.04)
    color:'white'
    background_color:[0,0,0,0]
    pos_hint:{'x':0.65,'y':0.07}

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]

        """)
        
        btntracerloc.bind(on_release=self.tracerloc)


        # les objet de la page de trafic
        #latitretrafic=Label(text="[b]Type[/b]",markup=True,size_hint=(0.2,0.08), pos_hint={'x':0.37,'y':0.56}, color="black")

        latitretrafic=Label(text="[b]TRAFIC TEMPOREL[/b]",color='black', font_size="20sp", markup=True, size_hint=(0.8,0.1), pos_hint={'center_x':0.5, 'y':0.8})

        tabtrafic=MDDataTable(column_data=[
            ("ID",dp(20)),
            (("LIBELLE",dp(30))),
            (("TYPE",dp(30))),
            (("DATE Rdv",dp(30))),
            (("ADRESSE",dp(40))),
            (("RESP. CIBLE",dp(25))),
            (("TELEPHONE",dp(25))),
            (("LONGITIDE",dp(25))),
            (("ALTITUDE",dp(25))),
            (("DATETIME",dp(25)))
            ], row_data=[],size_hint=(0.9,0.4),pos_hint={'x':0.05,'y':0.4},check=True,rows_num=2000,use_pagination=True)

        tabtrafic.bind(on_check_press=self.check_rdv)

        labdatetrafic=Label(text="[b]Date[/b]",markup=True,size_hint=(0.1,0.08), pos_hint={'x':0.05,'y':0.3}, color="black")
       
        combodattrafic=Builder.load_string(
        """
Spinner:
    text:"Chosir"
    pos_hint:{'x':0.4, 'y':0.32}
    size_hint:(0.55,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
        """)

        combodattrafic.bind(on_release=self.chargedatetrafic)
        combodattrafic.bind(text=self.affdatetrafic)

        labtypetrafic=Label(text="[b]Type[/b]",markup=True,size_hint=(0.1,0.08), pos_hint={'x':0.05,'y':0.23}, color="black")
       
        combtypetrafic=Builder.load_string(
        """
Spinner:
    text:"Chosir"
    pos_hint:{'x':0.4, 'y':0.24}
    size_hint:(0.55,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
        """)
        
        combtypetrafic.bind(on_release=self.chargetypetrafic)
        combtypetrafic.bind(text=self.afftypetrafic)

        trechresptrafic=MDTextField(hint_text="Responsable",font_size='11sp',line_color_normal='black', pos_hint={'x':0.05, 'y':0.15},size_hint=(0.35,0.06))

        comboresptrafic=Builder.load_string(
        
        """
Spinner:
    text:"Chosir"
    pos_hint:{'x':0.6, 'y':0.17}
    size_hint:(0.35,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
        """)
        
        comboresptrafic.bind(on_release=self.chargerespotrafic)
        comboresptrafic.bind(text=self.affrespotrafic)

        bexportrafic=Builder.load_string(
        """ 
Button:
    text:"[b]Export Pdf[/b]"
    size_hint:(0.35,0.04)
    markup:True
    color:'white'
    background_color:(0,0,0,0)
    pos_hint:{'x':0.6,'y':0.07}

    canvas.before:
        Color:
            rgb:0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]

            
        """)

        bexportrafic.bind(on_release=self.updatetheme)

        

        # les outils de la page de setting
        # jaune-vert=0.4,0.6,0.2, tomato=0.8,0.5,0.2, vert claire =0.1,0.5,0.2

        

        bmenu1=Builder.load_string(
        """
Button:
    text:"Saving"
    font_size:"15sp"
    markup:True
    pos_hint:{'x':0.05,'y':0.88}
    size_hint:(0.4,0.04)
    color:'white'
    background_color:[0,0,0,0]

    canvas.before:
        Color:
            rgb:0.4,0.6,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
""")    
        
        bmenu1.bind(on_release=self.opensavetheme)

        bmenu2=Builder.load_string(
        """
Button:
    text:"Updating"
    font_size:"15sp"
    markup:True
    pos_hint:{'x':0.55,'y':0.88}
    size_hint:(0.4,0.04)
    color:'white'
    background_color:[0,0,0,0]

    canvas.before:
        Color:
            rgb:0.4,0.6,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
            
        """)
        
        bmenu2.bind(on_release=self.updatetheme)

        bmenu1rien=Button(pos_hint={'x':0.05,'y':0.86},size_hint=(0.42,0.1),background_color='seagreen')
      
        bmenu2rien=Button(pos_hint={'x':0.53,'y':0.86},size_hint=(0.42,0.1),background_color='seagreen')

        t1trafic= MDTextField(hint_text="ID Theme",font_size='17sp',disabled=True,line_color_normal='black', pos_hint={'x':0.05, 'y':0.79},size_hint=(0.4,0.06))
        t1trafic.bind(text=self.eff1)
        t2trafic= MDTextField(hint_text="Libellé ",font_size='17sp',line_color_normal='black', pos_hint={'x':0.55, 'y':0.79},size_hint=(0.4,0.08))
        t2trafic.bind(text=self.eff2)

        t3rechtrafic= MDTextField(hint_text="search",font_size='12sp',line_color_normal='black', pos_hint={'x':0.25, 'y':0.92},size_hint=(0.23,0.07))
        
        comborechupdatetheme=Spinner(text="[b]Chosir[/b]",markup=True,pos_hint={'x':0.5, 'y':0.94},size_hint=(0.25,0.04),background_normal="", color="black",font_size='15sp')
        comborechupdatetheme.bind(on_release=self.comborechupdatethemelike)
        comborechupdatetheme.bind(text=self.recherchethemesetting)

        btnsetting=Builder.load_string(
        """
Button:
    text:"[b]Save[/b]"
    markup:True
    size_hint:(0.3,0.04)
    color:'white'
    background_color:[0,0,0,0]
    pos_hint:{'x':0.65,'y':0.74}

    canvas.before:
        Color:
            rgb:0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]

        """)
        
        btnsetting.bind(on_release=self.savemodeltheme)

        btnsetteingdelelte=Builder.load_string(
        """
Button:
    text:"[b]Delete[/b]"
    markup:True
    size_hint:(0.3,0.04)
    color:'white'
    background_color:[0,0,0,0]
    pos_hint:{'x':0.65,'y':0.67}

    canvas.before:
        Color:
            rgb:0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]

        """)

        btnsetteingdelelte.bind(on_release=self.deletetheme)

        titinfoperso=Label(text="[b]Perso Info [/b]",font_size='15sp',markup=True,size_hint=(0.2,0.08), pos_hint={'x':0.05,'y':0.68}, color="black")

        labtypetransport=Label(text="[b]Type Trans..[/b]",font_size='12sp',markup=True,size_hint=(0.2,0.08), pos_hint={'x':0.05,'y':0.58}, color="black")
        iminfoperson=Image(source="feuill.jpg", size_hint=(0.3,0.3), pos_hint={'x':0.1,'y':0.58})

        moyentransport= Builder.load_string(
        
        """
Spinner:
    text:"Chosir"
    pos_hint:{'x':0.3, 'y':0.6}
    size_hint:(0.3,0.04)
    background_color:[0,0,0,0]
    color:"white"
    font_size:'16sp'

    canvas.before:
        Color:
            rgb: 0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]
        """)

        
        moyentransport.bind(on_release=self.openmoyentranport)

        distanceheure = MDTextField(hint_text="Distance/H",font_size='15sp',line_color_normal='black', pos_hint={'x':0.65, 'y':0.57},size_hint=(0.3,0.07))
        distanceheure.bind(text=self.effdateheure)

        btnsavpersoninfo=Builder.load_string(
        """
Button:
    text:"[b]Save[/b]"
    markup:True
    size_hint:(0.3,0.04)
    color:'white'
    background_color:[0,0,0,0]
    pos_hint:{'x':0.65,'y':0.52}

    canvas.before:
        Color:
            rgb:0.1,0.5,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[10]

        """)

        btnsavpersoninfo.bind(on_release=self.saveinfoperson)


        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select distance from distance where id='1'")
            results=self.cur.fetchone()

            self.cur.close()
            ccon.close()

            if results:
                distheure=str(results[0])+" Km/H"

        except:
            pass


        #cadregauche.add_widget(btaction)

        cadregauche.add_widget(b1)
        cadregauche.add_widget(b2)
        cadregauche.add_widget(b3)
        cadregauche.add_widget(b4)
        cadregauche.add_widget(b5)

        cadre.add_widget(imgtete)
        
        cadre.add_widget(cadregauche)
        cadre.add_widget(imgg)
        cadre.add_widget(lb)
        cadre.add_widget(latitre)
        cadre.add_widget(bsetting)

        cadre.add_widget(Builder.load_string(KV))

        return cadre
    

    def affmenu(self,instance):
        pass
    def effdateheure(self,instance,value):
        if instance.text=="":
            instance.hint_text="Distance/H"
        else:
            instance.hint_text=""

    def saveinfoperson(self,instance):

        try:
            dist=int(distanceheure.text)

            if instance.text=="[b]Save[/b]":

                self.connexion()
                cur=ccon.cursor()
                cur.execute("insert into distance(id,distance) values(?,?)",(1,dist))
                ccon.commit()
                cur.close()
                ccon.close()
                
                msg1=Popup(title="RESULT",content=Button(text="Save Succeful !!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

                distanceheure.text=""

            elif instance.text=="[b]Update[/b]":
                
                self.connexion()
                cur=ccon.cursor()
                cur.execute('update distance set distance=? where id=?',(dist,1))
                ccon.commit()

                cur.close()
                ccon.close()

                msg1=Popup(title="RESULT",content=Button(text="Succeful !!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

                distanceheure.text=""

        except:

            msg1=Popup(title="RESULT",content=Button(text="ERROR !!...Distance doit etre \nun entier sachant qu elle est deduite\nen Km/H",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()
    
    def openmoyentranport(self,instance):
        
        instance.values=""

        listt=['Jet','Voiture','Moto','Pied']

        for li in listt:
            instance.values.append(li)

        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select distance from distance where id='1'")
            results=self.cur.fetchone()

            self.cur.close()
            ccon.close()

            if results:
                distanceheure.text=str(results[0])+" Km/H"

        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()


    def affidtheme(self,instance,value):
        global iddst
        
        instance.values=""
        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select id_model from model_theme where detail='"+instance.text+"'")
            results=self.cur.fetchone()

            self.cur.close()
            ccon.close()

            if results:
                iddst=results[0]

        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()

    def chargetheme(self,instance):

        instance.values=""
        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select detail from model_theme")
            results=self.cur.fetchall()

            self.cur.close()
            ccon.close()

            for lign in results:
                instance.values.append(str(lign).replace("('","").replace("',)",""))

        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()
    
    def eff2(self,instance,value):
        try:
            if instance.text=="":
                instance.hint_text="Detail"
            else:
                instance.hint_text=""
        except:
            pass

    def eff1(self,instance,value):
        try:
            if instance.text=="":
                instance.hint_text="ID Theme"
            else:
                instance.hint_text=""
        except:
            pass
    
    def deletetheme(self,instance):
        #global codepays

        vall=0

        try:

            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select typpe from theme,model_theme where typpe=id_model and detail='"+t2trafic.text+"'")
            results=self.cur.fetchone()
            self.cur.close()
            ccon.close()

            if results:
                vall=results[0]

            if vall==0:
                self.connexion()
                cur=ccon.cursor()
                cur.execute('delete from model_theme where id_model=?',(int(t1trafic.text),))
                ccon.commit()
                cur.close()
                ccon.close()

                msg1=Popup(title="RESULT",content=Button(text="Succeful !!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

            else:
                msg1=Popup(title="RESULT",content=Button(text="Impossible car cette info\npossede deja un alias!!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()
        except:
            msg1=Popup(title="RESULT",content=Button(text="ERROR !!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()

    def savemodeltheme(self,instance):

        try:

            if instance.text=="[b]Save[/b]":

                self.connexion()
                cur=ccon.cursor()
                cur.execute("insert into model_theme(id_model,detail) values(?,?)",(int(t1trafic.text),t2trafic.text))
                ccon.commit()
                cur.close()
                ccon.close()
                
                msg1=Popup(title="RESULT",content=Button(text="Save Succeful !!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

                t1trafic.text=str(random.randint(0,500))
                t2trafic.text=""

            elif instance.text=="[b]Update[/b]":
                
                self.connexion()
                cur=ccon.cursor()
                cur.execute('update model_theme set detail=? where id_model=?',(t2trafic.text,int(t1trafic.text)))
                ccon.commit()

                cur.close()
                ccon.close()

                msg1=Popup(title="RESULT",content=Button(text="Succeful !!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()
                        
                t1trafic.text=""
                t2trafic.text=""

        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()


    def comborechupdatethemelike(self,instance):

        t1trafic.text=""
        t2trafic.text=""

        instance.values=""

        instance.text="[b]Chosir[/b]"

        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select detail from model_theme where detail LIKE'%"+t3rechtrafic.text+"%'")
            results=self.cur.fetchall()

            self.cur.close()
            ccon.close()

            for lign in results:
                instance.values.append(str(lign).replace("('","").replace("',)",""))

        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()


    def recherchethemesetting(self,instance, value):
        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select id_model,detail from model_theme where detail='"+instance.text+"'")
            results=self.cur.fetchone()

            if results:
                t1trafic.text=str(results[0])
                t2trafic.text=str(results[1])

            self.cur.close()
            ccon.close()
        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()
    
    def updatetheme(self,instance):

        t1trafic.text=""
        t2trafic.text=""
        btnsetting.text="[b]Update[/b]"

        btnsavpersoninfo.text="[b]Update[/b]" 
       

        try:
            cadre.add_widget(btnsetteingdelelte)
        except:
            pass
        
        try:
            cadre.add_widget(t3rechtrafic)
        except:
            pass
        try:
            cadre.add_widget(comborechupdatetheme)
        except:
            pass
        
        try:
            cadre.remove_widget(latitretrafic) 
        except:
            pass

    def opensavetheme(self,instance):
        
        t2trafic.text=""
        t1trafic.text=str(random.randint(0,500))
        btnsetting.text="[b]Save[/b]"
        btnsavpersoninfo.text="[b]Save[/b]"

        try:
            cadre.remove_widget(btnsetteingdelelte)
        except:
            pass

        try:
            cadre.remove_widget(t3rechtrafic)
        except:
            pass
        try:
            cadre.remove_widget(comborechupdatetheme)
        except:
            pass
        
        try:
            cadre.add_widget(latitretrafic)
        except:
            pass

    def enregistrer_model_theme(self,instance):
        pass

        #cursorr.execute('''  CREATE TABLE IF NOT EXISTS model_theme(id_model INTEGER PRIMARY KEY,detail TEXT)  ''')


    def affrespotrafic(self,instance,value):
        global libreexport,resultsexport
    
        try:

            if libreexport==True:

                self.connexion()
                self.cur=ccon.cursor()
                self.cur.execute("select ID,libelle,detail,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg from theme,model_theme where typpe=id_model and nom_concerne='"+instance.text+"'")
                
                resultsexport=self.cur.fetchall()

                self.cur.close()
                ccon.close()
            else:
                self.connexion()
                self.cur=ccon.cursor()
                self.cur.execute("select ID,libelle,detail,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg from theme,model_theme where typpe=id_model and nom_concerne='"+instance.text+"'")
                resultsexport=self.cur.fetchall()

                tabtrafic.row_data=resultsexport

                self.cur.close()
                ccon.close()
        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()
        
    
    def chargerespotrafic(self,instance):

        instance.values=""

        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select distinct nom_concerne from theme where nom_concerne LIKE'%"+trechresptrafic.text+"%'")
            results=self.cur.fetchall()

            self.cur.close()
            ccon.close()

            for element in results:
                
                instance.values.append(str(element).replace("('","").replace("',)",""))

        
        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()
    
    
    def afftypetrafic(self,instance,value):
        global libreexport,resultsexport
       
        if libreexport==True:

            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select ID,libelle,detail,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg from theme,model_theme where typpe=id_model and detail='"+instance.text+"'")
            resultsexport=self.cur.fetchall()

            self.cur.close()
            ccon.close()
        else:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select ID,libelle,detail,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg from theme,model_theme where typpe=id_model and detail='"+instance.text+"'")
            resultsexport=self.cur.fetchall()

            tabtrafic.row_data=resultsexport

            self.cur.close()
            ccon.close()
    def chargetypetrafic(self,instance):

        instance.values=""

        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select distinct detail from theme,model_theme where typpe=id_model")
            results=self.cur.fetchall()

            self.cur.close()
            ccon.close()

            for element in results:
                
                instance.values.append(str(element).replace("('","").replace("',)",""))
        
        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()
        

    def affdatetrafic(self,instance,value):
        global libreexport,resultsexport

        if libreexport==True:

            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select ID,libelle,detail,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg from theme,model_theme where typpe=id_model and ddate='"+instance.text+"'")
            
            resultsexport=self.cur.fetchall()

            self.cur.close()
            ccon.close()
        else:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select ID,libelle,detail,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg from theme,model_theme where typpe=id_model and ddate='"+instance.text+"'")
            resultsexport=self.cur.fetchall()

            tabtrafic.row_data=resultsexport

            self.cur.close()
            ccon.close()
    
    def chargedatetrafic(self,instance):

        instance.values=""

        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select distinct ddate from theme")
            results=self.cur.fetchall()

            self.cur.close()
            ccon.close()

            for element in results:
                
                instance.values.append(str(element).replace("('","").replace("',)",""))

        
        except:
            msg=Popup(title="STATUT",content=Button(text='ERROR!'),size_hint=(None, None), size=(200,200))
            msg.open()
        
    def fermecarnetrdvtrafic(self,instance):
        global msgtrafic

        msgtrafic.dismiss()

    def check_rdv(self,instance_table,current_row):
        global msgtrafic

        jour=0
        detail="rien"

        #try:
        dat=datetime.now().strftime('%Y-%m-%d')

        datt=datetime.strptime(dat,'%Y-%m-%d').date()

        date_rdv=str(current_row[3])

        date_rdvv=datetime.strptime(date_rdv,'%Y-%m-%d').date()

        jour=date_rdvv-datt

        jour=str(jour)

        coupe=jour.split(" ")

        jour=coupe[0]

        try:
            jour=int(jour)
        except:
            jour=int('0')

        if jour>0:
            if jour==1:
                detail="Rdv aura lieu dans :  "+str(jour) +" Jr"
            else:
                detail="Rdv aura lieu dans :  "+str(jour) +" Jrs"

        elif jour<0:

            jourr=jour

            chaine=str(jourr)

            chaine=chaine[1:]

            if jour==-1:
                detail="Rdv passé il y a :  "+chaine+" Jr"
            else:
                detail="Rdv passé il y a :  "+chaine+" Jrs"
        else:
            detail="Rdv d'aujourd'hui" 

        #except:
            #pass
        

        cad=MDFloatLayout()

        labb1=Label(text= detail ,font_size='14sp',pos_hint={'center_x':0.5,'center_y':0.65},color='white',size_hint=(0.8,0.2))
        
        bb2=Button(text="[b]Fermer[/b]", background_color='blue',pos_hint={'center_x':0.8,'center_y':0.25},size_hint=(0.4,0.04),markup=True,color='white')
        bb2.bind(on_release=self.fermecarnetrdvtrafic)

        try:  
            cad.add_widget(labb1)
            cad.add_widget(bb2)
           
        except:
            pass

        msgtrafic=Popup(title="CARNET NOIR ",background_color='seagreen',content=cad,size_hint=(None, None), size=(200,200))
        msgtrafic.open()

    def tracerloc(self,instance):

        if instance.text=="[b]Tracer[/b]":

            try:

                mpass=folium.Map(location=[altactuell,longactuell],zoom_start=15)

                folium.Marker(location=[altactuell,longactuell],radius=50,popup='Moi').add_to(mpass)
                folium.CircleMarker(location=[altactuell,longactuell],radius=10,popup='Moi',color='red').add_to(mpass)

                folium.Marker(location=[float(altloc.text),float(longloc.text)],radius=50,popup='La Cible').add_to(mpass)

                folium.PolyLine(locations=[(altactuell,longactuell),(float(altloc.text),float(longloc.text))], line_opacity=0.5).add_to(mpass)

                mpass.save('carte.html')

                instance.text="[b]Ouvrir[/b]"

                msg1=Popup(title="RESULT",content=Button(text=" Reussi !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

            except:
                msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()
        else:

            chem=os.path.dirname(os.path.abspath(__file__))

            chemnew=os.path.join(chem,'carte.html')

            webbrowser.open(f'file:///{chemnew}')

    def changeimg(self,instance):

        if instance.background_normal=='nouageux.jpg':
            instance.background_normal='solei.png'
        elif instance.background_normal=='solei.png':
            instance.background_normal='pluie.jpg'
        elif instance.background_normal=='pluie.jpg':
            instance.background_normal='nouageux.jpg'
    
    def chargejour(self,instance):
        instance.values=""

        listann=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

        for lig in listann:
            instance.values.append(lig)


    def chargemois(self,instance):
        instance.values=""

        listann=['1','2','3','4','5','6','7','8','9','10','11','12']

        for lig in listann:
            instance.values.append(lig)
    
    def charganne(self, instance):
        instance.values=""

        listann=['2024','2025','2026']

        for lig in listann:
            instance.values.append(lig)

    def affchois(self,instance,value):
        global iddtheme

        #ID,libelle,typpe,ddate,adresse,nom_concerne,tel,longitude,altitude

        try:
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select  detail,ID,libelle,typpe,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg from theme,model_theme where id_model=typpe and libelle='"+ instance.text +"'")

            lig=self.cur.fetchone()

            daterdv='0000-00-00'

            if lig:

                typetheme.text=lig[0]
                iddtheme=lig[1]
                nomtheme.text=lig[2]
                typps=lig[3]
                daterdv=lig[4]
                adressresp.text=lig[5]
                nomconcerne.text=lig[6]
                tel.text=lig[7]
                longitude.text=lig[8]
                altitude.text=lig[9]
                lbdate.text=lig[10]
            
            ccon.close()

        except:
            msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()
        
        try:
            daterdv=str(daterdv)
            tabdat=daterdv.split('-')

            ann.text=tabdat[0]
            moiss.text=tabdat[1]
            jourr.text=tabdat[2]

        except:
            msg1=Popup(title="RESULT",content=Button(text="show date Error  !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()
    
    def chargedistincttype(self,instance):

        instance.values=""
        instance.text=""

        try:

            self.connexion()
            cur=ccon.cursor()
            cur.execute("select distinct typpe from theme") 

            ligne=cur.fetchall()

            for lig in ligne:
                instance.values.append(str(lig).replace('(','').replace(',)','').replace("'",""))
            
            ccon.close()

        except:
            msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()

    def affinfoloc(self,instance,value):
        global distheure

        btntracerloc.text="[b]Tracer[/b]"

        global altactuell,longactuell,dist

        try: 
            self.connexion()
            self.cur=ccon.cursor()
            self.cur.execute("select detail,longitude,altitude from theme,model_theme where libelle='"+ instance.text +"' and id_model=typpe")

            lig=self.cur.fetchone()

            if lig:

                typethemeloc.text=lig[0]
                longloc.text=lig[1]
                altloc.text=lig[2]

        except:
            msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()

        try:
            if altloc.text !="" and longloc.text!="":
            
                api_key = '816df9762d27a4792fb6ba28975fb716'
                labtemp.text=str(self.get_temperature(api_key,float(altloc.text),float(longloc.text)))+" °C"
        except:
            pass

        #altloc.text='-5.3276'
        #longloc.text='15.3136'

        #print(altactuell,"#",longactuell)
        #print(altloc.text,"#",longloc.text)
      
        try:
            distance.text=self.calculateurkilo(float(altloc.text),float(longloc.text),altactuell,longactuell)#15.3136,-4.3376,15.3136,-4.3276)#48.8566,2.3522,34.0522,-118.2437)#

            
            #str(math.ceil(dist/75))+" H"
            
        except:
            pass

       

        try:

            distt=distance.text.split(" ")
            disheurev=distheure.split(" ")
            
            nbrheur.text=int(distt[0])/ int(disheurev[0])

            print(disheurev[0])
            print(distt[0])

        except:
            pass

    def calculateurkilo(self,lat1, lon1, lat2, lon2):
        global dist

        try:
            R = 6371  # Rayon de la Terre en kilomètres
            lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
            dlat = lat2 - lat1
            dlon = lon2 - lon1
        
            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

            dist=R * c
            dist=math.ceil(dist)

            kiloo=str(dist)+" km"
        
            return kiloo
        
        except:
            msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()
    
    def recupcoordonnee():

        try:
            g=geocoder.ip('me')

            if g.latlng:

                latts=g.latlng[0]
                longgs=g.latlng[1]

            return latts,longgs
        
        except:
            msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()

    def get_temperature(self,api_key, latitude, longitude):

        try:

            url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temperature = data['main']['temp']

                if math.ceil(temperature)<=15:
                    
                    btnimgetat.background_normal='pluie.jpg'

                    msg1=Popup(title="RESULT",content=Button(text="Il fait pluie !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                    msg1.open()

                elif math.ceil(temperature)>15 and math.ceil(temperature)<=30:

                    btnimgetat.background_normal='nouageux.jpg'

                    msg1=Popup(title="RESULT",content=Button(text="Nuageux !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                    msg1.open()

                elif math.ceil(temperature)>30:
                
                    btnimgetat.background_normal='solei.png'

                    msg1=Popup(title="RESULT",content=Button(text="Il fait Beau !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                    msg1.open()

                return temperature
            
            else:
                raise Exception(f"Error: {data.get('message', 'Unable to fetch weather data')}")
       
        except:
            pass


    def recidtheloc(self,instance):

        instance.values=""
        instance.text=""

        longloc.text=""
        altloc.text=""
        distance.text=""
        nbrheur.text=""

        btnimgetat.background_normal=''
        labtemp.text=""

        try:

            self.connexion()
            cur=ccon.cursor()
            cur.execute("select libelle from theme where libelle like'%"+idthemeloc.text+"%'")

            ligne=cur.fetchall()

            for lig in ligne:
                instance.values.append(str(lig).replace('(','').replace(',)','').replace("'",""))
            
            ccon.close()

        except:
            msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()

    
    def rechidtheme(self,instance):

        instance.values=""
        instance.text=""

        nomtheme.text=""
        typetheme.text=""
        adressresp.text=""
        nomconcerne.text=""
        tel.text=""
        longitude.text=""
        altitude.text=""
        lbdate.text=""

        try:

            self.connexion()
            cur=ccon.cursor()
            cur.execute("select libelle from theme where libelle like'%"+idtheme.text+"%'")

            ligne=cur.fetchall()

            for lig in ligne:
                instance.values.append(str(lig).replace('(','').replace(',)','').replace("'",""))
            
            ccon.close()

        except:
            msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()

    def closegps(self,instance):
        global msggps,altactuell,longactuell

        try:
            msggps.dismiss()
        except:
            pass

        # creation et connexion à la base Sqlite 

        self.connexion()

        # recuperation de coordonnee gps

        try:
            
            g=geocoder.ip('me')
            
            if g.latlng:

                longactuell=g.latlng[0]
                altactuell=g.latlng[1]

                latts=g.latlng[0]
                longgs=g.latlng[1]

            longitude.text=str(latts)
            altitude.text=str(longgs)

            benregistrer.text="[b]Save[/b]"

        except:
            msg1=Popup(title="ERROR",content=Button(text="Erreur survenue, il semble que vous\nn etes pas connecté,si ce ne pas le cas\nNB: veuillez redemarrer l application",font_size='13sp',color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
            msg1.open()
    
    def numerisergps(self,instance):
        global msggps,iddtheme,iddst

        try:
            datt=ann.text+"-"+moiss.text+"-"+jourr.text
            datts=datetime.strptime(datt,'%Y-%m-%d').date()
        except:
            pass


        if instance.text=='[b]Suivant[/b]':

            if nomtheme.text=="" or typetheme.text=="" or typetheme.text=="Chosir" or adressresp.text=="" or nomconcerne.text=="" or tel.text=="":
                
                msg1=Popup(title="RESULT",content=Button(text="Saisie erronée !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()
            
            else:

                cadcloss=FloatLayout()

                bdemmgps=Button(text="[b]Demarrer[/b]",font_size='14sp', pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.3,0.05),color='white',markup=True,background_color='red')
                bdemmgps.bind(on_press=self.closegps)

                try:
                
                    cadcloss.add_widget(bdemmgps)

                except:
                    pass

                msggps=Popup(title="GPS",content=cadcloss,size_hint=(None, None), size=(282,250),background_color='seagreen')
                msggps.open()

        elif instance.text=="[b]Modifier[/b]":

            #print(datts)

            try:
                self.connexion()
                cur=ccon.cursor()
                cur.execute('update theme set libelle=?,typpe=?,ddate=?,adresse=?,nom_concerne=?,tel=? where ID=?',(nomtheme.text,str(iddst),datts,adressresp.text,nomconcerne.text,tel.text,iddtheme))
                ccon.commit()

                ccon.close()

                idtheme.text=""
                nomtheme.text=""
                combrecherche.text="Choisir"
                typetheme.text="Choisir"
                adressresp.text=""
                nomconcerne.text=""
                tel.text=""
                longitude.text=""
                altitude.text=""
                jourr.text="JJ"
                moiss.text="MM"
                ann.text="AAAA"

                msg1=Popup(title="RESULT",content=Button(text="Mofification effectuée avec succes !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

            except:
                msg1=Popup(title="RESULT",content=Button(text="Erreur survenue, veuillez ressayer plus tard",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

        else:
            
            try:
                self.connexion()
                cur=ccon.cursor()
                cur.execute("insert into theme(ID,libelle,typpe,ddate,adresse,nom_concerne,tel,longitude,altitude,datenreg) values(?,?,?,?,?,?,?,?,?,?)",(int(idtheme.text),nomtheme.text, str(iddst),datts,adressresp.text,nomconcerne.text,tel.text,longitude.text, altitude.text,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                ccon.commit()
                ccon.close()
                
                msg1=Popup(title="RESULT",content=Button(text="Save Succeful !!",color="white", background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

                idtheme.text=""
                nomtheme.text=""
                typetheme.text="Choisir"
                adressresp.text=""
                nomconcerne.text=""
                tel.text=""
                longitude.text=""
                altitude.text=""
                jourr.text="JJ"
                moiss.text="MM"
                ann.text="AAAA"

            except:
                msg1=Popup(title="RESULT",content=Button(text="Error !!",color="white",background_color='seagreen'),size_hint=(None, None), size=(282,200),background_color='seagreen')
                msg1.open()

                idtheme.text=str(random.randint(1,1500))

    def chargetype(self,instance):
        instance.values=""

        tab=["Pharmacie","Boutique","Ecole","Fac","Autre"]
        for lin in tab:
            instance.values.append(str(lin))

    def accueil(self,isntance):
        global etat

        b1.size_hint=(0,0.1)
        b1.text=""

        b2.size_hint=(0,0.1)
        b2.text=""

        b3.size_hint=(0,0.1)
        b3.text=""

        b4.size_hint=(0,0.1)
        b4.text=""

        b5.size_hint=(0,0.1)
        b5.text=""

        try:
            cadregauche.remove_widget(ic1)
        except:
            pass
        try:
            cadregauche.remove_widget(ic2)
        except:
            pass
        try:
            cadregauche.remove_widget(ic3)
        except:
            pass
        try:
            cadregauche.remove_widget(ic4)
        except:
            pass
        try:
            cadregauche.remove_widget(ic5)
        except:
            pass

        cadregauche.size_hint=0,0

        #btaction.size_hint=0,0

        #btaction.pos_hint={'x':0,'y':0.7}

        #btaction.background_normal='menu.jpg'


        etat = 0

        try:
            cadre.remove_widget(bsettingretour)
        except:
            pass

        try:
            cadre.add_widget(bsetting)
        except:
            pass

        try:
            cadregauche.remove_widget(b1)
            cadregauche.remove_widget(b2)
            cadregauche.remove_widget(b3)
            cadregauche.remove_widget(b4)
        except:
            pass
        try:
            cadre.add_widget(imgg)
        except:
            pass

        
        latitre.text="[b]Accueil[/b]"
        try:
            cadre.add_widget(latitre)
        except:
            pass


    def ajout(self, isntance):
        global etat

        b1.size_hint=(0,0.1)
        b1.text=""

        b2.size_hint=(0,0.1)
        b2.text=""

        b3.size_hint=(0,0.1)
        b3.text=""

        b4.size_hint=(0,0.1)
        b4.text=""

        b5.size_hint=(0,0.1)
        b5.text=""

        try:
            cadregauche.remove_widget(ic1)
        except:
            pass
        try:
            cadregauche.remove_widget(ic2)
        except:
            pass
        try:
            cadregauche.remove_widget(ic3)
        except:
            pass
        try:
            cadregauche.remove_widget(ic4)
        except:
            pass
        try:
            cadregauche.remove_widget(ic5)
        except:
            pass

        cadregauche.size_hint=0,0

        #btaction.size_hint=0,0

        #btaction.pos_hint={'x':0,'y':0.7}

        #btaction.background_normal='menu.jpg'

        etat = 0

        try:
            cadre.remove_widget(bsetting)
        except:
            pass

        try:
            cadregauche.remove_widget(b1)
            cadregauche.remove_widget(b2)
            cadregauche.remove_widget(b3)
            cadregauche.remove_widget(b4)
        except:
            pass

        latitre.text="[b]NOUVEAU THEME[/b]"

        idtheme.hint_text="ID_Thème"
        idtheme.disabled=True
        idtheme.password=True

        benregistrer.text="[b]Suivant[/b]"

        idtheme.text=""
        nomtheme.text=""
        
        adressresp.text=""
        nomconcerne.text=""
        tel.text=""
        longitude.text=""
        altitude.text=""
        lbdate.text=""

        jourr.text="JJ"
        moiss.text="MM"
        ann.text="AAAA"
        typetheme.text="Chosir"

        idtheme.text=str(random.randint(1,1500))

        try:
            cadre.remove_widget(lbdate)
        except:
            pass

        try:
            cadre.add_widget(trien1)
        except:
            pass

        try:
            cadre.add_widget(trien2)
        except:
            pass


        try:
            cadre.add_widget(latitre)
        except:
            pass

        try:
            cadre.add_widget(idtheme)
            
        except:
            pass
        
        try:
            cadre.add_widget(nomtheme)
            
        except:
            pass

        try:
            cadre.remove_widget(combrecherche)
        except:
            pass

        try:
            cadre.add_widget(typelab)
        except:
            pass
        try:
            cadre.add_widget(typetheme)
        except:
            pass
        try:
            cadre.add_widget(nomconcerne)
        except:
            pass
        try:
            cadre.add_widget(tel)
        except:
            pass
        try:
            cadre.add_widget(labrdv)
        except:
            pass
    
        try:
            cadre.add_widget(jourr)
            cadre.add_widget(moiss)
            cadre.add_widget(ann)
        except:
            pass

        try:
            cadre.add_widget(adressresp)
        except:
            pass
        try:
            cadre.add_widget(labgps)
        except:
            pass
        try:
            cadre.add_widget(altitude)
        except:
            pass
        try:
            cadre.add_widget(longitude)
        except:
            pass
        try:
            cadre.add_widget(benregistrer)
        except:
            pass

        try:
            cadre.remove_widget(imgg)
        except:
            pass

    def modificationtheme(self,instance): 
        global etat

        b1.size_hint=(0,0.1)
        b1.text=""

        b2.size_hint=(0,0.1)
        b2.text=""

        b3.size_hint=(0,0.1)
        b3.text=""

        b4.size_hint=(0,0.1)
        b4.text=""

        b5.size_hint=(0,0.1)
        b5.text=""

        try:
            cadregauche.remove_widget(ic1)
        except:
            pass
        try:
            cadregauche.remove_widget(ic2)
        except:
            pass
        try:
            cadregauche.remove_widget(ic3)
        except:
            pass
        try:
            cadregauche.remove_widget(ic4)
        except:
            pass
        try:
            cadregauche.remove_widget(ic5)
        except:
            pass

        #btaction.size_hint=0,0

        #btaction.pos_hint={'x':0,'y':0.7}

        #btaction.background_normal='menu.jpg'

        cadregauche.size_hint=0,0

        etat = 0

        

        try:
            cadre.remove_widget(bsetting)
        except:
            pass

        try:
            cadregauche.remove_widget(b1)
            cadregauche.remove_widget(b2)
            cadregauche.remove_widget(b3)
            cadregauche.remove_widget(b4)
        except:
            pass
    
        latitre.text="[b]MODIFICATION THEME[/b]"
        benregistrer.text="[b]Modifier[/b]"

        idtheme.text=""
        nomtheme.text=""
        typetheme.text=""
        adressresp.text=""
        nomconcerne.text=""
        tel.text=""
        longitude.text=""
        altitude.text=""
        lbdate.text=""

        jourr.text="JJ"
        moiss.text="MM"
        ann.text="AAAA"
        combrecherche.text="Chosir"

        try:
            cadre.add_widget(trien1)
        except:
            pass

        try:
            cadre.add_widget(trien2)
        except:
            pass

        try:
            cadre.add_widget(lbdate)
        except:
            pass
        
        try:
            cadre.add_widget(latitre)
        except:
            pass

        try:
            cadre.add_widget(idtheme)
            
        except:
            pass

        idtheme.hint_text="Rechercher"
        idtheme.disabled=False
        idtheme.password=False
        
        try:
            cadre.add_widget(nomtheme)
            
        except:
            pass

        try:
            cadre.add_widget(combrecherche)
        except:
            pass

        try:
            cadre.add_widget(typelab)
        except:
            pass
        try:
            cadre.add_widget(typetheme)
        except:
            pass
        try:
            cadre.add_widget(nomconcerne)
        except:
            pass
        try:
            cadre.add_widget(tel)
        except:
            pass
        try:
            cadre.add_widget(labrdv)
        except:
            pass
    
        try:
            cadre.add_widget(jourr)
            cadre.add_widget(moiss)
            cadre.add_widget(ann)
        except:
            pass

        try:
            cadre.add_widget(adressresp)
        except:
            pass
        try:
            cadre.add_widget(labgps)
        except:
            pass
        try:
            cadre.add_widget(altitude)
        except:
            pass
        try:
            cadre.add_widget(longitude)
        except:
            pass
        try:
            cadre.add_widget(benregistrer)
        except:
            pass

        try:
            cadre.remove_widget(imgg)
        except:
            pass
    
    def localisation(self,instance):
        global etat

        b1.size_hint=(0,0.1)
        b1.text=""

        b2.size_hint=(0,0.1)
        b2.text=""

        b3.size_hint=(0,0.1)
        b3.text=""

        b4.size_hint=(0,0.1)
        b4.text=""

        b5.size_hint=(0,0.1)
        b5.text=""

        try:
            cadregauche.remove_widget(ic1)
        except:
            pass
        try:
            cadregauche.remove_widget(ic2)
        except:
            pass
        try:
            cadregauche.remove_widget(ic3)
        except:
            pass
        try:
            cadregauche.remove_widget(ic4)
        except:
            pass
        try:
            cadregauche.remove_widget(ic5)
        except:
            pass

        cadregauche.size_hint=0,0

        #btaction.size_hint=0,0

        #btaction.pos_hint={'x':0,'y':0.7}

        #btaction.background_normal='menu.jpg'

        etat = 0

        try:
            cadre.remove_widget(bsetting)
        except:
            pass

        try:
            cadregauche.remove_widget(b1)
            cadregauche.remove_widget(b2)
            cadregauche.remove_widget(b3)
            cadregauche.remove_widget(b4)
        except:
            pass
    
        latitre.text="[b]TRACAGE THEME[/b]"
        combrechercheloc.text="Choisir"
        typethemeloc.text="Chosir"

        try:
            cadre.remove_widget(imgg)
        except:
            pass
        
        try:
            cadre.add_widget(latitre)
        except:
            pass

        try:
            cadre.add_widget(idthemeloc)
        except:
            pass
        try:
            cadre.add_widget(combrechercheloc)
        except:
            pass

        try:
            cadre.add_widget(typelabloc)
        except:
            pass

        try:
            cadre.add_widget(typethemeloc)
        except:
            pass
        try:
            cadre.add_widget(altloc)
        except:
            pass
        try:
            cadre.add_widget(longloc)
        except:
            pass

        try:
            cadre.add_widget(btnimagetemp)
        except:
            pass
        try:
            cadre.add_widget(nbrheur)
        except:
            pass
        try:
            cadre.add_widget(distance)
        except:
            pass

        try: 
            cadre.add_widget(btnimgetat)
        except:
            pass
        try:
            cadre.add_widget(labtemp)
        except:
            pass

        try:
            cadre.add_widget(btngpsloc)
        except:
            pass

        try:
            cadre.add_widget(modulcatioloc)
        except:
            pass
        try:
            cadre.add_widget(amplitudeloc)
        except:
            pass
        try:
            cadre.add_widget(precisionloc)
        except:
            pass

        try:
            cadre.add_widget(vitessloc)
        except:
            pass

        try:
            cadre.add_widget(btntracerloc)
        except:
            pass
       
    
    def trafic(self,instance):
        global etat,libreexport,resultsexport

        latitretrafic.text="[b]TRAFIC TEMPOREL[/b]"

        cadregauche.size_hint=0,0

        b1.size_hint=(0,0.1)
        b1.text=""

        b2.size_hint=(0,0.1)
        b2.text=""

        b3.size_hint=(0,0.1)
        b3.text=""

        b4.size_hint=(0,0.1)
        b4.text=""

        b5.size_hint=(0,0.1)
        b5.text=""

        try:
            cadregauche.remove_widget(ic1)
        except:
            pass
        try:
            cadregauche.remove_widget(ic2)
        except:
            pass
        try:
            cadregauche.remove_widget(ic3)
        except:
            pass
        try:
            cadregauche.remove_widget(ic4)
        except:
            pass
        try:
            cadregauche.remove_widget(ic5)
        except:
            pass


        #btaction.pos_hint={'x':0,'y':0.92}

        #btaction.size_hint=0,0

        cadregauche.size_hint=0,0
    
        #btaction.background_normal='ret.png'

        etat = 0

        try:
            cadre.add_widget(trechresptrafic)
        except:
            pass
        try:
            cadre.add_widget(comboresptrafic,)
        except:
            pass
        try:
            cadre.add_widget(bexportrafic)
        except:
            pass

        try:
            cadre.add_widget(combodattrafic)
        except:
            pass
        try:
            cadre.add_widget(labdatetrafic)
        except:
            pass
        try:
            cadre.add_widget(combtypetrafic)
        except:
            pass
        try:
            cadre.add_widget(labtypetrafic)
        except:
            pass
            
        try:
            cadre.add_widget(latitretrafic) 
        except:
            pass
        try:
            cadre.add_widget(tabtrafic)
        except:
            pass

        try:
            cadre.remove_widget(imgtete)
        except:
            pass

        try:
            cadre.remove_widget(bsetting)
        except:
            pass

        try:
            cadregauche.remove_widget(b1)
            cadregauche.remove_widget(b2)
            cadregauche.remove_widget(b3)
            cadregauche.remove_widget(b4)
        except:
            pass

        if libreexport==True:

            self.connexion()
            cur=ccon.cursor()
            cur.execute("select * from theme order by datenreg DESC")

            resultsexport=cur.fetchall()

            cur.close()
            ccon.close()

        else:

            self.connexion()
            cur=ccon.cursor()
            cur.execute("select * from theme order by datenreg DESC")

            resultsexport=cur.fetchall()

            cur.close()
            ccon.close()

            tabtrafic.row_data=resultsexport
    
    def retoursetting(self,instance):
        global etatsetting

        etatsetting="1"

        try:
            cadre.add_widget(latitre)
        except:
            pass

        try:
            cadre.add_widget(bsetting)
        except:
            pass

        try:
            cadre.remove_widget(instance)
        except:
            pass

        try:
            cadre.add_widget(imgtete)
        except:
            pass

        try:
            cadre.remove_widget(iminfoperson)
        except:
            pass

        try:
            cadre.remove_widget(btnsavpersoninfo)
        except:
            pass
            
        try:
            cadre.remove_widget(titinfoperso)
        except:
            pass

        try:
            cadre.remove_widget(labtypetransport)
        except:
            pass
        try:
            cadre.remove_widget(moyentransport)
        except:
            pass
        try:
            cadre.remove_widget(distanceheure)
        except:
            pass
        

        try:
            cadre.remove_widget(btnsetteingdelelte)
        except:
            pass

        try:
            cadre.remove_widget(btnsetting)
        except:
            pass

        try:
            cadre.remove_widget(t1trafic)
        except:
            pass
        try:
            cadre.remove_widget(t2trafic)
        except:
            pass

    
        try:
            cadre.remove_widget(t3rechtrafic)
        except:
            pass
        try:
            cadre.remove_widget(comborechupdatetheme)
        except:
            pass
        
        try:
            cadre.remove_widget(latitretrafic)
        except:
            pass
        try:
            cadre.remove_widget(tabtrafic)
        except:
            pass
        
        try:
            cadre.remove_widget(combodattrafic)
        except:
            pass
        try:
            cadre.remove_widget(labdatetrafic)
        except:
            pass
        try:
            cadre.remove_widget(combtypetrafic)
        except:
            pass
        try:
            cadre.remove_widget(labtypetrafic)
        except:
            pass

        try:
            cadre.remove_widget(trechresptrafic)
        except:
            pass
        try:
            cadre.remove_widget(comboresptrafic,)
        except:
            pass
        try:
            cadre.remove_widget(bexportrafic)
        except:
            pass

        try:
            cadre.remove_widget(bmenu1)
        except:
            pass
        try:
            cadre.remove_widget(bmenu2)
        except:
            pass
        try:
            cadre.remove_widget(bmenu1rien)
        except:
            pass
        try:
            cadre.remove_widget(bmenu2rien)
        except:
            pass

        #btaction.pos_hint={'x':0,'y':0.7}
        #btaction.size_hint=(0.25,0.15)
        #btaction.background_normal='menu.jpg'


    def settingparameters(self,instance):

        global etat,libreexport,resultsexport,etatsetting

        etatsetting="0"

        latitretrafic.text="[b]Setting[/b]"

        cadregauche.size_hint=0,0

        b1.size_hint=(0,0.1)
        b1.text=""

        b2.size_hint=(0,0.1)
        b2.text=""

        b3.size_hint=(0,0.1)
        b3.text=""

        b4.size_hint=(0,0.1)
        b4.text=""

        b5.size_hint=(0,0.1)
        b5.text=""

        #btaction.pos_hint={'x':0,'y':0.92}

        #btaction.size_hint=(0.15,0.08)
    
        #btaction.background_normal='ret.png'

        try:
            cadre.add_widget(bsettingretour)
        except:
            pass

        try:
            cadre.remove_widget(instance)
        except:
            pass

        etat = 0

        try:
            cadre.add_widget(iminfoperson)
        except:
            pass

        try:
            cadre.add_widget(btnsavpersoninfo)
        except:
            pass

        try:
            cadre.add_widget(titinfoperso)
        except:
            pass

        try:
            cadre.add_widget(labtypetransport)
        except:
            pass
        try:
            cadre.add_widget(moyentransport)
        except:
            pass
        try:
            cadre.add_widget(distanceheure)
        except:
            pass
        
        try:
            cadre.add_widget(btnsetting)
        except:
            pass

        try:
            cadre.add_widget(t1trafic)
        except:
            pass
        try:
            cadre.add_widget(t2trafic)
        except:
            pass


        try:
            cadre.add_widget(latitretrafic)
        except:
            pass

        try:
            cadre.remove_widget(imgtete)
        except:
            pass

        try:
            cadre.remove_widget(bsetting)
        except:
            pass

        try:
            cadre.remove_widget(latitre)
        except:
            pass

        try:
            cadre.add_widget(bmenu1)
        except:
            pass
        try:
            cadre.add_widget(bmenu2)
        except:
            pass

    def connexion(self):
        global ccon

        try:
            ccon=sqlite3.connect('localiseur.db')

            cursorr=ccon.cursor()

            cursorr.execute('''  CREATE TABLE IF NOT EXISTS theme(ID INTEGER PRIMARY KEY,libelle TEXT,typpe INTEGER,ddate DATE,adresse TEXT,nom_concerne TEXT,tel TEXT,longitude TEXT,altitude TEXT,datenreg DATETIME)  ''')

            cursorr.execute('''  CREATE TABLE IF NOT EXISTS model_theme(id_model INTEGER PRIMARY KEY,detail TEXT)  ''')  

            cursorr.execute('''  CREATE TABLE IF NOT EXISTS distance(id INTEGER PRIMARY KEY,distance INTEGER)  ''')  

            return ccon
        
        except:
            pass
    
    def seplier(self, instance): 
        global etat,etatsetting

        if etatsetting=="1":

            try:
                cadre.add_widget(imgtete)
            except:
                pass

            try:
                cadregauche.add_widget(b1)
                cadregauche.add_widget(b2)
                cadregauche.add_widget(b3)
                cadregauche.add_widget(b4)
                cadregauche.add_widget(b5)
            except:
                pass

            if etat==0:

                cadregauche.size_hint=0.6,0.6
                
                b1.size_hint=(0.5,0.1)
                b1.text="[b]  Accueil          [/b]"

                b2.size_hint=(0.5,0.1)
                b2.text="[b] Ajout            [/b]"

                b3.size_hint=(0.5,0.1)
                b3.text="[b]  Modification [/b]"

                b4.size_hint=(0.5,0.1)
                b4.text="[b]  Localisation[/b]"
                b5.size_hint=(0.5,0.1)
                b5.text="[b]  Trafic            [/b]"
                
                #instance.pos_hint={'x':0.5,'x':0.7}

                #instance.background_normal='back.jpg'


                try:
                    cadregauche.add_widget(ic1)
                except:
                    pass
                try:
                    cadregauche.add_widget(ic2)
                except:
                    pass
                try:
                    cadregauche.add_widget(ic3)
                except:
                    pass
                try:
                    cadregauche.add_widget(ic4)
                except:
                    pass
                try:
                    cadregauche.add_widget(ic5)
                except:
                    pass


                try:
                    cadre.remove_widget(trien1)
                except:
                    pass

                try:
                    cadre.remove_widget(trien2)
                except:
                    pass

                try:
                    cadre.remove_widget(bsetting)
                except:
                    pass

                try:
                    cadre.remove_widget(lbdate)
                except:
                    pass

                try:
                    cadre.remove_widget(combrecherche)
                except:
                    pass

                try:
                    cadre.remove_widget(latitre)
                except:
                    pass

                try:
                    cadre.remove_widget(latitre)
                except:
                    pass

                try:
                    cadre.remove_widget(idtheme)
                    
                except:
                    pass
                
                try:
                    cadre.remove_widget(nomtheme)
                    
                except:
                    pass
                try:
                    cadre.remove_widget(typelab)
                except:
                    pass
                try:
                    cadre.remove_widget(typetheme)
                except:
                    pass
                try:
                    cadre.remove_widget(nomconcerne)
                except:
                    pass
                try:
                    cadre.remove_widget(tel)
                except:
                    pass
                try:
                    cadre.remove_widget(labrdv)
                except:
                    pass
            
                try:
                    cadre.remove_widget(jourr)
                    cadre.remove_widget(moiss)
                    cadre.remove_widget(ann)
                except:
                    pass

                try:
                    cadre.remove_widget(adressresp)
                except:
                    pass
                try:
                    cadre.remove_widget(labgps)
                except:
                    pass
                try:
                    cadre.remove_widget(altitude)
                except:
                    pass
                try:
                    cadre.remove_widget(longitude)
                except:
                    pass
                try:
                    cadre.remove_widget(benregistrer)
                except:
                    pass

                try:
                    cadre.remove_widget(idthemeloc)
                except:
                    pass
                try:
                    cadre.remove_widget(combrechercheloc)
                except:
                    pass

                try:
                    cadre.remove_widget(typelabloc)
                except:
                    pass

                try:
                    cadre.remove_widget(typethemeloc)
                except:
                    pass

                try:
                    cadre.remove_widget(longloc)
                except:
                    pass

                try:
                    cadre.remove_widget(altloc)
                except:
                    pass

                try:
                    cadre.remove_widget(btnimagetemp)
                except:
                    pass
                try:
                    cadre.remove_widget(nbrheur)
                except:
                    pass
                try:
                    cadre.remove_widget(distance)
                except:
                    pass

                try: 
                    cadre.remove_widget(btnimgetat)
                except:
                    pass
                try:
                    cadre.remove_widget(labtemp)
                except:
                    pass
                try:
                    cadre.remove_widget(btngpsloc)
                except:
                    pass

                try:
                    cadre.remove_widget(modulcatioloc)
                except:
                    pass
                try:
                    cadre.remove_widget(amplitudeloc)
                except:
                    pass
                try:
                    cadre.remove_widget(precisionloc)
                except:
                    pass

                try:
                    cadre.remove_widget(vitessloc)
                except:
                    pass

                try:
                    cadre.remove_widget(btntracerloc)
                except:
                    pass

                #pos_hint={'x':0,'top':0.76}

                #img1.size_hint=(0.06,0.07)
                #img2.size_hint=(0.06,0.07)
                #img3.size_hint=(0.06,0.07)
                #img4.size_hint=(0.06,0.07)
                
                try:
                    cadre.remove_widget(trechresptrafic)
                except:
                    pass
                try:
                    cadre.remove_widget(comboresptrafic,)
                except:
                    pass
                try:
                    cadre.remove_widget(bexportrafic)
                except:
                    pass

                try:
                    cadre.remove_widget(combodattrafic)
                except:
                    pass
                try:
                    cadre.remove_widget(labdatetrafic)
                except:
                    pass
                try:
                    cadre.remove_widget(combtypetrafic)
                except:
                    pass
                try:
                    cadre.remove_widget(labtypetrafic)
                except:
                    pass
                    
                try:
                    cadre.remove_widget(latitretrafic) 
                except:
                    pass
                try:
                    cadre.remove_widget(tabtrafic)
                except:
                    pass
                

                etat = 1
            else:
                
                try:
                    cadregauche.remove_widget(ic1)
                except:
                    pass
                try:
                    cadregauche.remove_widget(ic2)
                except:
                    pass
                try:
                    cadregauche.remove_widget(ic3)
                except:
                    pass
                try:
                    cadregauche.remove_widget(ic4)
                except:
                    pass
                try:
                    cadregauche.remove_widget(ic5)
                except:
                    pass
                
                cadregauche.size_hint=0,0

                try:
                    cadre.add_widget(latitre)
                except:
                    pass

                b1.size_hint=(0,0.1)
                b1.text=""

                b2.size_hint=(0,0.1)
                b2.text=""

                b3.size_hint=(0,0.1)
                b3.text=""

                b4.size_hint=(0,0.1)
                b4.text=""

                b5.size_hint=(0,0.1)
                b5.text=""

                

                #instance.pos_hint={'x':0,'y':0.7}

                #img1.size_hint=(0,0)
                #img2.size_hint=(0,0)
                #img3.size_hint=(0,0)
                #img4.size_hint=(0,0)

                #instance.background_normal='menu.jpg'

                etat = 0

    def recuperation(self,apii,longg,altt):
        pass
        
AccueilApp().run()
