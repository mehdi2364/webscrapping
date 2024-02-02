import discord
from discord.ext import commands
import requests
import spacy
import nlp_city
import api
import utils
import api_city

base_url = "https://api.waqi.info"
token = '6a83904c5df3e83213e191b295adf644300bde37'

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

class EchoCog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    def search_quality_air(self,city,message):
        quality_air = api.get_quality_air(city)
        if quality_air != 1:
            response = f"The quality of air in {city} ({api_city.find_country(city)}) is {quality_air} ({utils.get_class_aqi(quality_air)})"
            return response
        else:
            return (f"Sorry {message.author} , i don't have the this information for {city}")
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user.name}')

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself
        print(message.author)
        if message.author == self.bot.user:
            return
        print(self.bot.user.mention)
        # Echo back the message content
        if self.bot.user.mention in message.content:
            if('/aqi:' in message.content):
                print('aqi command')
                city = utils.get_word_in_parenthesis(message.content)
                print(city)
                if(city == None):
                    await message.channel.send(f"{message.author} , Please enter the command correcly, i can't identify the city")
                else:
                    response = self.search_quality_air(city,message)
                    print(response)
                    await message.channel.send(response)




            elif(('quality' in message.content.lower() and 'air' in message.content.lower())):
                print("quality")
                recognized_cities = nlp_city.recognize_city(message.content)

                if(recognized_cities):
                    print("reconnu")
                    print(recognized_cities)
                    for city in recognized_cities:
                        response = self.search_quality_air(city,message)
                        print(response)
                        await message.channel.send(response)

                else :
                    response = f"Sorry {message.author} ,I see that you want to have the quality of air, but i didn't identify which city\nMaybe i can't read the city in your phrase\nTry with the enter the following command in the chat and replace 'city' with your city , let the parenthesis"
                    await message.channel.send(response)
                    response = ("/aqi:(city)")
                    await message.channel.send(response)


# Add the Cog to the bot
bot.add_cog(EchoCog(bot))


# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTE5NDcxMTk5MTk0ODk1MTYwMg.GcvG8X.zjAviuMZBzJz9lDPvxE-YUQw11TvOGBrrDFtzQ')
