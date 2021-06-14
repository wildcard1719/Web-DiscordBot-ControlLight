import discord
import serial
import threading
from flask import Flask, render_template, request

app = Flask(__name__)


ser = serial.Serial("/dev/ttyS0", "9600")

client = discord.Client()

light = ""
admin = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global light, admin, status
    

    if message.author == client.user:
        return
    if message.author.id == 536932662972252170:
        admin = 1
    else:
        admin = 0

    if message.content.startswith('#light') or message.content.startswith('l'):
        if "on" in message.content:
            if admin == 1:
                light = "1"
                ser.write(light.encode())
                await message.channel.send('Light ON')
            else:
                await message.channel.send('Nice try')
        elif "off" in message.content:
            if admin == 1:        
                light = "0"
                ser.write(light.encode())
                await message.channel.send('Light OFF')
            else:
                await message.channel.send('Nice try')

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/light")
def light():
    return render_template("light.html")

@app.route("/lighton")
def lighton():
    ser.write("1".encode())
    return render_template("light.html")

@app.route("/lightoff")
def lightoff():
    ser.write("0".encode())
    return render_template("light.html")
    



def run_flask():
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port="80")

t = threading.Thread(target=run_flask)
t.deamon = True
t.start()

with open("/root/Bot/KIPP-token.txt", 'r') as tokenfile:
    token = tokenfile.read()
    client.run(token)

