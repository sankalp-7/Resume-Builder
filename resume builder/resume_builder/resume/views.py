from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from.forms import createuser
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.core.mail import EmailMessage
import smtplib
from email.message import EmailMessage
import imghdr
from PIL import Image, ImageDraw, ImageFont
import textwrap
import re
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    form=createuser()
    if request.method=='POST':
        form=createuser(request.POST)
        if form.is_valid():
            form.save()
        username=request.POST['email']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(user)
            login(request, user)
        # Redirect to a success page.
            
            return redirect('/builder')
    
    return render(request,'resume/home.html',{'form':form})
def builder(request):
    if request.method == "POST":
        global template_loc, tmp, img_h, data
        data = request.POST
        template_loc = 'static/ff.png'
        tmp = Image.open(template_loc)
        width, height = tmp.size
        draw = ImageDraw.Draw(tmp) 
        font = ImageFont.truetype(r'C:\Users\sanka\Downloads\FontsFree-Net-Lulo-Clean-W01-One.ttf', 100)
        img_h = font.getsize('I')[1]
        font2 = ImageFont.truetype(r'C:\Users\sanka\Downloads\FontsFree-Net-Lulo-Clean-W01-One.ttf', 50)
        font3 = ImageFont.truetype(r'C:\Users\sanka\Downloads\FontsFree-Net-Lulo-Clean-W01-One.ttf', 30)
        p_font=ImageFont.truetype(r'C:\Users\sanka\Downloads\Calibri.ttf',40)
        
        name=data['name']
        number=data['number']
        email=data['email']
        address=data['address']
        summary=data['summary']
        school1=data['school1']
        year1=data['year1']
        marks1=data['marks1']
        school2=data['school2']
        year2=data['year2']
        marks2=data['marks2']
        print(school1)
        text='WEB DEVELOPER'
        shape=[(220,655),(width-240,655)]
        shape1=[(220,455),(width-240,455)]
        contactline=[(880,755),(880,1210)]
        #HEADER
        draw.text(((width//2)-700, 200), name, fill ="black", font = font) 
        draw.line(shape, fill ="gray", width = 0)
        draw.text(((width//2)-360, 525), text, fill ="black", font = font2) 
        draw.line(shape1, fill ="gray", width = 0)
        # DRAWING CONTACT
        draw.text((100, 755), 'CONTACT', fill ="black", font = font2) 
        drawimg('static/phone1.png', 80, 895)
        draw.text((180, 905), number, fill ="gray", font = p_font) 
        drawimg('static/email1.png', 80, 965)
        draw.text((180, 975), email, fill ="gray", font = p_font) 
        drawimg('static/maps1.png', 80, 965+70)
        draw.text((180, 975+70), address, fill ="gray", font = p_font) 
        draw.line(contactline,fill="gray",width=0)
        # DRAWING AWARDS
        draw.text((1000, 755), 'AWARDS', fill ="black", font = font2) 
        awards = re.split("\*", data["awards"])
        yy=825
        for i in range(0,len(awards)):
            draw.text((1000, yy),awards[i],fill="gray",font=p_font)
            yy+=70
        #DRAWING EDUCATION
        draw.text((100, 1430), 'EDUCATION', fill ="black", font = font2) 
        draw.text((105,1550), school1, fill ="black", font = font3)
        draw.text((105,1650),year1,fill="gray",font=p_font)
        draw.text((105,1700),marks1+"%",fill="gray",font=p_font)
        draw.text((105,1800),school2,fill="black",font=font3)
        draw.text((105,1900),year2,fill="gray",font=p_font)
        draw.text((105,1950),marks2+"%",fill="gray",font=p_font)
        draw.line([(105,2180-120),(505,2180-120)],fill="gray",width=0)
        draw.line([(880,1430),(880,2930)],fill="gray",width=0)
        #DRAWING SKILLS
        draw.text((100, 2140), 'SKILLS', fill ="black", font = font2) 
        skill_list=re.split(',',data['skills'])
        y_text=2250
        for skill in skill_list:
            draw.text((85,y_text),'.',fill="black",font=p_font)
            draw.text((115,y_text),skill,fill="gray",font=p_font)
            y_text+=60
        #DRAWING PROJECTS
        draw.text((1000, 1430), 'PROJECTS', fill ="black", font = font2) 
        experience = re.split("\#|\*", data["experience"])
        print(experience)
        experience.pop(0)
        c=0
        y_text=1550
        for i in experience:
            c+=1
            if c%2==0:
                lines = textwrap.wrap(i, width=70)
                print(lines)
                for line in lines:
                    draw.text((1050,y_text),line,fill="gray",font=p_font)
                    y_text+=115
            else:

                draw.text((1000,y_text),i,fill="black",font=font3)
                y_text+=95
            
        # for i in range(0, len(experience)):
        #     xCrnt = 1000
        #     t = 15
        #     if i == 0:
        #         t += 125
        #     if (i % 2) != 0:  # Even
        #         if i == len(experience)-1:
        #             draw.text((xCrnt,1550+t),experience[i],fill="gray",font=p_font)
        #         else:
        #             draw.text((xCrnt,1550+t),experience[i],fill="gray",font=p_font)
        #     else:
        #         if i == len(experience)-1:
        #             draw.text((xCrnt,1550+t),experience[i],fill="gray",font=p_font)
        #         else:
        #             draw.text((xCrnt,1550+t),experience[i],fill="gray",font=p_font)

        tmp.show()
    obj=User.objects.all()
    return render(request,'resume/resume.html',{'obj':obj})
def drawimg(loc1, x, y):
    img = Image.open(loc1).resize((img_h - 48, img_h -48)).convert("L")
    tmp.paste(img, (x, y))
        