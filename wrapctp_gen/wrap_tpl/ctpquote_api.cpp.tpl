#include "ctpquote_api.h"
#include <string.h>


Quote::Quote()
{
	[[ range .On ]][[ .FuncName ]]_ = NULL;
	[[ end ]]
}


DLL_EXPORT_C_DECL void* WPCTP qCreateApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false, const bool bIsMulticast=false) { return CThostFtdcMdApi::CreateFtdcMdApi(pszFlowPath, bIsUsingUdp, bIsMulticast); }
DLL_EXPORT_C_DECL void* WPCTP qCreateSpi() { return new Quote(); }
DLL_EXPORT_C_DECL void* WPCTP qGetApiVersion() { return (void*)CThostFtdcMdApi::GetApiVersion(); }
DLL_EXPORT_C_DECL void* WPCTP qGetTradingDay(CThostFtdcMdApi *api) { return (void*)api->GetTradingDay(); }
[[ range .On ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL void WPCTP q[[ .FuncName ]](Quote* spi, void* func){ spi->[[ .FuncName ]]_ = func; }
[[ end ]]
[[ range .Fn ]]
// [[ .Comment ]]
DLL_EXPORT_C_DECL [[ .FuncRtn ]] WPCTP q[[ .FuncName ]](CThostFtdcMdApi *api[[ range .FuncFields ]], [[.FieldType]] [[.FieldName]][[if eq .FieldName "*ppInstrumentID"]][][[end]][[end]]){ [[ if eq .FuncRtn "void"]]api->[[.FuncName]]([[ range $i, $v := .FuncFields ]][[if gt $i 0]], [[end]][[trimStar .FieldName]][[end]]); return;[[ else ]]return api->[[.FuncName]]([[ range $i, $v := .FuncFields ]][[if gt $i 0]], [[end]][[trimStar .FieldName]][[end]]);[[ end ]] }
[[ end ]]
