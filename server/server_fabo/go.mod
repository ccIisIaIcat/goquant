module fabo_server

go 1.19

replace strategy => ../../gosource/strategy

replace trade => ../../gosource/trade/trade

replace genbar => ../../gosource/genbar

replace fabo => ../../gosource/signal/fabo

replace zigzag => ../../gosource/indicator/zigzag

replace general_struct => ../../gosource/global

replace record => ../../gosource/record

replace global => ../../gosource/global

replace ctpapi => ../../gosource/ctpapi

replace mainforce_query => ../../gosource/query/mainforce_query

replace tick_query => ../../gosource/query/tick_query

replace fake => ../../gosource/fake

require (
	global v0.0.1
	mainforce_query v0.0.0-00010101000000-000000000000
	strategy v0.0.0-00010101000000-000000000000
	tick_query v0.0.0-00010101000000-000000000000
	trade v0.0.0-00010101000000-000000000000
)

require (
	ctpapi v0.0.5 // indirect
	fabo v0.0.1 // indirect
	genbar v0.0.1 // indirect
	github.com/PuerkitoBio/goquery v1.8.0 // indirect
	github.com/andybalholm/cascadia v1.3.1 // indirect
	github.com/go-sql-driver/mysql v1.7.0 // indirect
	golang.org/x/net v0.0.0-20211112202133-69e39bad7dc2 // indirect
	golang.org/x/text v0.5.0 // indirect
	gopkg.in/ini.v1 v1.67.0 // indirect
	zigzag v0.0.1 // indirect
)
