##csv_reader

import json
import unidecode

#make first words more important

class Recipes:

    def init(filepath):

        with open(filepath,"r") as file:
            Recipes.recipes=json.loads(file.read())

        Recipes.names=[unidecode.unidecode("".join([char if char.isalpha() else " "
                       for char in i["Name"]]).lower()).split()
                       for i in Recipes.recipes]

        Recipes.descriptions=[unidecode.unidecode("".join([char if char.isalpha() else " "
                              for char in str(i["Description"])]).lower()).split()
                              for i in Recipes.recipes]

        Recipes.ingredients=[unidecode.unidecode("".join([char if char.isalpha() else " "
                              for char in str(i["Ingredients"])]).lower()).split()
                              for i in Recipes.recipes]

    def search(text):

        text=unidecode.unidecode("".join([i if i.isalpha() else " " for i in text])).lower().split()
        results=[]

        if len(" ".join(text))<=1:
            return([])

        for i,(recipe,description,ingredients) in enumerate(zip(Recipes.names,Recipes.descriptions,Recipes.ingredients)):

            results.append([i,0])
            results[-1][-1]+=sum(" ".join(recipe).count(word) for word in text)*5
            results[-1][-1]+=sum(" ".join(ingredients).count(word) for word in text)
            results[-1][-1]+=sum(" ".join(description).count(word) for word in text)*0

        results=sorted(results,key=lambda i: -i[-1])

        n=0
        while results[n][-1]:
            n+=1

        results=[(Recipes.recipes[i]["Name"],"_".join(Recipes.names[i])+".jpg") for i,count in results[:n]]

        return(results[::-1])

if __name__=='__main__':

    Recipes.init("files/recipes.json")
    [print(i) for i in Recipes.search("tomato, World.")]