import requests

class Player_not_registered:
    def __init__(self, bot, ctx, arg):
        self.bot = bot
        self.ctx = ctx
        self.arg = arg
    
    async def commandCheck(self):
        if self.arg is None:
            await self.ctx.send('Event id required !')
            return
        else:
            # Returns all registered users to the targeted event.
            r = requests.get('https://raid-helper.dev/api/v2/events/' + self.arg)
            content = r.json()
            # Get and store all user id for the targeted event
            eventUserId = list()
            for item in content['signUps']:
                eventUserId.append(int(item['userId']))

            # Get user id with GM/Officier/Membre role
            membersId = list()
            for user in self.ctx.guild.members:
                for role in user.roles:
                    if role.id in [861243034343964712, 861242852573839360, 1016385635512221889]: # Roles : GM's - Officiers - Membre
                        membersId.append(user.id)
                        break
            
            # print('Users id with gm/officier/membre role :')
            # print(membersId)

            # print('Registered users id')
            # print(eventUserId)

            # List of players not register for the event
            missingUser = [i for i in membersId if i not in eventUserId]
            missingUserName = ''
            for missingUserId in missingUser:
                missingUserName += '@' + self.bot.get_user(missingUserId).name + '#' + self.bot.get_user(missingUserId).discriminator + ' '

            # Send private message to the user who user the command
            # await self.ctx.message.author.send('Liste des joueurs qui ne sont pas inscrits à l\'événement du ' + content['date'] + ' dans le channel #' + content['channelName'])
            # await self.ctx.message.author.send(missingUserName)

            # Mention all missing users
            if not missingUser:
                await self.ctx.send('Tous les joueurs sont inscrits !')
            else:
                # msg = ""
                # for user in missingUser:
                #     msg += "".join("<@"+str(user)+"> ")
                # await self.ctx.send(msg)
                # await self.ctx.send("Merci de vous inscrire à l'événement du " + content['date'])
                await self.ctx.message.author.send('Liste des joueurs qui ne sont pas inscrits à l\'événement du ' + content['date'] + ' dans le channel #' + content['channelName'])
                await self.ctx.message.author.send(missingUserName)