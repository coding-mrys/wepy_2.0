import webbrowser
from PIL import Image
import math

#create files / clear files
html = open("index.html","w")
css = open("style.css","w")
js = open("script.js","w")

#use files
html = open("index.html","a")
css = open("style.css","a")
js = open("script.js","a")

#write token
html.write("<!-- CODE BY WEPY -->\n<link rel='stylesheet' href='style.css'>")

#font family
css.write("\nbody{font-family:arial;}")

#create topic
def topic(text,id,color,size):
    html.write("\n<h1 id='"+str(id)+"'>"+str(text)+"</h1>")
    css.write("\n#"+str(id)+"{font-size:"+str(size)+"px;\ncolor:"+color+";}")

#create text
def text(text,id,color,size):
    html.write("\n<p id='"+str(id)+"'>"+str(text)+"</p>")
    css.write("\n#"+str(id)+"{font-size:"+str(size)+"px;\ncolor:"+color+";}")

#set alignment
def alingment(alingment):
    css.write("\nbody{text-align:"+alingment+";}")

#open file
def open():
    webbrowser.open("index.html")

#set background
def background(background):
    bg = background 
    img = False
    for i in range(len(bg)):
        if bg[i] == ".":
            img = True
    if img:
        css.write("\nbody{background-image:url("+background+");}")
    else:
        css.write("\nbody{background-color:"+background+";}")

#create chart
class chart:
    #create pillar chart
    def pillar_chart(x,y,id,color,backgroundcolor,size,pillarsize):

        high_y = 0
        for j in range(len(y)-1):
            if y[j] >= y[j+1]:
                high_y=y[j]

        y1 = high_y
        y2 = (high_y/2)+((high_y/2)/2)
        y3 = high_y/2
        y4 = ((high_y/2)/2)
        y5 = 0

        html.write("\n<table id='box_"+str(id)+
        "' border=1>\n<tr>\n<td>\n<p class='"+str(id)+
        "_pillar_y'>"+str(y1)+"</p>\n<p class='"+str(id)+
        "_pillar_y'>"+str(y2)+"</p>\n<p class='"+str(id)+
        "_pillar_y'>"+str(y3)+"\n<p class='"+str(id)+
        "_pillar_y'>"+str(y4)+"\n<p class='"+str(id)+
        "_pillar_y'>"+str(y5)+
        "</p>\n</td>\n<td id='"+str(id)+"_chart_in'>\n<b id='"+
        str(id)+"_pillar_chart'>")

        for i in range(len(x)):
            html.write("\n<b class='"+str(id)+"_pillar' id='"+
            str(id)+"_"+str(i)+"'></b>")

            css.write("\n#"+str(id)+"_"+str(i)+"{width:"+
            str(pillarsize)+"px;height:"+str(y[i])+"px;}")

        html.write("\n</b>\n</td>\n</tr>\n<tr>\n<td></td>\n<td>")

        for k in range(len(x)):
            html.write("\n<b class='"+str(id)+"_pillar_x'>"+str(x[k])+"</b>")

        html.write("\n</td>\n</tr>\n</table>") 

        #set backgroundcolor, width, padding
        css.write("\n#box_"+str(id)+"{background-color:" 
        +backgroundcolor+";width:"+str(size)+
        "px;padding:20px;display:inline-block;color:"+color+
        ";}\n."+str(id)+
        "_pillar_y{margin-top:20px;margin-right:20px;padding:10px;}\n."+
        str(id)+"_pillar{display:inline-block;background-color:"+str(color)+
        ";padding:10px;margin:10px;margin-bottom:-130px;}\n."+str(id)+
        "_pillar_x{margin-right:20px;margin-left:20px;display:inline-block;width:"+
        str(pillarsize)+";}\n#"+str(id)+"_chart_in{ padding:10px;}")

    #create bar chart
    def bar_chart(x,y,id,color,backgroundcolor,size,barsize):
        html.write("\n")

#create table
def table(matrix,id,color,backgroundcolor,boxsize,border):
    html.write("\n<table id='wepy_table' id='table_"+str(id)+"'")
    css.write("\n.table_box{display:inline-block; padding:10px;width:"+
    str(boxsize)+"px;}")
    css.write("\n#wepy_table{background-color:"+backgroundcolor+
    ";color:"+color+";display:inline-block;text-align:center;}")
    if border:
        html.write("border=1>")
    else:
        html.write(">")
    for i in range(len(matrix)):
        html.write("\n<tr>")
        m=matrix[i]
        for j in range(len(m)):
            html.write("\n<td class='table_box'>"+str(m[j])+"</td>")
        html.write("\n</tr>")
    html.write("</table>")

#create placeholder/s
def placeholder(loop):
    css.write("\n.placeholder{ padding:5px;}")
    for i in range(int(loop)):
        html.write("\n<p class='placeholder'></p>")

#trigonometry
class trigonometry:

    #sinus funtion
    def sinus(y_value,id,backgroundcolor,color,size):
        #create sinus funtion as an image
        if color == "white":
            pixel = Image.open("graph/trigonometry/sinus/pixel_white.png")
        else:
            pixel = Image.open("graph/trigonometry/sinus/pixel_black.png")

        image = Image.open("graph/trigonometry/sinus/sinus.png")
        line = Image.open("graph/trigonometry/sinus/line.png")

        y=250
        f= y_value
        for x in range(360):
            y -= ((math.sin(math.radians(x))*10)/5)*y_value
            image.paste(pixel,(x,int(y)),pixel)

        for x in range(360,720):
            y += ((math.sin(math.radians(x))*10)/5)*y_value
            image.paste(pixel,(x,int(y)),pixel)

        img = "graph/trigonometry/sinus/sinus.png"
        image.paste(line,(0,250),line)

        image.save(img)

        if f>=1:
            y1 = f; y2 = int(f)/2; y3 = 0; y4 = -int(f)/2; y5 = -int(f)
        else:
            y1 = 1; y2 = 0.5; y3 = 0; y4 = -0.5; y5 = -1

        #include img & create graph
        html.write("<div id='"+str(id)+"_graph'>\n<table id='"+str(id)+
        "'>\n<tr>\n<td id='"+str(id)+
        "_num'>\n<p id='"+str(id)+"_p_marginTop' class='"+str(id)+"_num_p'>"+str(y1)+"</p>\n<p class='"+str(id)+"_num_p'>"+
        str(y2)+"</p>\n<p class='"+str(id)+"_num_p'>"+str(y3)+"</p>\n<p class='"
        +str(id)+"_num_p'>"+str(y4)+
        "</p>\n<p id='"+str(id)+"_p_marginBottom'  class='"+str(id)+"_num_p'>"+str(y5)+"</p>\n</td>\n<td id='"+str(id)+
        "_num'>\n<img src='"+img+"'>\n</td>\n</tr>\n</table>\n</div>")
        
        css.write("\n#"+str(id)+"{width:"+str(size)+
        "px;padding-right:10px;background-color:"+
        str(backgroundcolor)+";}\n#"+str(id)+"_img img{width:"+str(size)+
        "px;padding:10px;}\n."+str(id)+
        "_num_p{ padding:10px;margin-top:80px;margin-bottom:80px;}\n#"+str(id)+
        "_graph{ display:inline-block;}\n#"+str(id)+"_p_marginTop{margin-top:10px;}\n#"
        +str(id)+"_p_marginBottom{margin-bottom:10px;}")

#info
print("files are created...") 