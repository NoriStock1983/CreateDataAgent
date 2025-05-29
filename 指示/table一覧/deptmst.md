## deptmstテーブル
| 項目名                     | 型            | 主キー        | NOT NULL |
| ----------------------- | ------------ | ---------- | -------- |
| deptcd                  | nvarchar(4)  | PRIMARYKEY |          |
| companycd               | nvarchar(3)  | PRIMARYKEY | NOT NULL |
| deptnm                  | nvarchar(10) |            | NOT NULL |
| deptnm_short            | nvarchar(2)  |            | NOT NULL |
| created_by              | nvarchar(8)  |            | NOT NULL |
| created_date            | datetime     |            | NOT NULL |
| updated_by              | nvarchar(8)  |            | NOT NULL |
| updated_date            | datetime     |            | NOT NULL |
| updatecounter           | number       |            | NOT NULL |

## Froegin key
| 項目名                   | 参照テーブル   | 参照項目     |
| ----------------------- | ------------ | ---------- |
| companycd               | companymst   | companycd  |