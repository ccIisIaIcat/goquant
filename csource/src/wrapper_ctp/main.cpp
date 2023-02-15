#ifdef _WIN32
#include "windows/ctpquote_api.h"
#include "windows/ctptrade_api.h"
#elif __APPLE__
#include "macos/ctpquote_api.h"
#include "macos/ctptrade_api.h"
#elif __linux__
#include "linux/ctpquote_api.h"
#include "linux/ctptrade_api.h"
#endif


#include <iostream>
#include <string>
#include <typeinfo>
#include <time.h>
#include <stdio.h>
#ifdef _WIN32
#include <windows.h>
#include <io.h>
#include<direct.h>
#else
#include <unistd.h>
#include <dirent.h>
#endif
#include <sys/stat.h>
#include <sys/types.h>


#ifdef _WIN32
#define sleep(a) Sleep(a*1000)
#define access _access
#define mkdir(a, b) _mkdir(a)
#endif


#ifdef _WIN32
#define strcpy strcpy_s
#else
#define strcpy strcpy
#endif


void OnRspAuthenticate_(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    std::string tmp = std::string(pRspInfo->ErrorMsg);
    std::cout << "Auth: " << tmp << std::endl;
//    std::cout << gbk_to_utf8(tmp) << std::endl;
};

void OnRspQryInstrument_(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    std::cout << "Exchanged: " << pInstrument->ExchangeID << std::endl;
    std::cout << "InstrumentID: " << pInstrument->InstrumentID << std::endl;
    std::cout << "InstrumentName: " << pInstrument->InstrumentName << std::endl;
};

void OnRspUserLogin_(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    std::cout << "OnLogin: " << pRspInfo->ErrorMsg << std::endl;
};

void OnFrontConnected_() {
    std::cout << "Front Connected" << std::endl;
    return ;
};

void OnRtnOrder_(CThostFtdcOrderField *pOrder) {
    std::cout << "OnOrder: " << pOrder->StatusMsg << std::endl;
}

void OnRtnTrade_(CThostFtdcTradeField *pTrade) {
    std::cout << "OnTrade: " << pTrade->TradeType << std::endl;
}

void OnRspOrderInsert_(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    std::cout << "OnErrorOrder: " << pRspInfo->ErrorMsg << std::endl;
}

