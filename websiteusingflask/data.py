import json


class Database:
    def __init__(self):
        try:
            with open ("file.json","r") as f:
                self.data= json.load(f)

        except FileNotFoundError:
            with open('file.json', 'w') as f:
                self.data={}
                json.dump(self.data,f)

    def save( self,name, email, password):

            with open('file.json', 'r') as rf:
                self.data = json.load(rf)
                if email in self.data:
                    return 1
                else:
                    self.data[email] = [name, password]
            with open('file.json', 'w') as wf:
                json.dump(self.data, wf)
                return 0

    def check(self,email,password):
        with open("file.json", "r") as f:
            self.data = json.load(f)
            if email in self.data:
                if self.data[email][1]== password:
                    return 1
                else:
                    return 0
            else:
                return 0





