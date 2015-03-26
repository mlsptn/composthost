import os 
import sys

def compost(input): 
    start = .7 
    steps = 30

    expand = int((1.0/float(start)) * 100.0)
    print 'expand is ' + str(expand)
    decay = int(float(start) * 100.0)
    print 'decay is ' + str(decay)

    for i in range(steps):
        start = str(float(start) - .006);
        expand = int((1.0/float(start)) * 100.0)
        decay = int(float(start) * 100.0)

        filename = './results/' + str(i).zfill(4) + '.png'
        if i == 0:
            im = input
        else:
            im = './results/' + str(i-1).zfill(4) + '.png'
        print 'im is ' + im
        if (i % 2 == 0):
            command = 'convert %s -liquid-rescale %sx%s%%\! %s' % (im, decay, decay, filename)
            print command
        else:
            command = 'convert %s -liquid-rescale %sx%s%%\! %s' % (im, expand, expand, filename)
            print command
        os.system(command)
    os.system('rm ./results/*[02468].png')
    gifName = input[(input.find('/')+1):]
    os.system('convert -delay 10 -loop 0 ./results/*.png ./results/' + gifName[:-4] + '.gif')
    os.system('rm ./results/*.png')
    os.system('say "compost complete"')

if __name__ == "__main__":
    foodDir = 'food'
    for file in os.listdir(foodDir):
        if file.endswith(('.jpg','.png','.jpeg')):
            food = foodDir + '/' + file 
            compost(food)
