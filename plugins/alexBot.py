#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from disco.bot import Plugin
import re
import random 
import datetime

class TutorialPlugin(Plugin):
    tags = {}
    lastTimeSpoke = datetime.datetime.now() + datetime.timedelta(minutes = -240)

    @Plugin.listen('MessageCreate')
    def on_message_create(self, event):
        triggerWords = ["im a", "i am a", "i'm", 'i"m', "i am", "im"]
	random.seed()
        alexChanceToSpeak = random.randint(0, 200)
        currentTime = datetime.datetime.now()
        timeDiff = currentTime - self.lastTimeSpoke
        minutesDiff = timeDiff.total_seconds() / 60
        adjustedChance = alexChanceToSpeak        
        
        #if minutesDiff > 3600:
        #    print "240"
        #    adjustedChance = alexChanceToSpeak + 25
        #elif minutesDiff > 2600:
        #    adjustedChance = alexChanceToSpeak + 15
        #    print "120"
        #elif minutesDiff > 2300:
        #    print "60"
        #    adjustedChance = alexChanceToSpeak + 10
        #elif minutesDiff > 2000:
        #    print "30"
        #    adjustedChance = alexChanceToSpeak + 5
        
	if alexChanceToSpeak >= 200:
	    event.reply(event.author.username + " just landed on a 0.5% roll, we have found a new super oof")
            self.tags[event.author.username] = "godmin"
            event.reply(':ok_hand: created tag `godmin`')

        elif event.author.username != "HiBotImAlex":
            matchedString = re.search(r"\b(?=("+'|'.join(triggerWords)+r")\b)\b",event.message.content, re.IGNORECASE)
            if matchedString:
                matchedString = matchedString.group(1)
                if matchedString and adjustedChance >=180:
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
			if alexChanceToSpeak >= 193:
			    event.reply("Hi" + imString.lower() + ", I'm Alex", tts=True)
                        else: 
			    event.reply("Hi" + imString.lower() + ", I'm Alex")
                        self.lastTimeSpoke = datetime.datetime.now()
                        return

    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
          event.channel.send_message('Woah, a new location to ping everyone from!')
    
    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
          event.msg.reply(event.author)
    
    @Plugin.command('ping')
    def on_ping_command(self, event):
          event.msg.reply('Pong!')

    @Plugin.command('tag', '<name:str> [value:str...]')
    def on_tag_command(self, event, name, value=None):

        if value:
            self.tags[name] = value
            event.msg.reply(':ok_hand: created tag `{}`'.format(value))
        else:
            if name in self.tags.keys():
                return event.msg.reply("`" + self.tags[name] + "`")
            else:
                return event.msg.reply('Unknown tag: `{}`'.format(value))
