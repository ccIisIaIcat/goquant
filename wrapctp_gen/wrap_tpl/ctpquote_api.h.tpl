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
#include "../../../ctpapi/windows/ThostFtdcMdApi.h"
#else
#define WPCTP      __stdcall
#include "../../../ctpapi/windows/ThostFtdcMdApi.h"
#endif
#elif __APPLE__
#define WPCTP
#include "../../../ctpapi/macos/ThostFtdcMdApi.h"
#elif __linux__
#define WPCTP
#include "../../../ctpapi/linux/ThostFtdcMdApi.h"
#endif

#include <string.h>

class Quote : public CThostFtdcMdSpi
{
public:
    Quote();
	
    [[ range .On ]]
	// [[ .Comment ]]
	typedef int (WPCTP *[[ .FuncTypeName ]])([[ range $i, $v := .FuncFields ]][[if gt $i 0]], [[end]][[ .FieldType ]] [[ .FieldName ]][[ end ]]);
	void *[[ .FuncName ]]_;
	virtual void [[ .FuncName ]]([[ range $n, $var := .FuncFields ]][[if gt $n 0]], [[end]][[ .FieldType ]] [[ .FieldName ]][[ end ]]){ if([[ .FuncName ]]_) (([[ .FuncTypeName ]])[[ .FuncName ]]_)([[ range $n, $var := .FuncFields ]][[if gt $n 0]], [[end]][[ trimStar .FieldName ]][[ end ]]); }
    [[ end ]]
};


DLL_EXPORT_C_DECL void* WPCTP qCreateApi(const char *pszFlowPath, const bool bIsUsingUdp, const bool bIsMulticast);
DLL_EXPORT_C_DECL void* WPCTP qCreateSpi();
DLL_EXPORT_C_DECL void* WPCTP qGetApiVersion();
DLL_EXPORT_C_DECL void* WPCTP qGetTradingDay(CThostFtdcMdApi *api);
[[ range .On ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL void WPCTP q[[ .FuncName ]](Quote* spi, void* func);
[[ end ]]
[[ range .Fn ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL [[ .FuncRtn ]] WPCTP q[[ .FuncName ]](CThostFtdcMdApi *api[[ range .FuncFields ]], [[.FieldType]] [[.FieldName]][[if eq .FieldName "*ppInstrumentID"]][][[end]][[end]]);
[[ end ]]
