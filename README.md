# visual-cryptography-hiding
Python visual cryptography script to hide message in .pbm image.

Python script that can be used to hide a message in a .pbm image, the user provides an initial image to use for encryption, the dimensions of this image provided are used to create a new image, the user also provides the message to be hidden in the new image created.

To encrypt:
```bash:
$ cd /hiding
$ python hiding.py hiding.pbm 'this is the message to hide'
```
The script also decrypts the message in the .pbm image

To decrypt:
```bash:
$ python hiding.py hiding.pbm
Do you want to hide or reveal information? Type hide or reveal. reveal
Hidden message is: this is the message to hide
$
