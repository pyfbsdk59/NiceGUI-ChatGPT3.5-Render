from nicegui import ui
import os, openai

#openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenaiData:
    def __init__(self):
        self.api_key_string = ""    
        self.api_key_string2 = ""
        self.on_changed("")
    def on_changed(self, symbol: str):
        if symbol is None or symbol == "":
            pass

        elif symbol.lower() == "save_api":

            self.api_key_string2 = self.api_key_string
            print(self.api_key_string2)
            ui.label(f'openai api key已載入。')


odt = OpenaiData() #存放openai api key類別


ui.input("Type in your openai api key here.").bind_value(odt, "api_key_string")
ui.button("Save api key", on_click=lambda: odt.on_changed("save_api"))
openai.api_key = odt.api_key_string2#os.getenv("OPENAI_API_KEY")

conversation = []

class ChatGPT:  
    

    def __init__(self):
        self.api_key = ""
        self.messages = conversation
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")



    def get_response(self, user_input):
        self.api_key = odt.api_key_string2
        ui.label(f'openai api key已再度載入。')
        openai.api_key = self.api_key
        conversation.append({"role": "user", "content": user_input})
        

        response = openai.ChatCompletion.create(
	            model=self.model,
                messages = self.messages

                )

        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        
        print("AI回答內容：")        
        print(response['choices'][0]['message']['content'].strip())


        
        return response['choices'][0]['message']['content'].strip()











chatgpt = ChatGPT()

class Prompt2Response:


    def __init__(self):
        self.prompt_string = ""
        self.answer_string = ""
        self.on_changed("")
    def on_changed(self, symbol: str):
        if symbol is None or symbol == "":
            pass

        elif symbol.lower() == "generate":
            self.answer_string = chatgpt.get_response(self.prompt_string)
            ui.label(f'ChatGPT AI: {p2r.answer_string}')
            ui.run_javascript('window.location.reload()')	






p2r= Prompt2Response()

ui.input("Type in prompt here.").bind_value(p2r, "prompt_string")

ui.button("Generate", on_click=lambda: p2r.on_changed("generate"))

#.bind_value(prompt, "answer_string")
ui.run(title="NiceGUI-ChatGPT3.5-Render範例")




