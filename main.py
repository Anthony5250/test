from kivy.lang import Builder
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp

import TrainPriviteC 
KV = '''
<Example>:
    
    
MDScreen:
    
    textfield1 : field1
    textfield2 : field2
    textfield3 : field3
    textfield4 : field4
 
    
    MDTextField:
        id: field1
        hint_text: "Enter Question"
        pos_hint: {'center_x': 0.5 ,'center_y': 0.8}
        size_hint_x: None
        width: 300
        
    MDTextField:
        id: field2
        hint_text: "Enter answer1"
        pos_hint: {'center_x': 0.5 ,'center_y': 0.7}
        size_hint_x:None
        width: 300
    MDTextField:
        id: field3
        hint_text: "Enter answer2"
        pos_hint: {'center_x': 0.5 ,'center_y': 0.6}
        size_hint_x: None
        width: 300
    MDTextField:
        id: field4
        hint_text: "Enter answer2"
        pos_hint: {'center_x': 0.5 ,'center_y': 0.5}
        size_hint_x: None
        width: 300
    

    MDFillRoundFlatButton:
        text: "Save"
        pos_hint: {'center_x': 0.5 ,'center_y': 0.4}
        on_press: app.Save_Text()

        


        
    '''


class Train(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.title = "Train Privite"
        return Builder.load_string(KV)
    

    
    def Save_Text(self):
        question = self.root.textfield1.text
    
        question_result = TrainPriviteC.remove_symbols(question)
        question_lowered_result = TrainPriviteC.lower(question_result)
        
        answer1 = self.root.textfield2.text
        

        answer2 = self.root.textfield3.text
     

        answer3 = self.root.textfield4.text
       
        
        


        file = open("trained data.txt", "a")
        file.write(f"<div class='{question_lowered_result}'>\n<div class='answer'>{question_lowered_result}</div>\n<div class='answer1'>{answer1}</div>\n<div class='answer2'>{answer2}</div>\n<div class='answer3'>{answer3}</div>\n</div>\n")
        file.write("******************")
        file.close()

        self.root.textfield1.text = ""
        self.root.textfield2.text = ""
        self.root.textfield3.text = ""
        self.root.textfield4.text = ""

        
        
           



Train().run()
