module trade_test

go 1.19

require gopkg.in/ini.v1 v1.67.0

require (
	github.com/stretchr/testify v1.8.1 // indirect
	golang.org/x/text v0.5.0 // indirect
)

require ctpapi v0.0.5

replace ctpapi => ../../gosource/ctpapi
