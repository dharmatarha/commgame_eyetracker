# import cv2
import os
import glob

baseF = '/media/adamb/bonczData/bargaining_game_Mordor/pair24/'

# glob for video files: "world.mp4" and "eye0.mp4"
worldCamFiles = glob.glob(baseF + '**/world.mp4', recursive=True)
eyeCamFiles = glob.glob(baseF + '**/eye0.mp4', recursive=True)

# loop through world camera files, resize / reformat them with ffmpeg
for camFile in worldCamFiles:
    # output file path for transformed video
    outFileBase = os.path.split(camFile)[0]
    outFile = os.path.join(outFileBase, 'worldSmall.mp4')
    # call ffmpeg
    print('Calling ffmpeg on video file at' + camFile)
    cmd_str = ' '.join(['ffmpeg', '-i', camFile, '-pix_fmt', 'yuv420p', '-vsync', 'passthrough', outFile])
    os.system(cmd_str)

# loop through eye camera files, resize / reformat them with ffmpeg
for camFile in eyeCamFiles:
    # output file path for transformed video
    outFileBase = os.path.split(camFile)[0]
    outFile = os.path.join(outFileBase, 'eye0Small.mp4')
    # call ffmpeg
    print('Calling ffmpeg on video file at' + camFile)
    cmd_str = ' '.join(['ffmpeg', '-i', camFile, '-pix_fmt', 'yuv420p', '-vsync', 'passthrough', outFile])
    os.system(cmd_str)


# for pair in range(8):
#     pairIdx = pair + 1
#
#     labName = 'G'
#
#     print('\nCurrent subject: pair' + str(pairIdx) + labName)
#     vidFile = baseF + 'pair' + str(pairIdx) + '/pair' + str(pairIdx) + labName + '/pupil/pair' + str(pairIdx) + labName + '/world.mp4'
#     outFile = baseF + 'pair' + str(pairIdx) + '/pair' + str(pairIdx) + labName + '/pupil/pair' + str(pairIdx) + labName + '/worldCamera.mp4'
#     print('Video file at ' + vidFile)
#
#     print('Calling ffmpeg...')
#     cmd_str = ' '.join(['ffmpeg', '-i', vidFile, '-pix_fmt', 'yuv420p', '-vsync', 'passthrough', outFile])
#     os.system(cmd_str)
