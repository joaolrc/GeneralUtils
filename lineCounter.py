import os

filesDir = '/home/joaolrc/Desktop/lineCounter/package/'
counter = 0
if os.path.isdir(filesDir):
    content = [filesDir + x for x in os.listdir(filesDir) ]

    for file in content:
        if os.path.isfile(file):
            print('Scaning file: {}').format(file)
            for line in open(file).xreadlines(  ): 
                print('[{}] {}'.format(counter, line) )
                counter =counter + 1
print('Total Row Count: {}'.format(counter))
