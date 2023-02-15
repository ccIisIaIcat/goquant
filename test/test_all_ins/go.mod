module all_ins

require allinsts_query v0.0.1

require (
	ctpapi v0.0.5 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	golang.org/x/text v0.5.0 // indirect
	gopkg.in/ini.v1 v1.67.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

replace allinsts_query => ../../gosource/query/allinsts_query

replace ctpapi => ../../gosource/ctpapi

go 1.19
