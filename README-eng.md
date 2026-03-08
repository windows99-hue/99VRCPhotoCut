# 99VRCPhotoCut

> Create, Share, Play

## Introduction

This is a lightweight utility designed to easily crop out the white borders from photos saved as instant photos in VRChat, leaving only the main image intact.

> [!WARNING]
>
> This program is only compatible with the Windows operating system. However, it may support MacOS/Linux after modifying the arbitrary key detection logic.

## Installation

### Download

You can download the compiled version from the [Releases](https://github.com/windows99-hue/99VRCPhotoCut/releases) page.

### Compile Yourself

This program needs to be compiled into an `exe` file to be usable.

> [!NOTE]
>
> This program was developed with Python 3.14 and should theoretically work with any Python 3.x version.

1. Clone this repository

2. Run the following command to install dependencies:
   ~~~shell
   pip install -r requirements.txt
   ~~~

3. Run the compilation command:
   ~~~shell
   pyinstaller -F main.py
   ~~~
   
   For more usage of `pyinstaller`, please refer to the official documentation.

## Usage

Simply drag and drop the photos you want to process onto `main.exe`, as shown in the image below:

![Preview](https://github.com/user-attachments/assets/a730e456-d4fa-4d42-9b5a-6da791eb033c)

Multiple photos can be dragged in at once. If there are duplicate filenames, the program will prompt you to confirm whether to overwrite the files.

## Final Notes

This program is licensed under the `MIT License`. Enjoy your use!

> Pausing time is a divine power, yet photography allows us to peek into this power of the gods. ——Tim
