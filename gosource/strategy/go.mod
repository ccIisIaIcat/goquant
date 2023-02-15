module strategy

require global v0.0.1

require gopkg.in/ini.v1 v1.67.0 // indirect

replace global => ../global

require zigzag v0.0.1

replace zigzag => ../indicator/zigzag

require fabo v0.0.1

replace fabo => ../signal/fabo

require genbar v0.0.1

replace genbar => ../../gosource/genbar

go 1.19
