#pragma once
#ifdef _WIN32  //64位系统没有预定义 WIN32
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT_C_DECL __declspec(dllexport)
#endif
#else
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C"
#else
#define DLL_EXPORT_C_DECL extern
#endif
#endif

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#ifdef WIN32
#define WPCTP      __cdecl
#include "../../csource/ctpapi/windows/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/windows/ThostFtdcUserApiStruct.h"
#else
#define WPCTP      __stdcall
#include "../../csource/ctpapi/windows/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/windows/ThostFtdcUserApiStruct.h"
#endif
#elif __APPLE__
#define WPCTP
#include "../../csource/ctpapi/macos/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/macos/ThostFtdcUserApiStruct.h"
#elif __linux__
#define WPCTP
#include "../../csource/ctpapi/linux/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/linux/ThostFtdcUserApiStruct.h"
#endif

#define bool _Bool

DLL_EXPORT_C_DECL void* WPCTP qCreateApi(const char *pszFlowPath, const bool bIsUsingUdp, const bool bIsMulticast);
DLL_EXPORT_C_DECL void* WPCTP qCreateSpi();
DLL_EXPORT_C_DECL void* WPCTP qGetApiVersion();
DLL_EXPORT_C_DECL void* WPCTP qGetTradingDay(void *api);
[[ range .On ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL void WPCTP q[[ .FuncName ]](void* spi, void* func);
DLL_EXPORT_C_DECL int q[[ .FuncName ]]_([[ range $i, $v := .FuncFields ]][[ if gt $i 0]], [[ end ]][[ .FieldType|struct_Type ]] [[ .FieldName ]][[ end ]]);
[[ end ]]
[[ range .Fn ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL [[ .FuncRtn ]] WPCTP q[[ .FuncName ]](void *api[[ range .FuncFields ]], [[.FieldType|struct_Type]] [[.FieldName]][[if eq .FieldName "*ppInstrumentID"]][][[end]][[end]]);
[[ end ]]
