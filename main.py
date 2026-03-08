from PIL import Image
import os
from clc99 import *
import keyboard
import msvcrt
import sys

def crop_image(image_path):

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    if not image_path.lower().endswith(valid_extensions):
        print_error(f"{os.path.basename(image_path)} 不是有效图片文件！")
        return False

    try:
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            print_status(f"原始图片尺寸: 宽={img_width}, 高={img_height}")
            
            left = 65
            upper = 70
            right = 1980
            lower = 1149
            
            if right > img_width or lower > img_height:
                print_warning(f"裁剪坐标超出图片范围！")
                print_status(f"裁剪区域宽度={right-left}, 高度={lower-upper}")
                print_status(f"建议检查图片尺寸或调整裁剪坐标")
                return
            
            cropped_img = img.crop((left, upper, right, lower))
            
            filename = os.path.splitext(image_path)[0] + "_cropped" + os.path.splitext(image_path)[1]
            output_path = os.path.join(os.getcwd(), filename)
            
            if os.path.exists(output_path):
                print_warning(f"当前目录已存在 {filename}，要覆盖吗？（按下Y键继续，N键跳过）")
                while True:
                    if keyboard.is_pressed('y'):
                        break
                    elif keyboard.is_pressed('n'):
                        print_status(f"跳过保存 {filename}")
                        return
            
            cropped_img.save(output_path)
            print_good(f"裁剪完成！文件已保存到: {output_path}")
            print_status(f"裁剪后图片尺寸: 宽={cropped_img.width}, 高={cropped_img.height}")
            
    except FileNotFoundError:
        print_error(f"找不到文件 {image_path}，请检查路径是否正确")
    except PermissionError:
        print_error(f"没有权限访问文件 {image_path} 或保存输出文件")
    except Exception as e:
        print_error(f"处理图片时出错：{str(e)}")

if __name__ == "__main__":

    ascii_art = r"""


  ___   _____     ______  ____  _           _         ____      _   
 / _ \ / _ \ \   / /  _ \|  _ \| |__   ___ | |_ ___  / ___|   _| |_
| (_) | (_) \ \ / /| |_) | |_) | '_ \ / _ \| __/ _ \| |  | | | | __|
 \__, |\__, |\ V / |  _ <|  __/| | | | (_) | || (_) | |__| |_| | |_
   /_/   /_/  \_/  |_| \_\_|   |_| |_|\___/ \__\___/ \____\__,_|\__|

   

"""
    print(ascii_art)
    print_notrun("欢迎使用99VRChat拍立得裁剪工具！")

    if len(sys.argv) < 2:
        print_error("请将图片文件直接拖到本脚本图标上！")
        print_status("按任意键退出...")
        msvcrt.getch()
        sys.exit(1)
    else:
        success_count = 0
        total_count = len(sys.argv) - 1

    print_status(f"共检测到 {total_count} 个文件，正在处理...")

    for f in sys.argv[1:]:
        if os.path.isfile(f):
            print_status(f"正在处理图片: {f}")
            crop_image(f)
            success_count += 1
        else:
            print_warning(f"跳过非图片项: {f}")

    print_good(f"处理完成！成功裁剪 {success_count} 张图片。")
    print_status("按任意键退出...")
    msvcrt.getch()