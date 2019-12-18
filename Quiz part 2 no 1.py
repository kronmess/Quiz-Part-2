class Spell:   
    def __init__(self, incantation, name):    
        self.name = name    
        self.incantation = incantation   
    def __str__(self):    
        return self.name + '' + self.incantation + '\n' + self.get_description()   
    def get_description(self):    
        return 'No description'  
    def execute(self):    
        print(self.incantation)
class Accio(Spell):  
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def get_description(self):    
        return 'This charm summons an object to the caster, potentially over a significant distance'     
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')   
    def get_description(self):    
            return 'Causes the victim to become confused and befuddled.'   
    def study_spell(self,spell):    
        print(spell)
spell = Accio()  
spell.execute()
study_spell(spell)  
study_spell(Confundo()) 


#1 a) Spell is the parent class and Accio and Confundo are the child classes.
#1 b) It does not print anything.
#1 c) Nothing, because the method is not being called when only study_spell is used. The study spell method is defined only in the Confundo class
#1 d) You must add a get_description method in the Accio class that takes self as the parameter. 
# Then returns the string so it will print the description when print(Accio()) is typed.