package ctpapi

import (
	"strings"

	"golang.org/x/text/encoding/simplifiedchinese"
)

func Bytes2String(t []byte) string {
	var idx int
	for k, v := range t {
		if v == 0 {
			idx = k
			break
		}
	}
	msg, _ := simplifiedchinese.GB18030.NewDecoder().Bytes(t[:idx])
	return strings.Trim(string(msg), "\u0000")
}