void OnErrRtnOrderInsert_(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {
    std::cout << "OnErrorOrder: " << pRspInfo->ErrorMsg << std::endl;
}

int main() {
    CThostFtdcTraderApi *api;
    Trade *pSpi;
    
    std::string vern;
    //variable
    // std::string trade_front = "tcp://180.168.146.187:10130";
    std::string trade_front = "tcp://180.168.146.187:10202";
    std::string logdir = "./log/";
    if (access(logdir.c_str(), 0) == -1) {
		mkdir(logdir.c_str(), 0755);
    }
    
    CThostFtdcReqUserLoginField f1 = { 0 };
    strcpy(f1.BrokerID, "9999");
    strcpy(f1.UserID, "008107");
    strcpy(f1.Password, "1");
    
    CThostFtdcReqAuthenticateField f2 = { 0 };
    strcpy(f2.BrokerID, "9999");
    strcpy(f2.UserID, "008107");
    strcpy(f2.AuthCode, "0000000000000000");
    strcpy(f2.AppID, "simnow_client_test");
    
    TThostFtdcSystemInfoLenType nlen = 273;
    TThostFtdcClientSystemInfoType sysinfo = { 0 };

    // FrontAddr=tcp://180.168.146.187:10130
    // FrontMdAddr=tcp://180.168.146.187:10131
    // BrokerID=9999
    // UserID=181101
    // Password=etveritas007
    // InvestorID=181101
    // UserProductInfo=test
    // AuthCode=0000000000000000
    // AppID=simnow_client_test
    // InstrumentID=ag2301
    // ExchangeID=SHFE
    // bIsUsingUdp=1
    // bIsMulticast=0
    
    CThostFtdcQryInstrumentField f3 = { 0 };

	CThostFtdcInputOrderField f4 = { 0 };
	strcpy(f4.BrokerID, "9999");
	strcpy(f4.InvestorID, "008107");
	strcpy(f4.InstrumentID, "SA305");
	strcpy(f4.UserID, "008107");
	f4.CombOffsetFlag[0] = THOST_FTDC_OF_Open;
	f4.CombHedgeFlag[0] = THOST_FTDC_HF_Speculation;
	strcpy(f4.ExchangeID, "CZCE");
	f4.VolumeTotalOriginal = 10;
	f4.IsAutoSuspend = 0;
	f4.IsSwapOrder = 0;
	f4.OrderPriceType = THOST_FTDC_OPT_LimitPrice;
	f4.Direction = THOST_FTDC_D_Buy;
	f4.TimeCondition = THOST_FTDC_TC_IOC;
	f4.VolumeCondition = THOST_FTDC_VC_AV;
	f4.ContingentCondition = THOST_FTDC_CC_Immediately;
	f4.ForceCloseReason = THOST_FTDC_FCC_NotForceClose;
	f4.LimitPrice = 2670;
	f4.StopPrice = 0;
    
   // C++ API
   api = CThostFtdcTraderApi::CreateFtdcTraderApi(logdir.c_str());
   pSpi = new Trade();
   vern = std::string((char *)api->GetApiVersion());
   std::cout << vern << std::endl;
   // instantiate
   pSpi->OnFrontConnected_ = (void *)OnFrontConnected_;
   pSpi->OnRspAuthenticate_ = (void *)OnRspAuthenticate_;
   pSpi->OnRspQryInstrument_ = (void *)OnRspQryInstrument_;
   pSpi->OnRspUserLogin_ = (void *)OnRspUserLogin_;

   api->RegisterSpi(pSpi);
   api->SubscribePublicTopic(THOST_TERT_RESUME);
   api->SubscribePrivateTopic(THOST_TERT_RESUME);
   api->RegisterFront(const_cast<char *>(trade_front.c_str()));
   api->Init();
   while (api->ReqAuthenticate(&f2, 1) != 0) {
       std::cout << "Retry Auth" << std::endl;
       sleep(2);
   }

   while(api->ReqUserLogin(&f1, 2, nlen, sysinfo) != 0) {
       std::cout << "Retry Login" << std::endl;
       sleep(2);
   }

   while (api->ReqQryInstrument(&f3, 3) != 0) {
       std::cout << "Retry QryInst" << std::endl;
       sleep(2);
   }
   std::cout << "Get" << std::endl;
//    api->Join();
//   sleep(30);
//    api->Release();

//     // C API
//     api = (CThostFtdcTraderApi *)tCreateApi(logdir.c_str());
//     pSpi = (Trade *)tCreateSpi();
//     tOnFrontConnected(pSpi, (void *)(OnFrontConnected_));
//     tOnRspAuthenticate(pSpi, (void *)(OnRspAuthenticate_));
//     tOnRspQryInstrument(pSpi, (void *)(OnRspQryInstrument_));
//     tOnRspUserLogin(pSpi, (void *)(OnRspUserLogin_));
//     tOnRtnOrder(pSpi, (void *)(OnRtnOrder_));
//     tOnRtnTrade(pSpi, (void *)(OnRtnTrade_));
//     tOnRspOrderInsert(pSpi, (void *)(OnRspOrderInsert_));
//     tOnErrRtnOrderInsert(pSpi, (void *)(OnErrRtnOrderInsert_));
//     vern = std::string((char *)tGetApiVersion());

//     tRegisterSpi(api, pSpi);
//     tSubscribePrivateTopic(api, THOST_TERT_RESUME);
//     tSubscribePublicTopic(api, THOST_TERT_RESUME);
//     tRegisterFront(api, const_cast<char *>(trade_front.c_str()));
//     tInit(api);
//     while (tReqAuthenticate(api, &f2, 1) != 0) {
//         std::cout << "Retry Auth" << std::endl;
//         sleep(2);
//     }
// #ifdef __APPLE__
//     while (tReqUserLogin(api, &f1, 1, nlen, sysinfo) != 0) {
// #else
//     while (tReqUserLogin(api, &f1, 1) != 0) {
// #endif
//         std::cout << "Retry Login" << std::endl;
//         sleep(2);
//     }
//     while (tReqQryInstrument(api, &f3, 1) != 0) {
//         std::cout << "Retry QryInstrument" << std::endl;
//         sleep(2);
//     }
//    tJoin(api);
    // while (tReqOrderInsert(api, &f4, 1) != 0) {
    //     std::cout << "Retry Order" << std::endl;
    //     sleep(2);
    // }
//    sleep(60);

}
