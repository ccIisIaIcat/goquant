package main

/*
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef char arr1[11];
typedef char arr2[11];

struct tmp {
	arr1 et1;
	arr2 et2;
};

void testst(struct tmp *a1) {
	a1->et1[0] = 'A';
	a1->et2[0] = 'B';
}

void print(char *a) {
	printf("%s\n", a);
}

void print1(char **a) {
	printf("%s\n", a[0]);
}

int num1() {
	return 2;
}
*/
import (
	"C"
)
import (
	"fmt"
	"unsafe"
)

type TThostFtdcClientSystemInfoType [273]byte

type tmp struct {
	et1 [11]byte
	et2 [11]byte
}

func main() {
	quoteFront := "tcp://180.168.146.187:10131"
	// bquoteFront := []byte(quoteFront)
	// bquoteFront := C.CString(quoteFront)
	var tmp1 TThostFtdcClientSystemInfoType
	copy(tmp1[:], quoteFront)
	var rev string
	rev = string(tmp1[:])
	fmt.Println(rev)
	// fmt.Println(tmp1)
	instruments := make([]string, 0)
	instruments = append(instruments, "rb2305")
	ppInstrumentID := make([]*C.char, len(instruments)) // [][]byte{[]byte(instrument)}
	for i := 0; i < len(instruments); i++ {
		ppInstrumentID[i] = (*C.char)(unsafe.Pointer(C.CBytes([]byte(instruments[i]))))
	}

	front := C.CString(quoteFront)
	C.print((*C.char)(front))
	C.print((*C.char)(unsafe.Pointer(&tmp1[0])))
	C.print((*C.char)(unsafe.Pointer(&tmp1)))
	C.print1((**C.char)(&ppInstrumentID[0]))

	// (*CThostFtdcRspUserLoginField)(unsafe.Pointer(pRspUserLogin))
	//  * C.struct_tmp
	st := tmp{}
	C.testst((*C.struct_tmp)(unsafe.Pointer(&st)))
	fmt.Println(string(st.et1[:]))
	fmt.Println(string(st.et2[:]))
	fmt.Println(rnum())
	// 地址测试
	// fmt.Println((*C.char)(unsafe.Pointer(&pszFrontAddress)))
	// fmt.Println(unsafe.Pointer(&pszFrontAddress))
	// fmt.Println(fmt.Sprintf("%p", &pszFrontAddress))
}

func rnum() int {
	res := C.num1()
	return int(res)
}
