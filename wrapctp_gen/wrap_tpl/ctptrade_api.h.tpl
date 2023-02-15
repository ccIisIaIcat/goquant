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

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#ifdef WIN32
#define WPCTP      __cdecl
#include "../../../ctpapi/windows/ThostFtdcTraderApi.h"
#include "../../../ctpapi/windows/DataCollect.h"
#else
#define WPCTP      __stdcall
#include "../../../ctpapi/windows/ThostFtdcTraderApi.h"
#include "../../../ctpapi/windows/DataCollect.h"
#endif
#elif __APPLE__
#define WPCTP
#include "../../../ctpapi/macos/ThostFtdcTraderApi.h"
#include "../../../ctpapi/macos/DataCollect.h"
#elif __linux__
#define WPCTP
#include "../../../ctpapi/linux/ThostFtdcTraderApi.h"
#include "../../../ctpapi/linux/DataCollect.h"
#endif

#include <string.h>

DLL_EXPORT_C_DECL int WPCTP dCTP_GetSystemInfo(char* pSystemInfo, int nLen);
[[if eq .Pf "macos"]]#ifdef __APPLE__
DLL_EXPORT_C_DECL int WPCTP dCTP_GetSystemInfoUnAesEncode(char* pSystemInfo, int nLen);
#endif[[end]]
DLL_EXPORT_C_DECL void* WPCTP dCTP_GetDataCollectApiVersion();

class Trade : public CThostFtdcTraderSpi
{
public:
    Trade();

    [[ range .On ]]
	// [[ .Comment ]]
	typedef int (WPCTP *[[ .FuncTypeName ]])([[ range $i, $v := .FuncFields ]][[if gt $i 0]], [[end]][[ .FieldType ]] [[ .FieldName ]][[ end ]]);
	void *[[ .FuncName ]]_;
	virtual void [[ .FuncName ]]([[ range $n, $var := .FuncFields ]][[if gt $n 0]], [[end]][[ .FieldType ]] [[ .FieldName ]][[ end ]]){ if([[ .FuncName ]]_) (([[ .FuncTypeName ]])[[ .FuncName ]]_)([[ range $n, $var := .FuncFields ]][[if gt $n 0]], [[end]][[ trimStar .FieldName ]][[ end ]]); }
    [[ end ]]
};

DLL_EXPORT_C_DECL void* WPCTP tCreateApi(const char *pszFlowPath);
DLL_EXPORT_C_DECL void* WPCTP tCreateSpi();
DLL_EXPORT_C_DECL void* WPCTP tGetApiVersion();
DLL_EXPORT_C_DECL void* WPCTP tGetTradingDay(CThostFtdcTraderApi *api);
[[ range .On ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL void WPCTP t[[ .FuncName ]](Trade* spi, void* func);
[[ end ]]
[[ range .Fn ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL [[ .FuncRtn ]] WPCTP t[[ .FuncName ]](CThostFtdcTraderApi *api[[ range .FuncFields ]], [[.FieldType]] [[.FieldName]][[if eq .FieldName "*ppInstrumentID"]][][[end]][[end]]);
[[ end ]]