#Defining a language function
def greet(lang):
   if lang == 'es':
       print('Hola')
   elif lang == 'fr':
        print('Bonjour')
   else:
        print('Hello')

def greet():
   return "Hello"

print(greet(),'Sally')