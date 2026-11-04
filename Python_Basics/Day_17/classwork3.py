from abc import ABC, abstractmethod
class Notification:
    @abstractmethod
    def send(self,message):
        pass

class EmailNotification(Notification):
    def __init__(self,email):
        self.email = email

    def send(self,message):
        self.message = message
        return f"Email Sent to {self.email} : {message}"

class SmsNotification(Notification):
    def __init__(self,phone):
        self.phone = phone

    def send(self,message):
        self.message = message
        return f"SMS Sent to {self.phone} : {message}"

for n  in [EmailNotification("apil@gmail.com"),SmsNotification("980000000")]:
    print(n.send("Class starts at 7 AM"))