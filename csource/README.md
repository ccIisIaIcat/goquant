# C/C++ Source

## 说明

​	__C/C++工程源文件__

## 文件夹结构

__ctpapi__：CTP API官方源代码和官方动态链接库

__include__：C/C++头文件目录

__src__：C/C++源文件目录

__src/wrapper_ctp__：CTP API包装源文件


## Build Library

### MAC

进入当前工作目录下的`src/wrapper_ctp/macos`路径

#### 命令行

Quote API

__gcc__

```
g++ -shared -fPIC -o ../../../../libs/ctpapi/libctpquote_api.dylib ctpquote_api.cpp -L ../../../ctpapi/macos  -lthostmduserapi_se -lthosttraderapi_se -lMacDataCollect
```

__clang__

```
clang++ -shared -fPIC -o libctpquote_api.dylib ctpquote_api.cpp -L ../../../ctpapi/macos  -lthostmduserapi_se -lthosttraderapi_se -lMacDataCollect
```

Trade API

__gcc__

```
g++ -shared -fPIC -o ../../../../libs/ctpapi/libctptrade_api.dylib ctptrade_api.cpp -L ../../../ctpapi/macos  -lthostmduserapi_se -lthosttraderapi_se -lMacDataCollect
```

__clang__

```
clang++ -shared -fPIC -o libctptrade_api.dylib ctptrade_api.cpp -L ../../../ctpapi/macos  -lthostmduserapi_se -lthosttraderapi_se -lMacDataCollect
```

#### Xcode

打开项目根目录下的macos文件夹下的AlgoTrade工作空间，对其中项目进行编译

__如果使用Xcode进行编译，需要在Xcode的 Build Settings -> Apple Clang - Code Generation -> Symbols Hidden by Default设置为`No`，或者在需要导出的函数前添加 `__attribute__((visibility("default")))`__

## Windows

打开项目根目录下的windows文件夹下的AlgoTrade解决方案，对其中项目进行编译

### Linux

进入当前工作目录下的`src/wrapper_ctp/macos`路径

Quote API

```
g++ -shared -fPIC -Wl,-rpath . -L ../../../ctpapi/linux/ -o ../../../../libs/ctpapi/libctpquote_api.so ctpquote_api.cpp -lthostmduserapi_se -lthosttraderapi_se -lLinuxDataCollect
```

Trade API

```
g++ -shared -fPIC -Wl,-rpath . -L ../../../ctpapi/linux/ -o ../../../../libs/ctpapi/libctptrade_api.so ctptrade_api.cpp -lthostmduserapi_se -lthosttraderapi_se -lLinuxDataCollect
```
