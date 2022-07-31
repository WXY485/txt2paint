cmake_minimum_required( VERSION 2.8 )
project(cppCallPythonFunc)
 
#set(CMAKE_CXX_STANDARD 14)
 
# 用locate Python.h 取得头文件的位置之后可以使用 #include <Python.h>
include_directories(
   "/usr/include/python3.6"
)
 
 
#在控制台运行python3.6-config --ldflags 取得参数
#-L/usr/lib/python3.6/ -L/usr/lib -lpython3.6m -lpthread -ldl  -lutil -lm  -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions
 
# 添加动态库的位置
LINK_DIRECTORIES("/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu")
# LINK_DIRECTORIES("/usr/lib")
 
add_executable(runpy main.cpp exercise1.py)
target_link_libraries(runpy -lpython3.6m)

