from category import Category
// category -> filename
// Category -> name of class you want to import

class Store: 
    #init is like constructor

    def __init__(self, name="my store", categories):
         #first define attributes of the store
         #self is equivalent to "this" keyword
         self.name = name
         self.categories = categories

    def __str__(self):
        #return f'{self.name} has {len(self.categories)} categories'
        output = self.name
        # 1. Food
        # 2. Toys
        # 3. Beds

        i = 1
        for cat in self.categories:
            output += f'\n{i}. {cat}'
            i += 1
        output += f '\n{i}. Quit' #exit

        return output

    def __repr(self):
        return f'{self.name} has {len(self.categories)} categories'

my_store = Store("Pets Plus", ["Food", "Toys", "Beds"])
print(my_store)


#add input parser (how do we get input into the browser)
selection = int(input('Select a category number: \n'))-1 #initial selection


while(selection != len(my_store.categories)); #did they select quit? If not, let them chose again.
    print(f'You selected {my_store.categories[selection]}')
    selection = int(input('Select a category number: \n'))-1  #gives while the opportunity to check for quit
#save result in variable (selection)

#erros to check for:
    #input is valid number (>0, <len(cat))
    #actual categories