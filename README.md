# ChemDB
#####_Chemicals DataBase for laboratories._
ChemDB is a very easy to use software wich allow you to manage your chemical database.
Most of the laboratories at universities use an archaic Excel file to manage their chemicals. But most of them are not up to date and inventories can be very difficult. With ChemDB, you can import your data from an Excel file to ChemDB's database. Moreover, you can reverse the data to an Excel file.

## Installing ChemDB
### One Client or "Server" ?
ChemDB is mostly used to be a single client with a single software wich mean you cannot really use it with multiple posts and one server. But if you put your database in a dropbox or an equivalent system or an ftp server, you will be able to connect a single database with multiple clients

### Instaling
#### Easy Mode
To install ChemDB easily just download the last release (for Mac or PC (comming soon)) directly [here](https://github.com/dedichan/ChemDB/releases).

#### Heroic Mode
You can also, of course, download the repository and compile it by yourself. For that, you will need Python 3 (3.4 or higher highly recommanded) and the folling dependencies :
* sqlite3 - SQLite Databse Reader (normaly included in your Python instalation)
* PyQt5 - Interface (you will need a proper Qt5 instalation to build it)
* xlwt - Excel Writer 
* xlrd - Excel Reader 

Compilation recommanded with py2app, py2exe or linux equivalent. Do NOT use PyInstaller, it is highly unstable with PyQt5.
Do not forget to include the "data" folder during compilation.

### First Launch
#### New Database and importing from Excel
If you start the software with no "sqlite" database, you will be asked to create a new one (if you plan to make it as "server", do not forget to put the file in a shared folder or the dropbox, other client will have to use the "load an existing DB" and point to the file previously created).
The newly created DB is absolutly empty. If you try to create a new elementyou will see in the botom that the "ID" is "1" and you can't modify it. In fact, ChemDB always create a new item as the highest ID stored plus one. But there is exceptions. There is already an item stored as id "-1" in the database and you can't modify it (unless you want the software to be unusable). Also, the id "0" is protected and cannot be used.

If you want to import your data from Excel, you hava to modify you sheet in order to satisfy with ChemDB importing syntax :

| X  | A  | B  | C |D |E |F |G |H |
| --------|---------|-------|-------|-------|-------|-------|-------|-------|
| 1  | Name   | Vendor    | Id Vendor Catalog    |  CAS   |Size    | Storage    | Room    | Id    |
| 2 | X | X    | X    | X    | X    | X    | X    | 1    |
| 3 |  X | X    | X    | X    | X    | X    | X    | 2    |
| ... | ... |... |... |... |... |... |... |... |
| n |  X | X    | X    | X    | X    | X    | X    | n    |

It is really important that you follow this order for columns and no one is missing (even if you never used that information). Note that the first line of you sheet will be IGNORED by the software. Name, vendor, id vendor, etc... are noted here to help you modifying your Excel file. Moreover, we higly recommand that there is an absolute continuity in your file with no empty line. In addition, you have to manually complete all the ID column starting from 1 untill the last line with no interruption. Also, it is very important that the document is empty after the last line, otherwise, the software will make useless imports.

When you are sure your Excel file complain with the requirements, use "Repopulate" and let the software take your data (it may take a long time if your files contain a lot of data).
