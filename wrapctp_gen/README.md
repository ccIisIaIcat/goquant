# Generate

__For C and platform__

```
go run wrapper_gen.go -csys macos -lang c -outpath ../csource/src/wrapper_ctp/macos

go run wrapper_gen.go -csys windows -lang c -outpath ../csource/src/wrapper_ctp/windows

go run wrapper_gen.go -csys linux -lang c -outpath ../csource/src/wrapper_ctp/linux
```

__For Python and platform__

```
go run wrapper_gen.go -csys macos -lang python -outpath ../pysource/CtpApi/macos

go run wrapper_gen.go -csys windows -lang python -outpath ../pysource/CtpApi/windows

go run wrapper_gen.go -csys linux -lang python -outpath ../pysource/CtpApi/linux
```

__For Golang and platform__

```
go run wrapper_gen.go -csys macos -lang golang -outpath ../gosource/ctpapi/

go run wrapper_gen.go -csys windows -lang golang -outpath ../gosource/ctpapi/

go run wrapper_gen.go -csys linux -lang golang -outpath ../gosource/ctpapi/
```
