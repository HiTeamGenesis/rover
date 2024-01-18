![Genesis Rover](https://i.imgur.com/F5X8UA5.png)  

# Our autonomous, life-detection rover.
Made to compete in the University Rover Challenge 2024.

## Setup Instructions for Raspberry Pi 4B

Making sure your pi is up-to-date

```$ sudo apt update; sudo apt upgrade; sudo reboot ```

Changing linux swap size to 2GB

```$ sudo nano /etc/dphys-swapfile ```
Change: CONF_SWAPSIZE=2048

```$ sudo /etc/init.d/dphys-swapfile restart swapon -s ```

Install packages

```
$ sudo apt-get install -y libdrm-amdgpu1 libdrm-amdgpu1-dbgsym libdrm-dev libdrm-exynos1 libdrm-exynos1-dbgsym libdrm-freedreno1 libdrm-freedreno1-dbgsym libdrm-nouveau2 libdrm-nouveau2-dbgsym libdrm-omap1 libdrm-omap1-dbgsym libdrm-radeon1 libdrm-radeon1-dbgsym libdrm-tegra0 libdrm-tegra0-dbgsym libdrm2 libdrm2-dbgsym

$ sudo apt-get install -y libglu1-mesa libglu1-mesa-dev glusterfs-common libglu1-mesa libglu1-mesa-dev libglui-dev libglui2c2

$ sudo apt-get install -y libglu1-mesa libglu1-mesa-dev mesa-utils mesa-utils-extra xorg-dev libgtk-3-dev libusb-1.0-0-dev
```

Getting RealSense

```
$ cd ~
$ git clone https://github.com/IntelRealSense/librealsense.git
$ cd librealsense
$ sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/ 
$ sudo udevadm control --reload-rules && sudo udevadm trigger 

```

Updating cmake (very important)

```
$ cd ~
$ wget https://cmake.org/files/v3.11/cmake-3.11.4.tar.gz
$ tar -zxvf cmake-3.11.4.tar.gz;rm cmake-3.11.4.tar.gz
$ cd cmake-3.11.4
$ ./configure --prefix=/home/pi/cmake-3.11.4
$ make -j4
$ sudo make install
$ export PATH=/home/pi/cmake-3.11.4/bin:$PATH
$ source ~/.bashrc
$ cmake --version
cmake version 3.11.4
```

Setting Path

```
$ nano ~/.bashrc
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

$ source ~/.bashrc

```

Installing TBB

```
$ cd ~
$ wget https://github.com/PINTO0309/TBBonARMv7/raw/master/libtbb-dev_2018U2_armhf.deb
$ sudo dpkg -i ~/libtbb-dev_2018U2_armhf.deb
$ sudo ldconfig
$ rm libtbb-dev_2018U2_armhf.deb
```

Installing Python3.9 **(VERY IMPORTANT)**

`$ sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev`

``` 
$ wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz
$ tar xf Python-3.9.0.tar.xz
$ cd Python-3.9.0
$./configure --enable-optimizations --prefix=/usr
$ make -j4
$ sudo make altinstall
```

``` 
cd ..
sudo rm -r Python-3.9.0
rm Python-3.9.0.tar.xz
. ~/.bashrc
```

Installing OpenCV *(must be 4.5.3.56)*

`$ python3.9 -m pip install opencv-contrib-python==4.5.3.56`

Building librealsense2 

```
$ cd ~/librealsense
$ mkdir  build  && cd build
$ cmake .. -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=Release -DFORCE_LIBUVC=true
$ make -j4
$ sudo make install
```

Building pyrealsense2

```
$ cd ~/librealsense/build

$ cmake .. -DBUILD_PYTHON_BINDINGS=bool:true -DPYTHON_EXECUTABLE=$(which python3.9)

$ make -j4
$ sudo make install
```

Finally, make sure the following is in your ~/.bashrc:

```
export PATH=/home/pi/cmake-3.11.4/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH:/usr/local/lib:/usr/local/OFF
```

Done! 🚀