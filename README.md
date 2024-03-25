## Cutout data augment

### requirement
  pip install numpy



A data enhancement method for Cutout in the data annotation box.

It can improve the efficiency of enhancement to a certain extent and avoid meaningless cutouts.Program execution will automatically generate an xml annotation file corresponding to the image.

This is a example:
![the origin image](origin/img/well5_0001.jpg)
![image after augment](result/img/Cutoutwell5_0001.jpg)

# attention

To run the code, you need to input images and tags at the same time. It is best for tags and images to be in the same order in the folder, otherwise tags and images will not match.

