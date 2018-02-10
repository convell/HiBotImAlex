# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from disco.bot import Plugin
import re
import random 

class TutorialPlugin(Plugin):
    @Plugin.listen('MessageCreate')
    def on_message_create(self, event):
        triggerWords = ["im a", "i am a", "i'm", 'i"m', "i am", "im"]
        #if event.author.username != "HiBotImAlex" and not "@" in event.message.content:
        #    event.reply(event.message.content)
	if event.author.username == "Zetamancer":
	    event.reply("Dont talk to me or my bot children ever again")
        if event.author.username != "HiBotImAlex":
            matchedString = re.search(r"\b(?=("+'|'.join(triggerWords)+r")\b)\b",event.message.content, re.IGNORECASE)
            if matchedString:
                random.seed()
                alexChanceToSpeak = random.randint(0, 100)
                matchedString = matchedString.group(1)
                if matchedString and alexChanceToSpeak >= 50:
                    imString = event.message.content.split(matchedString,1)[1]
                    
                    if "," in imString:
                        imString = imString.split(",",1)[0]
                    elif "!" in imString:
                        imString = imString.split("!",1)[0]
                    elif "." in imString:
                        imString = imString.split(".",1)[0]
                    elif "?" in imString:
                        imString = imString.split("?",1)[0]

                    if not '"' in imString:
                        event.reply("Hi" + imString.lower() + ", I'm Alex")
                        return


    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
          event.msg.reply(event.author)
    
    @Plugin.command('ping')
    def on_ping_command(self, event):
          event.msg.reply('Pong!')
