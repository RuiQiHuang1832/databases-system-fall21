# bot.py
# This file is intended to be a "getting started" code example for students.
# The code in this file is fully functional.
# Students are free to edit the code in the milestone 3 folder.
# Students are NOT allowed to distribute this code without the express permission of the class instructor
# IMPORTANT: How to set your secret environment variables? read README guidelines.

# imports
import os
import discord
import database as db
import fetch as fe
# environment variables
token = os.environ['DISCORD_TOKEN']
server = os.environ['DISCORD_GUILD']

# database connection
# secret keys related to your database must be updated. Otherwise, it won't work
db_conn = db.connect()
# bot events
client = discord.Client()

@client.event
async def on_ready():
    """
    This method triggers with the bot connects to the server
    Note that the sample implementation here only prints the
    welcome message on the IDE console, not on Discord
    :return: VOID
    """
    print("{} has joined the server".format(client.user.name))


@client.event
async def on_message(message):
    """
    This method triggers when a user sends a message in any of your Discord server channels
    :param message: the message from the user. Note that this message is passed automatically by the Discord API
    :return: VOID
    """
    response = None # will save the response from the bot
    if message.author == client.user:
        
        return # the message was sent by the bot
    if message.type is discord.MessageType.new_member:
        response = "Welcome {}".format(message.author) # a new member joined the server. Welcome him.
    else:
        # A message was send by the user.
        msg = message.content.lower()
         
        if "/bloodbank-donors" in msg:
            val = fe.grab(msg)
            db.executemyorder(val)
            response = "These are the patients that have donated at least " + str(val) +" cc amount of blood and have insurance within the year:\n " + str(db.storage)

        if "milestone3" in msg:
            response = "I am alive. Signed: 'your bot'"
            
        if "/hospital-patients r no" in msg:
             response = "There are 2 patients that do not have insurance but is registered. " + "\nThey are: " + str(db.mylist) 

        if "/hospital-patients r yes" in msg:    
          response = "The 1 patient that has insurance and is registered is: " + str(db.myotherlist)  

        if "/hospital-receptions yes" in msg:
          response = "These are all the receptions that are also blood donors and have donated more than the requested amount of blood: " + str(db.receptions)  

        if "/patients-hospital" in msg:
            thedate = fe.grabdate(msg)
            val1 = fe.grabblood(msg)
            db.findBloodtype(val1)
            response = "These are the patients that have been a patient since " +thedate+ " and passed the exam with blood type " + val1 + ": " +str(db.listOfString)

        if "/bloodbank-born" in msg:
            val2 = fe.getyear(msg)
            val3 = fe.getbloodtype(msg)
            amount = fe.getamount(msg)
            db.rulefive(val2,val3)
            response = "These are the patients that are born after " + val2 + " with type " + val3.upper() + " blood type and have donated more than " + amount + " amount of blood: " + str(db.listofValues)
            
        if "/hospital-donor-exam" in msg:
          bloodamount = fe.getamount(msg)
          word = fe.passorfail(msg)
          db.ruleseven(bloodamount)
          response = "These are the donors that have " + word + " and have donated " + bloodamount + " cc of blood while being a patient: " +str(db.rulesevenstring)

        if "/hospital-walkin" in msg:
          val = fe.getwalkin(msg)
          db.rulesix(val)
          incentive = fe.getincentive(msg)
          response = "These are the patients that have recieved at least " + incentive + " and have a blood type of " + val.upper() + " that would be considered a walkin: " + str(db.rulesixstring)
            
    if response:
        # bot sends response to the Discord API and the response is show
        # on the channel from your Discord server that triggered this method.
        embed = discord.Embed(description=response)
        await message.channel.send(embed=embed)


try:
    # start the bot and keep the above methods listening for new events
    client.run(token)
except:
    print("Bot is offline because your secret environment variables are not set. Head to the left panel, " +
          "find the lock icon, and set your environment variables. For more details, read the README file in your " +
          "milestone 3 repository")

