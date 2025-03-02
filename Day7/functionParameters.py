def greet(name):
    print("Hello!")
    print(f"Good morning! {name}.")

greet("Anshika")

# function with more than 1 input
def greet_with(name,location):
    print(f'Hello {name}!')
    print(f'What is it like in {location}?')
#positional arguments
greet_with("Anshika","Nowhere")
#Keyword arguments
greet_with(location = "Greece" , name = "Anshika")