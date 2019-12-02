import pandas as pd
import cp3_dbops
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def team_charts(df, gameterm, teamname):
    player = df['PlayerName']
    stats = df[gameterm]
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.4)
    plt.xticks(rotation=90)
    plt.bar(player, stats)
    plt.title(gameterm+'s by Player')
    if not os.path.exists('./PlotImages/'+ teamname +'/'):
        os.makedirs('./PlotImages/'+ teamname +'/')
    plt.savefig('./PlotImages/'+ teamname +'/'+ gameterm +'.png', transparent=True)
    plt.close()
def process_video(team, allstats):
    cap = cv2.VideoCapture('LakersvsClippers.mp4')
    plotfigure = cv2.imread('./PlotImages/'+team+'/'+allstats[0]+'.png')
    dimensions = plotfigure.shape #(480,640,3)

    xplot = dimensions[0]
    yplot = dimensions[1]
    plotfigure = cv2.resize(plotfigure,(int(dimensions[1]*0.6), int(dimensions[0]*0.6)))

    ret, frame = cap.read()
    dimvideo = frame.shape
    xframe = dimvideo[0]
    yframe = dimvideo[1]

    xrate = xplot/xframe
    yrate = yplot/yframe
    i = 0
    while True:
        ret, frame = cap.read()
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
        if i < len(allstats) - 1:
            if timestamp / 10000 <= i:
                frame[int(xframe*0.2*xrate):int(xframe*0.8*xrate),int(yframe*0.2*yrate):int(yframe*0.8*yrate)] = plotfigure
            else:
                i = i + 1
                plotfigure = cv2.imread('./PlotImages/'+team+'/'+allstats[i]+'.png')
                plotfigure = cv2.resize(plotfigure,(int(dimensions[1]*0.6), int(dimensions[0]*0.6)))


        cv2.imshow('frame', frame)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

