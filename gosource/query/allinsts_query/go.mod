module allinsts_query

go 1.19

require (
	ctpapi v0.0.5
	global v0.0.0-00010101000000-000000000000
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	golang.org/x/text v0.5.0 // indirect
	gopkg.in/ini.v1 v1.67.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

replace ctpapi => ../../ctpapi

replace global => ../../global

replace mainforce_query => ../../gosource/query/mainforce_query
