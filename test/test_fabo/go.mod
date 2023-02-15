module fabo_test

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
	genbar v0.0.0-00010101000000-000000000000
	global v0.0.1
	mainforce_query v0.0.0-00010101000000-000000000000
	record v0.0.0-00010101000000-000000000000
	strategy v0.0.0-00010101000000-000000000000
	tick_query v0.0.0-00010101000000-000000000000
	trade v0.0.0-00010101000000-000000000000
)

require (
	ctpapi v0.0.5 // indirect
	fabo v0.0.1 // indirect
	github.com/PuerkitoBio/goquery v1.8.0 // indirect
	github.com/andybalholm/cascadia v1.3.1 // indirect
	github.com/go-sql-driver/mysql v1.7.0 // indirect
	github.com/golang/snappy v0.0.1 // indirect
	github.com/klauspost/compress v1.13.6 // indirect
	github.com/montanaflynn/stats v0.0.0-20171201202039-1bf9dbcd8cbe // indirect
	github.com/pkg/errors v0.9.1 // indirect
	github.com/xdg-go/pbkdf2 v1.0.0 // indirect
	github.com/xdg-go/scram v1.1.1 // indirect
	github.com/xdg-go/stringprep v1.0.3 // indirect
	github.com/youmark/pkcs8 v0.0.0-20181117223130-1be2e3e5546d // indirect
	go.mongodb.org/mongo-driver v1.11.1 // indirect
	golang.org/x/crypto v0.0.0-20220622213112-05595931fe9d // indirect
	golang.org/x/net v0.0.0-20211112202133-69e39bad7dc2 // indirect
	golang.org/x/sync v0.0.0-20210220032951-036812b2e83c // indirect
	golang.org/x/text v0.5.0 // indirect
	gopkg.in/ini.v1 v1.67.0 // indirect
	zigzag v0.0.1 // indirect
)
