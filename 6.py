'''
© 2019SelfBot ProtectV3.1
'''

from DHENZA import *
from akad.ttypes import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from important import *
from random import randint
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
Bot_startTime = time.strftime("%H:%M:%S", time.localtime())
# Login line
print("""
\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Start Bot ]\033[0m    
"""%(Bot_startTime))
#==============================================================
cl = LINE("ldf56885@eoopy.com","mai065558mai")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Selfbot Login ]\033[0m"""%(Bot_startTime))

k1 = LINE("qii76359@bcaoo.com","mai065558mai")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist1 Login ]\033[0m"""%(Bot_startTime))

k2 = LINE("xvx65670@bcaoo.com","mai065558mai")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist2 Login ]\033[0m"""%(Bot_startTime))

k3 = LINE("axz83700@eoopy.com","mai065558mai")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist3 Login ]\033[0m"""%(Bot_startTime))

k4 = LINE("bsx99927@zzrgg.com","mai065558mai")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist4 Login ]\033[0m"""%(Bot_startTime))

k5 = LINE("gcu89366@zzrgg.com","mai065558mai")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist5 Login ]\033[0m"""%(Bot_startTime))

#==========================[[PAKE TOKEN CHROMEOS 2.1.5]]=========================
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m

	    Welcome To Self Bot Protect  By mai

            
