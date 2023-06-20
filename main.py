from PIL import Image
import os
from colorama import Fore, Style
import json
 

def addWatermark(image, image_dir, watermark_path, parameters):
    width = parameters['width']
    offset = parameters['offset']
    opacity = parameters['opacity']
    output_dir = parameters['output_dir']

    filename = os.path.splitext(os.path.basename(image))[0]
    extension = os.path.splitext(image)[1]

    background = Image.open(os.path.join(image_dir, image))
    watermark = Image.open(watermark_path)

    # Calculate the desired height of the watermark based on the width
    aspect_ratio = watermark.size[0] / watermark.size[1]
    resized_watermark_width = int(width / 100 * background.size[0])
    resized_watermark_height = int(resized_watermark_width / aspect_ratio)

    # Resize the watermark while maintaining the aspect ratio
    watermark = watermark.resize((resized_watermark_width, resized_watermark_height))

    # Convert the watermark to RGBA format
    watermark = watermark.convert("RGBA")

    # Adjust the opacity of the watermark
    watermark_with_opacity = watermark.copy()
    watermark_with_opacity.putalpha(int((opacity / 100) * 255))

    # Determine the offset
    paste_x = int((background.size[0] - watermark.size[0]) * ((100 - offset) / 100))
    paste_y = int((background.size[1] - watermark.size[1]) * ((100 - offset) / 100))

    # Create a mask
    mask = Image.new('L', watermark.size, 0)
    mask.paste(watermark_with_opacity, (0, 0), watermark_with_opacity)

    # Paste the watermark
    background.paste(watermark_with_opacity, (paste_x, paste_y), mask)

    # Save the output image
    background.save(f"{os.path.join(target_dir, output_dir, filename)} - watermark{extension}")

if __name__ == '__main__':
    new_line = '\n'

    data_dir = 'data/'
    watermark = f'{data_dir}watermark.png'
    parameters_file = f'{data_dir}parameters.json'
    f = open(parameters_file) 
    parameters = json.load(f)
    print(Fore.CYAN + f"""
=====================================================================
 __          __  _______ ______ _____  __  __          _____  _  __  
 \ \        / /\|__   __|  ____|  __ \|  \/  |   /\   |  __ \| |/ /  
  \ \  /\  / /  \  | |  | |__  | |__) | \  / |  /  \  | |__) | ' /  
   \ \/  \/ / /\ \ | |  |  __| |  _  /| |\/| | / /\ \ |  _  /|  <   
    \  /\  / ____ \| |  | |____| | \ \| |  | |/ ____ \| | \ \| . \ 
     \/  \/_/    \_\_|  |______|_|  \_\_|  |_/_/    \_\_|  \_\_|\_\
                                                                                                          
=====================================================================""")
    while input(Fore.MAGENTA + f"""
Settings :
--------------------------
width       |   {parameters['width']}%
offset      |   {parameters['offset']}%
opacity     |   {parameters['opacity']}%
output_dir  |   {parameters['output_dir'][:-1]}

{Fore.CYAN}Change settings : write 'edit'
Run : [Enter]
>> """ + Style.RESET_ALL) == 'edit':
        parameter_name = input(Fore.CYAN + "Write the name of the setting you want to edit : " + Style.RESET_ALL)
        if parameter_name in parameters:
            new_value = input(Fore.CYAN + f"New value for '{parameter_name}' : " + Style.RESET_ALL)
            if parameter_name == 'output_dir':
                parameters[parameter_name] = new_value + '/'
            else:
                try:
                    parameters[parameter_name] = int(new_value)
                except:
                    print(Fore.RED + 'Error : incorrect value type' + Style.RESET_ALL)
            if input(Fore.CYAN + 'Save parameters ? [y/n] ' + Style.RESET_ALL) == 'y':
                with open(parameters_file, 'w') as f:
                    f.write('{"width":' + str(parameters["width"]) + ',"offset":' + str(parameters["offset"]) + ', "opacity":' + str(parameters["opacity"]) + ', "output_dir":"' + str(parameters["output_dir"]) + '"}')
        else:
            print(Fore.RED + 'Setting not found' + Style.RESET_ALL)

    print()

    while not os.path.isdir(target_dir := os.path.join(os.path.dirname(os.path.abspath(__file__)), input(Fore.CYAN + "Target directory ([Enter] for current): " + Style.RESET_ALL))):
        print(Fore.RED + 'No such directory' + Style.RESET_ALL)
    files = os.listdir(target_dir)

    if not os.path.isdir(os.path.join(target_dir, parameters['output_dir'])):
        os.makedirs(os.path.join(target_dir, parameters['output_dir']))

    image_extensions = ['.jpg', '.jpeg', '.png']
    files = [file for file in files if (file != watermark) and (os.path.splitext(file)[1].lower() in image_extensions)]

    print()

    file_progress = 0
    exception_errors = []
    for file in files:
        try:
            addWatermark(file, target_dir, watermark, parameters)
        except Exception as e:
            print(Fore.RED + f'Could not add a watermark to : {file}\nError: {e}' + Fore.CYAN)
            exception_errors.append(file)

        file_progress += 1
        print(Fore.BLUE + f'{int(file_progress * 100 / len(files))}% ({file_progress}/{len(files)})' + Fore.CYAN)

    new_line_tab = '\n\t'
    print(Fore.GREEN + f"""
Program finished
--------------------------
processed   | {len(files)}
successful  | {len(files) - len(exception_errors)}
exceptions  | {len(exception_errors)}
--------------------------
Processing issue(s) :
{new_line_tab.join(exception_errors)}
    """ + Style.RESET_ALL)
