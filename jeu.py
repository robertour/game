#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 14:43:37 2016

@author: georgesarsouze
"""
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from configuration import conf

Builder.load_file('Cartes.kv')

class Cache1(DragBehavior,RelativeLayout):
       
    def on_touch_move(self,touch):
        tx,ty=touch.pos
        sx,sy=self.pos
        
        #####access the reference of  a carte and collide 
        if self.parent.ref_carte1.collide_point(*touch.pos):
            self.parent.ref_carte1.alpha_color=0.5
            ##### grab the gridlayout widget inside the Carte1
            the_carte1_gridlayout = self.parent.ref_carte1.children[0]
            ##### grab the position of this gridlayout
            position_inside_relative_layout = the_carte1_gridlayout.pos
            ##### convert the position to absolute coordinates as Carte1 uses relativelayout
            position_in_absolute_terms = self.the_carte1_gridlayout.to_window(*position_inside_relative_layout)
            ##### assign the position
            self.pos = position_in_absolute_terms
        else:
            self.parent.ref_carte1.alpha_color=0
        
        if self.parent.ref_carte2.collide_point(*touch.pos):
            self.parent.ref_carte2.alpha_color=0.5
        else:
            self.parent.ref_carte2.alpha_color=0
            
        if self.parent.ref_carte3.collide_point(*touch.pos):
            self.parent.ref_carte3.alpha_color=0.5
        else:
            self.parent.ref_carte3.alpha_color=0
            
        if self.parent.ref_carte4.collide_point(*touch.pos):
            self.parent.ref_carte4.alpha_color=0.5
        else:
            self.parent.ref_carte4.alpha_color=0
            
        return super(Cache1,self).on_touch_move(touch)
        
    #def on_touch_down(self,touch):
        #f self.parent.ref_carte1.collide_point(*touch.pos):
            #self.pos=self.parent.ref_carte1.pos
            

class Cache2(DragBehavior,RelativeLayout):
    def on_touch_move(self,touch):
        tx,ty=touch.pos
        sx,sy=self.pos
        
         #####access the reference of  a carte and collide 
        if self.parent.ref_carte1.collide_point(*touch.pos):
            self.parent.ref_carte1.alpha_color=0.5
        else:
            self.parent.ref_carte1.alpha_color=0
        
        if self.parent.ref_carte2.collide_point(*touch.pos):
            self.parent.ref_carte2.alpha_color=0.5
        else:
            self.parent.ref_carte2.alpha_color=0
            
        if self.parent.ref_carte3.collide_point(*touch.pos):
            self.parent.ref_carte3.alpha_color=0.5
        else:
            self.parent.ref_carte3.alpha_color=0
            
        if self.parent.ref_carte4.collide_point(*touch.pos):
            self.parent.ref_carte4.alpha_color=0.5
        else:
            self.parent.ref_carte4.alpha_color=0

        return super(Cache2,self).on_touch_move(touch)
    
class Cache3(DragBehavior,RelativeLayout):
    def on_touch_move(self,touch):
        tx,ty=touch.pos
        sx,sy=self.pos
        
         #####access the reference of  a carte and collide 
        if self.parent.ref_carte1.collide_point(*touch.pos):
            self.parent.ref_carte1.alpha_color=0.5
        else:
            self.parent.ref_carte1.alpha_color=0
        
        if self.parent.ref_carte2.collide_point(*touch.pos):
            self.parent.ref_carte2.alpha_color=0.5
        else:
            self.parent.ref_carte2.alpha_color=0
            
        if self.parent.ref_carte3.collide_point(*touch.pos):
            self.parent.ref_carte3.alpha_color=0.5
        else:
            self.parent.ref_carte3.alpha_color=0
            
        if self.parent.ref_carte4.collide_point(*touch.pos):
            self.parent.ref_carte4.alpha_color=0.5
        else:
            self.parent.ref_carte4.alpha_color=0

        return super(Cache3,self).on_touch_move(touch)
  
class Cache4(DragBehavior,RelativeLayout):
    def on_touch_move(self,touch):
        tx,ty=touch.pos
        sx,sy=self.pos
        
         #####access the reference of  a carte and collide 
        if self.parent.ref_carte1.collide_point(*touch.pos):
            self.parent.ref_carte1.alpha_color=0.5
        else:
            self.parent.ref_carte1.alpha_color=0
        
        if self.parent.ref_carte2.collide_point(*touch.pos):
            self.parent.ref_carte2.alpha_color=0.5
        else:
            self.parent.ref_carte2.alpha_color=0
            
        if self.parent.ref_carte3.collide_point(*touch.pos):
            self.parent.ref_carte3.alpha_color=0.5
        else:
            self.parent.ref_carte3.alpha_color=0
            
        if self.parent.ref_carte4.collide_point(*touch.pos):
            self.parent.ref_carte4.alpha_color=0.5
        else:
            self.parent.ref_carte4.alpha_color=0

        return super(Cache4,self).on_touch_move(touch)
     
    
         
         
class Carte1(RelativeLayout):
    pass
class Carte2(RelativeLayout):
    pass
class Carte3(RelativeLayout):
    pass
class Carte4(RelativeLayout):
    pass

class Interface(AnchorLayout):
    def choisir_un_probleme(self):
        self.ids.id_texte_probleme.text=conf['Problemes'][0]
    

    def afficher_solution_du_probleme(self):
        affichage=""
        for j in range(4):
            n_cache=j+1
            n_carte=conf['Solutions'][0][j][0]
            position=conf['Solutions'][0][j][1]
            affichage +="Cache "+str(n_cache)+"sur la carte "+str(n_carte)+" en position "+str(position)+"\n"
        self.ids.id_texte_solution.text=affichage 
       
##### class EspaceJeu(RelativeLayout):
##### I think GridLayout might be a bettter approach for this,
##### We will encounter a few problems with the dragging, 
##### you can check the SpaceInvaders (Chapter 5)
class EspaceJeu(GridLayout):
    pass
class EspaceOutils(BoxLayout):
    pass
##### I added a new class to separate the Buttons from the game
class EspaceButtons(BoxLayout):
    pass
class EspaceInstructions(RelativeLayout):
    pass
class JeuApp(App):
    def build(self):
        return Interface()
        
JeuApp().run()
