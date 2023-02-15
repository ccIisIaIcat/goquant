/*
 * @Author: Wavy Wei 
 * @Date: 2022-12-12 14:21:36 
 * @Last Modified by: Wavy Wei
 * @Last Modified time: 2022-12-12 18:42:33
 */

package ctpapi

type THOST_TE_RESUME_TYPE = int32

const (
	THOST_TERT_RESTART THOST_TE_RESUME_TYPE = 0
	THOST_TERT_RESUME THOST_TE_RESUME_TYPE = 1
	THOST_TERT_QUICK THOST_TE_RESUME_TYPE = 2
	THOST_TERT_NONE THOST_TE_RESUME_TYPE = 3
)

[[ range .St]]// [[ .Comment ]]
type [[ .FuncName ]] = [[ .FuncTypeName|baseType ]]
[[ range .FuncFields ]]const [[ .FieldType ]] = [[ if eq (len .FieldName) 1 ]]'[[ .FieldName ]]'[[ else ]]"[[ .FieldName ]]"[[ end ]] // [[ .Comment ]]
[[ end ]]
[[ end ]]
