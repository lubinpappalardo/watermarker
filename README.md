# Watermarker
> #### ***alpha 1.1***

The quick and easy solution to watermark your images. Customizable settings and watermark image.
___
### 1. Seting up the files
> To install it, place the `data` folder and `main.py` **in the same directory**.

> The files have to be in any directory as long as your images are either in the same directory or in a child, grand-child, etc directory.

### 2. Requirements
> You will find the requirements.txt in the `data` folder.

> `Python 3.8` or higher is required

> This project was developed with `Python 3.10.11`

### 3. Running
> Run `main.py` in a terminal.

> Type 'edit' to edit the settings or just enter to continue.

> It will now ask for target directory, this is the path to directory in which are your images (note: do not put a '/' at the end). If your images are in the same directory as `main.py`, press enter.

> You will see the progress.

> At the end of the programm a feedback will be given telling you if any errors happened.

> The watermarked images should now be in a new folder 'watermarked' by default if not changed (see next section).

### 4. Customization
> A file named `parameters.json` is located in the `data` folder. It contains settings for the display of the watermark.

| Parameter | Type | Function |
| --- | --- | --- |
| width | Interger | Width of the watermark in percentage relative to the width of the image. |
| offset | Interger | Offset from the bottom right corner of the watermark in percentage relative to the width of the image. |
| opacity | Interger | Opacity in percentage of the watermark. |
| output_dir | String | Folder in which the watermarked images are saved. |
> You can either change those values directly in the files or using `main.py` by typing 'edit'.

### 5. Changing the watermark
> You can change the watermark by changing the `watermark.png` image in the `data` folder.  **Make sure it's a png**.

___

A `watermarker.zip` file will be available in the realeases for download.
