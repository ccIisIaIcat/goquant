//
//  ctptrade_api.cpp
//  ctptrade_api
//
//  Created by Wavy Wei on 2022/12/17.
//

#include <iostream>
#include "ctptrade_api.hpp"
#include "ctptrade_apiPriv.hpp"

void ctptrade_api::HelloWorld(const char * s)
{
    ctptrade_apiPriv *theObj = new ctptrade_apiPriv;
    theObj->HelloWorldPriv(s);
    delete theObj;
};

void ctptrade_apiPriv::HelloWorldPriv(const char * s) 
{
    std::cout << s << std::endl;
};

