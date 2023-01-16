import wepy2 as wepy

#create topic [text,id,color,size]
wepy.topic("WePy Examples","topic","rgb(100,100,200)",30.5)

#create text [text,id,color,size]
wepy.text("welcome to wepy","text","rgb(130,130,130)",19)

#set alingment
wepy.alingment("center")

#set background
wepy.background("rgb(22,22,22)")

#create chart
x=["person 1","person 2","person 3","person 4","person 5","person 6","person 7","person 8"]
y=[70,90,10,40,99,99,31,41]
wepy.chart.bar_chart(x,y,"barchart","cornflowerblue","black",200,60)
wepy.chart.pillar_chart(x,y,"pillarchart","cornflowerblue","black",840,40)

#placeholder
wepy.placeholder(1)

#create table
m=[
    [3,1,4],
    [1,5,9],
    [2,6,5]
]
wepy.table(m,"table","gray","white",240,True)

wepy.placeholder(1)
#trigonometry
#sinus
wepy.trigonometry.sinus(1,"sinus_function","white","black",400)

#open file
wepy.open()