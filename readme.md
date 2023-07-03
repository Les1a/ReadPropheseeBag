Setup
    https://docs.prophesee.ai/stable/installation/index.html
    运行Metavision_SDK_410_Setup.exe
    （即安装Prophesee这个文件夹）

Dependencies
    python 3.8 or 3.9
    下面以3.8为例

    Install packages
    python -m pip install pip --upgrade
    python -m pip install "opencv-python==4.5.5.64" "sk-video==1.1.10" "fire==0.4.0" "numpy==1.23.4" pandas scipy h5py
    python -m pip install jupyter jupyterlab matplotlib "ipywidgets==7.6.5"

    Add path
    %USERPROFILE%\AppData\Local\Programs\Python\Python38
    %USERPROFILE%\AppData\Local\Programs\Python\Python38\Scripts
    %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
    (
        举个栗子：
        import sys
        print(sys.path)
        # Add %USERPROFILE%\AppData\Local\Programs\Python\Python38 to PYTHONPATH if the output of print(sys.path) does not mention it.
        sys.path.append("%USERPROFILE%\AppData\Local\Programs\Python\Python38")
    )
    
    reboot

Run
    将待解压的raw文件均放入本文件夹目录中
    python read_raw2csv.py
