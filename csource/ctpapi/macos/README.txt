1. 说明

本次SDK更新主要内容(相比上一个发布的版本)：新增了8个查询接口，具体说明请查看changelog文件。

2. 开发环境要求

开发者需要配置Xcode开发环境，否则采集模块可能无法正常使用。

3. 操作系统要求

要求操作系统为MacOS 10.12以上版本。

4. 应用权限配置

信息采集模块采集信息时，需要应用具备某些权限。若应用不具备某些权限，
可能会导致获取到对应的采集项为空。因此在使用信息采集模块前， 请使用者申请权限。
包括允许应用访问网络权限。


5. 支持架构

目前SDK支持x86_64和arm64。

6. 如何使用API和采集模块

将交易api和行情api以及信息采集模块导入项目中。


7. 常见问题：

 7.1. 信息采集模块获取信息失败；
请检查项目中是否引入了openssl静态库，采集模块包含了openssl静态库，可能会引起冲突，
解决方案：移除项目中的其他openssl静态库。

 7.2. 项目中引入行情API导致交易API无法正常使用；
是由于API版本不一致导致的，请使用同一个版本的交易API和行情API。






