import discord
from discord.ext import commands
import random
import string
import os
import requests
import time


from model import get_class
from settings import settings

cevre = ""
cevre_sozluk = (os.listdir('ZanoBot2\cevre_img'))


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim

intents.message_content = True

# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Kaliteye hoş geldiniz...')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642')

@bot.command()
async def spotify(ctx):
    await ctx.send(f'https://open.spotify.com/playlist/2iBNDKyTDyV5o5YdvQ9MOy?si=bc4403ea7db54904')




@bot.command()
async def yardım(ctx):
    await ctx.send("**Zano 2 | Komutlar**\n\n**$environment:** Çevreyi kirleten ürünlerden kaçınma rehberidir.\n**$spotify:** Dünyanın en iyi Spotify oynatma listesinin linkini atar.\n**$parola:** Rastgele, 10 haneli, karışık bir parola üretmenizi sağlar.\n**$yazıtura:** Yazı-Tura atmanızı sağlar.\n**$spam:** Bu komutu yazdıktan sonra boşluk bırakarak mesajın kaç kere tekrarlanacağını yazınız, bunun ardından tekrardan boşluk bırakak tekrarlanacak mesajın içeriğini **boşluksuz olarak** yazınız. https://prnt.sc/b0VJzY-IrfaG\n**$emoji:** Sohbete rastgele bir emoji atar.\n**$şarkı:** _Yakında Sizinle_")

@bot.command()
async def spam(ctx, times: int, content='repeating...'):
    """$spam x (mesaj içeriği) yazdığınızda mesajın x kere tekrarlanmasını sağlar"""
    for i in range(times):
        await ctx.send(content + " " + str(i + 1))
    await ctx.send(content + (" ") + "spamlaması bitti!")



@bot.command()
async def random_mem(ctx):
    mem = ""
    mem_sozluk = (os.listdir('ZanoBot2\images'))
    mem = random.choice(mem_sozluk)
    with open(f'ZanoBot2\images\{mem}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        mem = discord.File(f)
    await ctx.send(file=mem)

@bot.command()
async def kedi(ctx):
    nadirlik = random.randint(1, 4)
    print(nadirlik)
    kedimem = ""

    if nadirlik == 1 or nadirlik == 2:
        kedimem = ""
        with open(f'ZanoBot2\kedi_mem_img/beforecoffeee.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            resim = discord.File(f)
            
            await ctx.send(file=resim)

    elif nadirlik == 3 or nadirlik == 4:
        kedimem = ""
        kedimem_sozluk = (os.listdir('ZanoBot2\kedi_mem_img'))
        kedimem = random.choice(kedimem_sozluk)
        with open(f'ZanoBot2\kedi_mem_img\{kedimem}', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            kedimem = discord.File(f)
    
        await ctx.send(file=kedimem)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('köpke')
async def köpke(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)


@bot.command()
async def upload_image(ctx):
    attachments = ctx.message.attachments
    if attachments:
        #print(files)
        for attachment in attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
        await ctx.send("Dosya yükledin!")
        
        await ctx.send(get_class("DiscordAI\keras_model.h5", "DiscordAI\labels.txt", file_path))

    else:
        await ctx.send("Dosya yüklemedin!")

bot.run(settings["TOKEN"])