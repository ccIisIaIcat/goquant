#include "ctptrade_api.h"
#include <string.h>

DLL_EXPORT_C_DECL int WPCTP dCTP_GetSystemInfo(char* pSystemInfo, int nLen) { return CTP_GetSystemInfo(pSystemInfo, nLen); };
[[if eq .Pf "macos"]]#ifdef __APPLE__
DLL_EXPORT_C_DECL int WPCTP dCTP_GetSystemInfoUnAesEncode(char* pSystemInfo, int nLen) { return CTP_GetSystemInfoUnAesEncode(pSystemInfo, nLen); };
#endif[[end]]
DLL_EXPORT_C_DECL void* WPCTP dCTP_GetDataCollectApiVersion() { return (void*)CTP_GetDataCollectApiVersion();};

Trade::Trade()
{
	[[ range .On ]][[ .FuncName ]]_ = NULL;
	[[ end ]]
}


DLL_EXPORT_C_DECL void* WPCTP tCreateApi(const char *pszFlowPath = "") { return CThostFtdcTraderApi::CreateFtdcTraderApi(pszFlowPath); }
DLL_EXPORT_C_DECL void* WPCTP tCreateSpi() { return new Trade(); }
DLL_EXPORT_C_DECL void* WPCTP tGetApiVersion() { return (void*)CThostFtdcTraderApi::GetApiVersion(); }
DLL_EXPORT_C_DECL void* WPCTP tGetTradingDay(CThostFtdcTraderApi *api) { return (void*)api->GetTradingDay(); }

[[ range .On ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL void WPCTP t[[ .FuncName ]](Trade* spi, void* func){ spi->[[ .FuncName ]]_ = func; }
[[ end ]]
[[ range .Fn ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL [[ .FuncRtn ]] WPCTP t[[ .FuncName ]](CThostFtdcTraderApi *api[[ range .FuncFields ]], [[.FieldType]] [[.FieldName]][[if eq .FieldName "*ppInstrumentID"]][][[end]][[end]]){ [[ if eq .FuncRtn "void"]]api->[[.FuncName]]([[ range $i, $v := .FuncFields ]][[if gt $i 0]], [[end]][[trimStar .FieldName]][[end]]); return;[[ else ]]return api->[[.FuncName]]([[ range $i, $v := .FuncFields ]][[if gt $i 0]], [[end]][[trimStar .FieldName]][[end]]);[[ end ]] }
[[ end ]]