# Instruction

In this package, we use this project to convert "txt" files obtained by laser algorithms into trajectories of pose.

# 1.Prerequisites

## 1.1 Ubuntu 

  Ubuntu 64-bit 16.04 or 18.04.

# 2 Install 

Clone the source code for the project .Before build the project, please rewrite the paths of  include_directories and LINK_DIRECTORIES in CMakeLists.txt.

```
git clone https://github.com/WXY485/PAINT.git
cd x86_64-linux-gnu
sudo cp python3.6m /usr/include/x86_64-linux-gnu
cd ..
mkdir build
cd build
cmake ..
make
```

# 3 RUN

Move the executable file runpy to the same directory as the txt and exercise.py files.Then we can  run the executable file to get the graph.

```
sudo mv runpy /home/.../project/
./runpy exercise1 paint
```