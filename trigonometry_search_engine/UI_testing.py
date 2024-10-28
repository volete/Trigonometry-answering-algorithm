"""
What im doing here is that im creating one window('root') 
and putting an Entry inside so i can get the prompt
and then use the prompt to render a label that displays the answer.
i may import llama or chatgpt for explaining how, since you kinda need a neural network for that,
and you won't catch me writing a whole neural network just for explaining something, fuck you
GUI: customtkinter
"""

""" TODO list """
#TODO: make it so you can see your prompt and your answer 


import customtkinter

# root configuration
root = customtkinter.CTk()
root.geometry("1000x500")
root.title("Trigonometry calculator")



main_label = customtkinter.CTkLabel(master=root, # Top label('Trigonometry calulator') configuration
                                    text="Trigonometry calculator", 
                                    font=("Arial", 44))



def on_enter_pressed(event): # when the enter button is pressed it gets the input and renders your input on screen 
    query_input = input_box.get()
    input_box.delete(0, 'end')

    #question label configuring
    question_label = customtkinter.CTkLabel(master=main_frame, text=query_input, font=("Helvetica", 25))
    question_label.pack(side="top")

    if query_input in 'hi':
        label = customtkinter.CTkLabel(master=root, text='hi')
        label.pack()




main_frame = customtkinter.CTkFrame(master=root, 
                                    width=1000, 
                                    height=250, 
                                    bg_color='#1c1c1c')


input_box = customtkinter.CTkEntry(master=main_frame, width=500, height=30, font=("Helvetica", 25))
input_box.bind("<Return>", on_enter_pressed)

main_label.pack(side="top", pady=30)
input_box.pack()
main_frame.pack(side="bottom", pady=30)
root.mainloop()
