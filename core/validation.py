import hashlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def check(your_answer):
    hash_object = hashlib.sha256(str.encode(your_answer))
    hex_dig = hash_object.hexdigest()
    if hex_dig == '1f00098bf5baa73ab29931c4a8cd1dd1d6555c410492cc9aa50ffaf3d2fd5859':
        #print('Congratulations! You are a python data visualization expert.')
        img = mpimg.imread('./data/validation/congrats.png')
    else:
        #print('Wrong answer. Please try again.')
        img = mpimg.imread('./data/validation/try_again.png')
        
    fig, ax = plt.subplots(1, 1, figsize=(5,5))
    ax.imshow(img)
    ax.grid(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()