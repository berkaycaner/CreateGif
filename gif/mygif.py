import imageio.v3 as imio
import numpy as np # Numpy is needed to resize the shape of the images.They have to be the same size to create a gif.

filenames = ['drlivesey1.jpg', 'drlivesey2.jpg', 'drlivesey3.jpg']
images = []

# Read the first image and get its shape
ref_image = imio.imread(filenames[0])
ref_shape = ref_image.shape

images.append(ref_image)
for filename in filenames[1:]:
    img = imio.imread(filename)
    # Resize if shape doesn't match
    if img.shape != ref_shape:
        from PIL import Image
        img = Image.fromarray(img).resize((ref_shape[1], ref_shape[0]))
        img = np.array(img)
    images.append(img)

imio.imwrite('drlivesey.gif', images, duration=500, loop=0)