Login Time %s \033[0m\n\n"""%(Bot_startTime))
#==============================================================================
oepoll = OEPoll(cl)
call = cl
creator = ["u7dd3b094df38ef9fa28d313f73455389"]
owner = ["u7dd3b094df38ef9fa28d313f73455389"]
admin = ["u7dd3b094df38ef9fa28d313f73455389"]
staff = ["u7dd3b094df38ef9fa28d313f73455389"]
#==============================================================================
lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid             
KAC = [k1,k2,k3,k4,k5]
ABC = [k1,k2,k3,k4,k5]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid]
Saint = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
#===============================================================================
welcome = []
targets = []
lower = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
protectname = []
botStart = time.time()
msgditerima = {}
unsendchat = {}
msgdikirim = {}
userTemp = {}
userKicked = []
dict = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
dhenzaqr = []
offbot = []
msg_image={}
msg_video={}
msg_sticker={}
detectUnsend = []
simisimi = []
tagmeOpen = codecs.open("tag.json","r","utf-8")
tagme = json.load(tagmeOpen)
#===============================================================================
responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName
#===============================================================================
settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",    
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 500,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "dhenza":{},
    "likeOn": True,
    "Timeline": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":20},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "unsend":True,
    "selfbot":True,
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "mention":"Masuk say ngitip bacok",
    "Respontag":"Cuy ngrtag mele..",
    "welcome":"Wellcome to my Fams",
    "comment":"ᴀᴜᴛᴏʟɪᴋᴇ ʙʏ: \n\n\n\n™S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ\n\n\n\nᴄʀᴇᴀᴛᴏʀ:\nhttp://line.me/ti/p/~mai06555mai",
    "message":"ᴄɪᴇᴇ ᴋᴇᴛᴀʜᴜᴀɴ ɴɢᴇ ᴀᴅᴅ\nᴍᴀᴋᴀsɪʜ ʏᴀ sᴜᴅᴀʜ ᴀᴅᴅ..\n\n\n\n\n™S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ\n\n\n\nᴄʀᴇᴀᴛᴏʀ:\nhttp://line.me/ti/p/~mai06555mai",
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

bl = {
    'blacklist':{}
    }

with open('bl.json', 'r') as fp:
    bl = json.load(fp)

rname = {
    "rname":"s"
}

sname = {
    "sname":"k"
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dzProfile = cl.getProfile()
myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]                   
       
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "✏DAFTAR JONES「{}」\n\n╔━━━━[ SILENT KILLER ]━━━\n╠❂➣✏1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠❂➣✏%i.  " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
        
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dhenza "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0) 

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Sempak Bot\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━\n"
    helpMessage += "│┃ " + "╭──⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟─\n"
    helpMessage += "│┃" + " ├───  ᴍᴇɴᴜ ʙᴏᴛ  ────────────────\n"
    helpMessage += "│┃" + " ├──────────────\n"
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴘ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "bk @\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍʏʙᴏᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "in\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "out\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜᴘʙᴏᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍɪᴅ @\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀʙᴏᴜᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴛɪᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʀᴇᴀᴛᴏʀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɢʟɪsᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "เปิดลิ้ง\n"
    num = (num+1)    
    helpMessage += "│╠❂➣ %i. " % num + key + "ปิดลิ้ง\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i ." % num + key + "ลิ้ง\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɢʀᴜᴘɪɴғᴏ ɴᴏ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "รายชื่อสตาฟ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "รายชื่อบอท\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʜᴀᴘᴜsᴄʜᴀᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sɪᴅᴇʀ ᴏɴ[ᴏғғ]\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "แทค\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜᴘɢʀᴜᴘ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʙᴄᴀsᴛ:「ᴛᴇxᴛ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴇᴛɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɴᴀᴍᴇ: ɴᴀᴍᴀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɴᴀᴍᴇ1/10: ɴᴀᴍᴀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʀᴇsᴇᴛɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "s:sɪᴅᴇʀ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴘᴇsᴀɴ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴡᴇʟᴄᴏᴍᴇ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sʀᴇsᴘᴏɴ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜᴘʙᴏᴛ 「ubah foto」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "1/10ᴜᴘ 「ubah foto」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄsɪᴅᴇʀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄᴘᴇsᴀɴ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʀᴇsᴘᴏɴ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄᴡᴇʟᴄᴏᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜɴsᴇɴᴅ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏʙʟᴏᴄᴋ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟᴀɢᴜ ᴊᴜᴅᴜʟ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴍᴜʟᴇ:「ʟɪɴᴋ」 \n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "!ɢᴏᴏɢʟᴇ ᴄᴀʀɪ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʏᴛᴍᴘ4: ᴄᴀʀɪ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʜᴀɴɢᴇᴅᴜᴀʟ \n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʜᴀɴɢᴇᴅᴜᴀʟʟɪɴᴋ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɪᴍɢ ғᴏᴏᴅ: ᴄᴀʀɪ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴘʀᴏғɪʟᴇsᴍᴜʟᴇ: ɪᴅ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + " ᴘʀᴏғɪʟᴇɪɢ: ɪᴅ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍᴇᴍᴇ@1@2@3\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴛᴀғsɪʀǫᴜʀᴀɴ ɴᴏ|ɴᴏ\n"
    num = (num+1)    
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅɪᴍɢ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟɪᴍɢ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛɪᴍɢ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅᴠɪᴅᴇᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟᴠɪᴅᴇᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛᴠɪᴅᴇᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅsᴛɪᴄᴋᴇʀ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟsᴛɪᴄᴋᴇʀ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛsᴛɪᴄᴋᴇʀ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅᴀᴜᴅɪᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟᴀᴜᴅɪᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛᴀᴜᴅɪᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)    
    helpMessage += "│┃ " + "├──────────────\n"
    helpMessage += "│┃ " + "╰──⍟ ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ⍟─────────\n"
    helpMessage += "╰━━━━━━━━━━━━━━━━"
    helpMessage += " Creator: https://line.me/ti/p/~mai06555mai \n"
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭━━━━━━━━━━━━━━━━\n"
    helpMessage2 += "│┃ " + "╭───⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟─\n"
    helpMessage2 += "│┃" + " ├─── ᴄᴏᴍᴍᴀɴᴅ ᴋɪᴄᴋᴇʀ ────────────\n"
    helpMessage2 += "│┃" + " ├──────────────\n"
    helpMessage2 += "│╠❂➣ %i. " % num + key + "gk @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "bk @ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴍᴀɪɴᴋᴀɴ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "เชิญ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙʟ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴʟɪsᴛ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ғʀᴇsʜ/ʀᴇғʀᴇsʜ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ɢᴀs \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴋɪʟʟʙᴀɴ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sᴘᴀᴍɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅʙᴏᴛ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴᴀʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴄʟᴇᴀʀʙᴀɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "แอดมิน ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ตั้งแอดมิน @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ลบแอดมิน @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "แอดมิน ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + " ᴏᴡɴᴇʀ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "สตาฟ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sᴛᴀғғᴅᴇʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ตั้งสตาฟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ลบสตาฟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴏᴛ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "บอทลบ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "บอทแอด @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴏᴛᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴᴅᴇʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴛᴀʟᴋʙᴀɴ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "s bl\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "s dbn\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i ." % num + key + "ᴛᴀʟᴋʙᴀɴᴅᴇʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴛᴀᴋʙᴀɴ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + " ᴛᴀʟᴋʙᴀɴᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴛᴀʟᴋʙᴀɴʟɪsᴛ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀʟʟᴘʀᴏ ᴏɴ/ᴏғғ\n"
    num = (num+1)    
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛǫʀ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴜʀʟ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴊs ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙʏᴇ1/10\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʟᴇᴀᴠᴇɢʀᴜᴘ「ɴᴏ」\n"
    num = (num+1)    
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴋɪᴄᴋᴇʀ「ɪɴ」\n"
    num = (num+1)  
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴋɪᴄᴋᴇʀ「ʟᴠ」\n"
    num = (num+1)    
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ɪɴғᴏɢʀᴜᴘ「ɴᴏ」\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ɪɴғᴏᴍᴇᴍʙᴇʀ「ɴᴏ」\n"
    num = (num+1)     
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sɪʟᴇɴᴛᴋɪʟʟᴇʀ [ᴋɪᴄᴋᴀʟʟ]\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴜʙᴀʀ [ᴋɪᴄᴋᴀʟʟ]\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sɪʟᴇɴᴛ1/2 \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏʙʟᴏᴋ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│┃ " + "├──────────────\n"
    helpMessage2 += "│┃ " + "╰──⍟ ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ⍟────────\n"
    helpMessage2 += "╰━━━━━━━━━━━━━━━━"
    helpMessage2 += " My ID LINE : 〘 https://line.me/ti/p/~mai06555mai 〙\n"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.kickoutFromGroup(op.param1, [op.param2])
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if k1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k1.reissueGroupTicket(op.param1)
                                X = k1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                k1.kickoutFromGroup(op.param1, [op.param2])
                                k1.updateGroup(X)
                                k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k2.reissueGroupTicket(op.param1)
                                    X = k2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    k2.kickoutFromGroup(op.param1, [op.param2])
                                    k2.updateGroup(X)
                                    k2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k3.reissueGroupTicket(op.param1)
                                        X = k3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        k3.kickoutFromGroup(op.param1, [op.param2])
                                        k3.updateGroup(X)
                                        k3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k4.reissueGroupTicket(op.param1)
                                            X = k4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            k4.kickoutFromGroup(op.param1, [op.param2])
                                            k4.updateGroup(X)
                                            k4.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                k5.reissueGroupTicket(op.param1)
                                                X = k5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                k5.kickoutFromGroup(op.param1, [op.param2])
                                                k5.updateGroup(X)
                                                k5.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
#====================================================================                          
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)      
#====================================================================                          
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            cl.cancelGroupInvitation(op.param1,[taged])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Amid in op.param3:
                G = k1.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k1.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k1.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k1.cancelGroupInvitation(op.param1,[taged])
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Bmid in op.param3:
                G = k2.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k2.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k2.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k2.cancelGroupInvitation(op.param1,[taged])
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Cmid in op.param3:
                G = k3.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k3.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k3.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k3.cancelGroupInvitation(op.param1,[taged])
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Dmid in op.param3:
                G = k4.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k4.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k4.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k4.cancelGroupInvitation(op.param1,[taged])
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Emid in op.param3:
                G = k5.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k5.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        ke.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k5.cancelGroupInvitation(op.param1,[taged])
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass

        if op.type == 13:
            if op.param3 in bl['blacklist'] and op.param2 in bl['blacklist'] and op.param2 not in Bots and op.param2 not in Saint and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                bl['blacklist'][op.param2] = True
                with open('bl.json', 'w') as fp:
                    json.dump(bl, fp, sort_keys=True, indent=4)
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k1.cancelGroupInvitation(op.param1,[op.param3])
                                k1.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k2.cancelGroupInvitation(op.param1,[op.param3])
                                    k2.kickoutFromGroup(op.param1, [op.param2])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k3.cancelGroupInvitation(op.param1,[op.param3])
                                        k3.kickoutFromGroup(op.param1, [op.param2])
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k4.cancelGroupInvitation(op.param1,[op.param3])
                                            k4.kickoutFromGroup(op.param1, [op.param2])
                                    except:
                                        try:
                                            if op.param3 not in bl["blacklist"]:
                                                k5.cancelGroupInvitation(op.param1,[op.param3])
                                                k5.kickoutFromGroup(op.param1, [op.param2])
                                        except:
                                            pass
                return                     
#====================================================================       
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        group = k1.getGroup(op.param1)
                        inv1 = op.param3.replace('\x1e',',')
                        inv2 = inv1.split(',')
                        for target in inv2:
                            k1.cancelGroupInvitation(op.param1, [target])
                            k1.kickoutFromGroup(op.param1, [op.param2])
                            bl["blacklist"][op.param2] = True
                    except:
                        try:
                            group = k2.getGroup(op.param1)
                            inv1 = op.param3.replace('\x1e',',')
                            inv2 = inv1.split(',')
                            for target in inv2:
                                k2.cancelGroupInvitation(op.param1, [target])
                                k2.kickoutFromGroup(op.param1, [op.param2])
                                bl["blacklist"][op.param2] = True
                        except:
                            try:
                                group = k3.getGroup(op.param1)
                                inv1 = op.param3.replace('\x1e',',')
                                inv2 = inv1.split(',')
                                for target in inv2:
                                    k3.cancelGroupInvitation(op.param1, [target])
                                    k3.kickoutFromGroup(op.param1, [op.param2])
                                    bl["blacklist"][op.param2] = True
                            except:
                                try:
                                    group = k4.getGroup(op.param1)
                                    inv1 = op.param3.replace('\x1e',',')
                                    inv2 = inv1.split(',')
                                    for target in inv2:
                                        k4.cancelGroupInvitation(op.param1, [target])
                                        k4.kickoutFromGroup(op.param1, [op.param2])
                                        bl["blacklist"][op.param2] = True
                                except:
                                    try:
                                        group = k5.getGroup(op.param1)
                                        inv1 = op.param3.replace('\x1e',',')
                                        inv2 = inv1.split(',')
                                        for target in inv2:
                                            k5.cancelGroupInvitation(op.param1, [target])
                                            k5.kickoutFromGroup(op.param1, [op.param2])
                                            bl["blacklist"][op.param2] = True
                                    except:
                                        pass       
       
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in bl["blacklist"]:
                        	k1.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                                                                
                return
                                        
        if op.type == 17:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in bl["blacklist"]:
                        	k1.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                                                                
                return                                                                         
#====================================================================  
        if op.type == 11:
            if op.param2 in bl['blacklist']:
                    try:
                        k1.reissueGroupTicket(op.param1) 
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.reissueGroupTicket(op.param1) 
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.reissueGroupTicket(op.param1) 
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.reissueGroupTicket(op.param1) 
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.reissueGroupTicket(op.param1) 
                                    except:
                                        pass
                 
#====================================================================                                                                                                                 
#====================================================================                            
        if op.type == 17:
            if op.param2 in bl['blacklist']:                
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                                                                
                
#====================================================================
        if op.type == 19:
            if op.param2 in bl['blacklist']:            
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                                                                
#====================================================================
            if op.param1 in protectantijs:
                if g2MID in op.param3:
                    if op.param2 not in Bots and op.param2 not in Saint and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bl["blacklist"][op.param2] = True
                        try:
                            g1.inviteIntoGroup(op.param1,[g1MID])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.inviteIntoGroup(op.param1,[g2MID])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                               
            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            bl["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            bl["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            bl["blacklist"][op.param2] = True              
            except:
                pass
#==================================================================== 
        if op.type == 13:
            if op.param3 in bl["blacklist"]:
                    try:
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        pass

        if op.type == 17:
            if op.param2 in bl["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
             
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])        

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in bl["blacklist"]:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                            k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)									
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                k2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                    k3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                        k4.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)											
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                            k5.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass             
                return        
#====================================================================                  
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            group = cl.getGroup(op.param1)
                                            group.preventedJoinByTicket = False
                                            cl.updateGroup(group)
                                            invsend = 0
                                            Ticket = cl.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass 
                return
                                                                                                                    
        if op.type == 19:
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        group = k1.getGroup(op.param1)
                                        group.preventedJoinByTicket = False
                                        k1.updateGroup(group)
                                        invsend = 0
                                        Ticket = k1.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass 
                return
                                                                                                                    
        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                                k5.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                    k2.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        group = k2.getGroup(op.param1)
                                        group.preventedJoinByTicket = False
                                        k2.updateGroup(group)
                                        invsend = 0
                                        Ticket = k2.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
                                                                                                                    
        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                    k3.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        group = k3.getGroup(op.param1)
                                        group.preventedJoinByTicket = False
                                        k3.updateGroup(group)
                                        invsend = 0
                                        Ticket = k3.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
                                                                                                                    
        if op.type == 19:
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k5.kickoutFromGroup(op.param1,[op.param2])
                        k5.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                    k4.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        group = k4.getGroup(op.param1)
                                        group.preventedJoinByTicket = False
                                        k4.updateGroup(group)
                                        invsend = 0
                                        Ticket = k4.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
                                                                                                                    
        if op.type == 19:
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    k5.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        group = k5.getGroup(op.param1)
                                        group.preventedJoinByTicket = False
                                        k5.updateGroup(group)
                                        invsend = 0
                                        Ticket = k5.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
        if op.type == 19:
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            group = cl.getGroup(op.param1)
                                            group.preventedJoinByTicket = False
                                            cl.updateGroup(group)
                                            invsend = 0
                                            Ticket = cl.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
#===================================================================================================                  
                return

        if op.type == 55:
            if op.param3 in bl['blacklist'] and op.param2 in bl['blacklist'] and op.param2 not in Bots and op.param2 not in admin:
                try:
                    k1.cancelGroupInvitation(op.param1,[op.param3])
                except:
                    try:
                        k2.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        try:
                            k3.cancelGroupInvitation(op.param1,[op.param3])
                        except:
                            try:
                                k4.cancelGroupInvitation(op.param1,[op.param3])
                            except:
                                try:
                                    k5.cancelGroupInvitation(op.param1,[op.param3])
                                except:
                                    pass         
#===================================================================================================                      
        if op.type == 55:
            if op.param2 in bl["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 55:
            if op.param2 in bl["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                G = cl.getGroup(op.param1)	
                G.preventedJoinByTicket = True		
                random.choice(ABC).updateGroup(G)	
                random.choice(ABC).sendMessage(op.param1,"ติดดำถาวร กรุนาทักแอดมินบอท")					
                random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)														
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)
                        cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)
            
        if op.type == 26:
           if bl["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in bl["blacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if bl["talkban"] == True:
                   if msg._from in bl["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["yg nge tag semoga masuk surga amin"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "No tag me....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
                           
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
                         
#=======================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots&media         	   
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker respon hasben changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")
                            
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
                         
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
                         
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
                         
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
                         
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
                               
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Nothing in bot")
#SC ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Succes add to staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes expel to staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Nothing in staff")
#SC ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Succes Add to Admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes to expel admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#SC ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in blacklist")
#SC TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in Talkban")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Bot on")
                                
                        elif cmd == "off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Bot off")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)                                
                                md = "│[ MAI ] \n"                                
                                if wait["sticker"] == True: md+="│╠══[  ON  ] sᴛɪᴄᴋᴇʀ✔️\n"
                                else: md+="│[ OFF ] sᴛɪᴄᴋᴇʀ❌\n"
                                if wait["contact"] == True: md+="│╠══[  ON  ] ᴄᴏɴᴛᴀᴄᴛ✔️\n"
                                else: md+="│[ OFF ] ᴄᴏɴᴛᴀᴄᴛ❌\n"
                                if wait["detectMention"] == True: md+="│╠══[  ON  ] ʀᴇsᴘᴏɴ✔️\n"
                                else: md+="│[ OFF ] ʀᴇsᴘᴏɴ❌\n"
                                if wait["autoJoin"] == True: md+="│╠══[  ON  ] ᴀᴜᴛᴏᴊᴏɪɴ✔️\n"
                                else: md+="│[ OFF ] ᴀᴜᴛᴏᴊᴏɪɴ❌\n"
                                if settings["autoJoinTicket"] == True: md+="│╠══[  ON  ] ᴊᴏɪɴᴛɪᴄᴋᴇᴛ✔️\n"
                                else: md+="│[ OFF ] ᴊᴏɪɴᴛɪᴄᴋᴇᴛ❌\n"
                                if settings["unsendMessage"] == True: md+="│╠══[  ON  ] ᴜɴsᴇɴᴅ✔️\n"
                                else: md+="│[ OFF ] ᴜɴsᴇɴᴅ❌\n"
                                if wait["autoAdd"] == True: md+="│╠══[  ON  ] ᴀᴜᴛᴏᴀᴅᴅ✔️\n"
                                else: md+="│[ OFF ] ᴀᴜᴛᴏᴀᴅᴅ❌\n"
                                if msg.to in welcome: md+="│╠══[  ON  ] ᴡᴇʟᴄᴏᴍᴇ✔️\n"
                                else: md+="│[ OFF ] ᴡᴇʟᴄᴏᴍᴇ❌\n"
                                if wait["autoLeave"] == True: md+="│╠══[  ON  ] ᴀᴜᴛᴏʟᴇᴀᴠᴇ✔️\n"
                                else: md+="│[ OFF ] ᴀᴜᴛᴏʟᴇᴀᴠᴇ❌\n"
                                if msg.to in ghost: md+="│╠══[  ON  ] ɢʜᴏsᴛ✔️\n"
                                else: md+="│[ OFF ] ɢʜᴏsᴛ❌\n"
                                if msg.to in protectqr: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛǫʀ✔️\n"
                                else: md+="│[ OFF ] ᴘʀᴏᴛᴇᴄᴛǫʀ❌\n"
                                if msg.to in protectjoin: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ✔️\n"
                                else: md+="│[ OFF ] ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ❌\n"
                                if msg.to in protectkick: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ✔️\n"
                                else: md+="│[ OFF ] ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ❌\n"
                                if msg.to in protectinvite: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛɪɴᴠɪᴛᴇ✔️\n"
                                else: md+="│[ OFF ] ᴘʀᴏᴛᴇᴄᴛɪɴᴠɪᴛᴇ❌\n"
                                if msg.to in protectantijs: md+="│╠══[  ON  ] ᴊs✔️\n"
                                else: md+="│[ OFF ] ᴊs❌\n"                                
                                if msg.to in protectcancel: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ✔️\n"
                                else: md+="│[ OFF ] ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ❌\n"
                                md+= "│[ MAI ]"
                                cl.sendMessage(msg.to, md+"\n│ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│ᴊᴀᴍ  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")   
                                                                 
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                cl.sendMessage(msg.to,"Creator Kami")
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "me" or text.lower() == 'คท':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:                                           
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                                path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                                image = 'http://dl.profile.line.naver.jp'+path
                                cl.sendImageWithURL(msg.to, image)
                                
                        elif cmd == "มี":                       	
                    	    if msg._from in owner or msg._from in admin or msg._from in staff: 
                              contact = cl.getContact(sender)
                              image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                              cl.sendMessage(msg.to, "Nama : "+str(contact.displayName))
                              cl.sendMessage(msg.to, None,contentMetadata={'mid': sender}, contentType=13)
                                                                                                     
                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                                
                        elif cmd  == "mybot":
                          if msg._from in admin:
                              cl.sendContact(to, Amid)
                              cl.sendContact(to, Bmid)
                              cl.sendContact(to, Cmid)
                              cl.sendContact(to, Dmid)
                              cl.sendContact(to, Emid)
                              
                        elif cmd  == "midbot":
                          if msg._from in admin:
                              k1.sendMessage(msg.to,Amid)
                              k2.sendMessage(msg.to,Bmid)
                              k3.sendMessage(msg.to,Cmid)                            
                              k4.sendMessage(msg.to,Dmid)
                              k5.sendMessage(msg.to,Emid)       

                        elif cmd == "speedbot" or cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(to, "Speed...🏁")
                               elapsed_time = time.time() - start
                               k1.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k2.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k3.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k4.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k5.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")  

                        elif cmd == "sb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k1.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k2.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k3.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k4.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k5.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                              
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)                                      
                                  cl.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))                              
                              else:
                                  cl.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  
                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)                                  
                                   cl.sendMessage(msg.to,"Chat sudah d bersihkan 👍")                                  
                               except:
                                   pass

                        elif cmd.startswith("พิม: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               saya = k1.getGroupIdsJoined()
                               saya = k2.getGroupIdsJoined()
                               saya = k3.getGroupIdsJoined()
                               saya = k4.getGroupIdsJoined()
                               saya = k5.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"\n" + str(pesan))
                                   k1.sendMessage(group,"\n" + str(pesan))
                                   k2.sendMessage(group,"\n" + str(pesan))
                                   k3.sendMessage(group,"\n" + str(pesan))
                                   k4.sendMessage(group,"\n" + str(pesan))
                                   k5.sendMessage(group,"\n" + str(pesan))

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               cl.sendMessage(msg.to, "🔴 Sname \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("ชื่อ "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Succes change Sname")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "🔴Sname change \n\nSname succes change to {}".format(str(key).lower()))

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "Succes Reset Sname ")

                        elif cmd == "รี5":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "please wait")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Done...")
                            
                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)

                        elif cmd == "รายชื่อเพื่อน":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"🔰ʟɪsᴛ ᴛᴇᴍᴀɴ🔰\n\n"+ma+"\ᴛᴏᴛᴀʟ"+str(len(gid))+"ᴛᴇᴍᴀɴ")

                        elif cmd == "รายชื่อกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"🔰ɢʀᴜᴘʟɪsᴛ 🔰\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "ปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "เปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(x.name)+ "\nᴜʀʟ ɢʀᴜᴘ: : http://line.me/R/ti/g/"+gurl)
#================BOT UPDATE NAME============#
                        elif cmd.startswith("ชื่อ: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ1: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ2: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ3: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ4: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("ชื่อ5: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == 'แทค':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "รายชื่อบอท":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰ʙᴏᴛʟɪsᴛ🔰\n\n\n"+ma+"\n%s ʙᴏᴛs" %(str(len(Bots))))
                   
                        elif cmd == "รายชื่อแอด":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰ᴀᴅᴍɪɴʟɪsᴛ🔰\n\n🔰ᴏᴡɴᴇʀ\n"+ma+"\n🔰ᴀᴅᴍɪɴ\n"+mb+"\n🔰sᴛᴀғғ:\n"+mc+"\n%s 🔰ᴀᴅᴍɪɴʟɪsᴛ🔰" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "set2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                mg = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                g = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectantijs
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = ghost
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"⛎ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ⛎\n\n🔒ᴘʀᴏᴛᴇᴄᴛ ǫʀ:\n"+ma+"\n🔒ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ:\n"+mb+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴀɴᴛɪᴋɪᴄᴋᴇʀ:\n"+mc+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ:\n"+md+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ:\n"+me+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ:\n"+mf+"\n🔒ɢʜᴏsᴛ:\n"+mg+"\n\n⛎ᴘʀᴏᴛᴇᴄᴛ ʟɪsᴛ %s ɢʀᴏᴜᴘ⛎" %(str(len(protectqr)+len(protectinvite)+len(protectantijs)+len(protectcancel)+len(protectkick)+len(protectjoin)+len(ghost))))
                                
                        elif cmd == "b":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                k1.sendMessage(msg.to,responsename1)
                                k2.sendMessage(msg.to,responsename2)
                                k3.sendMessage(msg.to,responsename3)
                                k4.sendMessage(msg.to,responsename4)
                                k5.sendMessage(msg.to,responsename5)
                                
                                             
                        elif cmd == "in":
                         if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0                        
                               ticket = cl.reissueGroupTicket(to)
                               k1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k2.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k3.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k4.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k5.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                        
                        elif cmd == "iv":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    k1.acceptGroupInvitation(msg.to)
                                    k2.acceptGroupInvitation(msg.to)
                                    k3.acceptGroupInvitation(msg.to)
                                    k4.acceptGroupInvitation(msg.to)
                                    k5.acceptGroupInvitation(msg.to)
                                except:
                                    pass       
                               
                        elif cmd == "bb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               k1.sendMessage(msg.to, "۞❂✪ อยู่ค่ะเจ้านาย.. ⋮➲➤")
                               k2.sendMessage(msg.to, "۞❂✪ อยู่ค่ะเจ้านาย.. ⋮➲➤")
                               k3.sendMessage(msg.to, "۞❂✪ อยู่ค่ะเจ้านาย.. ⋮➲➤")
                               k4.sendMessage(msg.to, "۞❂✪ อยู่ค่ะเจ้านาย.. ⋮➲➤")
                               k5.sendMessage(msg.to, "۞❂✪ อยู่ค่ะเจ้านาย.. ⋮➲➤")
                                
                        elif cmd == "out":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                               k1.leaveGroup(msg.to)
                               k2.leaveGroup(msg.to)
                               k3.leaveGroup(msg.to)
                               k4.leaveGroup(msg.to)
                               k5.leaveGroup(msg.to)
#====================================================================                            
                        elif cmd == "tim":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "тιмe reѕpon\n\n geт proғιle\n   %.10f\n geт conтacт\n   %.10f\n geт groυp\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()                               
                               cl.sendMessage(msg.to, "ѕpeed....")                               
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{}".format(str(elapsed_time)))
#===========add img============# 
                        elif cmd == "รูปกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"ส่งรูปมาค่ะ...")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("addsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessaget(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                cl.sendMessaget(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             cl.sendMessage(to, ret_) 
#=========== [ Add Audio] ============#
                     
                        elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(sender), str(result), 'Auto Like by dhenza')
                                    cl.sendMessage(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "Clone Profile \nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "Restore Profile \nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif 'Protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                                    
                        elif 'Pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)
                                  if msg.to in protectantijs:
                                      msgs = ""
                                  else:
                                      protectantijs.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protecttion sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection sudah dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)       
#===========KICKOUT============#       
                        elif ("Bk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                                      
                        elif text.lower() == 'เตะดำ':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    cl.sendMessage(to, "ʙᴏᴛs ʟɪᴍɪᴛ ")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                      
                        elif "ดึง " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass
#===========ADMIN ADD============
                        elif ("ตั้งสตาฟ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Bot " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ʙᴏᴛ")
                                       except:
                                           pass

                        elif ("ตั้งแอดมิน " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ admin")
                                       except:
                                           pass

                        elif ("ลบแอดมิน " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"❃ѕuccєєdєd menghapus admin")
                                       except:
                                           pass

                        elif ("ลบสตาฟ " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("บอทลบ " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ʙᴏᴛs")
                                       except:
                                           pass
#====================================#
                        elif cmd == "แอดมิน on" or text.lower() == 'admin:on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact")

                        elif cmd == "admindell" or text.lower() == 'adminexpl:on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "สตาฟ on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staffdell" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "botdell" or text.lower() == 'botexpl:on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"Loading...")
                                cl.sendMessage(msg.to,"Refresh done...")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)                                            
#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'join on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'join off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'add on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'add off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'มุดลิ้ง on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Auto Join Ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'มุดลิ้ง off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Auto join Ticket dinonaktifkan")
                                
                        elif cmd == "unsend on" or text.lower() == 'ud on':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = True
                                cl.sendMessage(msg.to,"detect unsend diaktifkan")

                        elif cmd == "unsend off" or text.lower() == 'ud off':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = False
                                cl.sendMessage(msg.to,"detect unsend dinonaktifkan")
             
                        elif cmd == "timeline on" or text.lower() == 'ไล on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                cl.sendMessage(msg.to,"detect timeline on")

                        elif cmd == "timeline off" or text.lower() == 'ไล off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                cl.sendMessage(msg.to,"detect timleline off ")
#===========COMMAND BLACKLIST============#
                        elif cmd == "banall":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                                                
                        elif cmd == "bandell":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"Limit bosku")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendMessage(msg.to,"Sucsess clear banned")
                                            except:
                                                pass
                        elif ("ดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           bl["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("ขาว " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del bl["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "talbandell" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif ("ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           bl["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("bandell " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del bl["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "bandell" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")


                        elif cmd == "blc" or text.lower() == 'ดำ':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if bl["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"คนที่ติดดำ")
                              else:
                                    ma = ""
                                    for i in bl["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'ล้างดำ':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              bl["blacklist"] = {}
                              ragets = cl.getContacts(bl["blacklist"])
                              mc = "「%i」Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"ลบบัญชีดำแล้วค่ะ" +mc)
                              
                        elif cmd == "Bc" or text.lower() == 'bc':
                          if wait["selfbot"] == True:
                            if sender in admin:
                              if bl['blacklist'] == {}:
                                cl.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                num = 0
                                mc = []
                                for m_id in bl['blacklist']:
                                    mc.append(m_id)
                                cban = cl.getContacts(mc)
                                nban = []
                                for x in range(len(cban)):
                                    nban.append("%i - "%num+cban[x].displayName)
                                    num = (num+1)
                                bn = "\n".join(str(i)for i in nban)
                                cl.sendMessage(msg.to, "User Blacklist: \n\n" + bn + "\n")
                                print ("Cek blacklist")

                        elif cmd == "cb" or text.lower() == 'Cb':
                          if wait["selfbot"] == True:
                            if sender in admin:
                              cl.sendMessage(msg.to,"{} blacklist cleared.".format(str(len(bl['blacklist']))))
                              bl['blacklist'] = {}
                              with open('bl.json', 'w') as fp:
                                  json.dump(bl, fp, sort_keys=True, indent=4)
#===========COMMAND SET============#
                        elif msg.contentType == 16:
                           if wait["Timeline"] == True:
                              msg.contentType = 0
                              msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                              random.choice(ABC).sendMessage(msg.to, "like done")
                        
                        elif cmd == "ck":
                            if msg._from in admin or msg._from in owner:
                               try:k1.inviteIntoGroup(to, [Amid]);has = "OK"
                               except:has = "NOT"
                               try:k1.kickoutFromGroup(to, [Amid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               k1.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))                               
                               try:k2.inviteIntoGroup(to, [Bmid]);has = "OK"
                               except:has = "NOT"
                               try:k2.kickoutFromGroup(to, [Bmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               k2.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:k3.inviteIntoGroup(to, [Cmid]);has = "OK"
                               except:has = "NOT"
                               try:k3.kickoutFromGroup(to, [Cmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               k3.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:k4.inviteIntoGroup(to, [Dmid]);has = "OK"
                               except:has = "NOT"
                               try:k4.kickoutFromGroup(to, [Dmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               k4.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:k5.inviteIntoGroup(to, [Emid]);has = "OK"
                               except:has = "NOT"
                               try:k5.kickoutFromGroup(to, [Emid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               k5.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))                                               
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "มุดแล้วค่ะ : %s" % str(group.name))
                                     group1 = cl.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k1.findGroupByTicket(ticket_id)
                                     k1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k1.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = k1.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k2.findGroupByTicket(ticket_id)
                                     k2.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k2.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = k2.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k3.findGroupByTicket(ticket_id)
                                     k3.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k3.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = k3.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k4.findGroupByTicket(ticket_id)
                                     k4.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k4.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = k4.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k5.findGroupByTicket(ticket_id)
                                     k5.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k5.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = k5.findGroupByTicket(ticket_id)

    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
