import os
import sys

inputdir = 'video'
outputdir = 'svideo'

for v in os.listdir(inputdir):
    invp = os.path.join(inputdir,v)
    outputv = os.path.join(outputdir,v)
    cmd = 'ffmpeg -i {} -filter_complex "[0:v]split=2[blur][clear]; [blur]crop=iw/2:ih:0:0[blur]; [clear]crop=iw/2:ih:iw/2:0[clear]; [blur][clear]blend=all_expr=\'A*(if(gte(X,W*T*0.5),1,0))+B*(1-if(gte(X,W*T*0.5),1,0))\'[output]" -map "[output]" -c:v libx264 -crf 6 {}'.format(invp,outputv)
    
    
    print(cmd)
    os.system(cmd)