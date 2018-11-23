import imageio as img

def create_gif(gif_name,gif_path,duration):
    frame = []
    for i in gif_path:
        frame.append(img.imread(i))
    img.mimsave(gif_name,frame,duration=duration)
    pass

def main():
    gifname = 'zyx.gif'
    gifpath = ['D:\\lenovo\\Pictures\\Acg\\001.jpg','D:\\lenovo\\Pictures\\Acg\\002.jpg','D:\\lenovo\\Pictures\\Acg\\003.jpg']
    dur = 1
    create_gif(gifname,gifpath,duration=dur)

if __name__ == '__main__':
    main()