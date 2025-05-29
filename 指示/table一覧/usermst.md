

## usermstテーブル

| 項目名                   | 型           | 主キー      | NOT NULL |
| ----------------------- | ------------ | ---------- | -------- |
| usercd                  | nvarchar(8)  | PRIMARYKEY |          |
| user_f_name             | nvarchar(50) |            | NOT NULL |
| user_l_name             | nvarchar(50) |            | NOT NULL |
| belonged_companycd      | nvarchar(4)  |            | NOT NULL |
| belonged_deptcd         | nvarchar(4)  |            | NOT NULL |
| authcd                  | nvarchar(2)  |            | NOT NULL |
| activeflg               | boolean      |            | NOT NULL |
| created_by              | nvarchar(8)  |            | NOT NULL |
| created_date            | datetime     |            | NOT NULL |
| updated_by              | nvarchar(8)  |            | NOT NULL |
| updated_date            | datetime     |            | NOT NULL |
| updatecounter           | number       |            | NOT NULL |

## Froegin key
| 項目名                   | 参照テーブル   | 参照項目     |
| ----------------------- | ------------ | ---------- |
| belonged_companycd      | companymst   | companycd  |
| belonged_deptcd         | deptmst      | deptcd     |