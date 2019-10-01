# Number-Plate-Anonymiser

A Python interface for encrypting vehicle license plate data. Under GDPR, 
Transport Scotland can not interact with the raw number plate data if it could 
be used to identify people in conjunction with other datasets such as, the time 
when and location where the license plate was picked up on camera.

## Advice for Users
:book: TO BE UPDATED

## Advice for Developers
Using the `gui.ui` file with `PyInstaller` and `--onefile` seems to be a massive 
pain. To get around this, we can instead use `PyQt5`'s own inbuilt converter to 
convert from a `.ui` file to a regular `.py` file. The short version to do this 
is:
```shell script
python -m PyQt5.uic.pyuic -x gui.ui -o gui.py
```

## Running the Anonymiser
1. Download the [latest release](https://github.com/TransportScotland/Number-Plate-Anonymiser/releases) 
   of the project. 
2. Unzip the number-plate-anonymiser folder
3. Run the number-plate-anonymiser.exe file that can be found in that folder. 
   Note: It will not work if it is copied out of the folder.

