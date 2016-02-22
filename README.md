# ChemDB
#####_Chemicals DataBase for laboratories._
ChemDB is a very easy to use software which allow you to manage your chemical database.
Most of the laboratories at universities use an archaic Excel file to manage their chemicals, but most of them are not up to date and inventories can be very difficult. With ChemDB, you can import your data from an Excel file to an optimized database. Moreover, you can reverse the data to an Excel file if needed.

## Installing ChemDB
### One Client or "Server" ?
ChemDB is mostly used to be a single client with a single software which mean you cannot really use it with multiple posts and one server. But if you put your database in a dropbox or an equivalent system or an ftp server, you will be able to connect a single database with multiple clients

### Instaling
#### Easy Mode
To install ChemDB easily just download the latest release (for Mac or PC) directly [here](https://github.com/dedichan/ChemDB/releases).

#### Heroic Mode
You can also, of course, download the repository and compile it by yourself. For that, you will need Python 3 (3.4 or higher highly recommended) and the following dependencies :
* sqlite3 - SQLite Database Reader (usually included in your Python installation)
* PyQt5 - Interface (you will need a proper Qt5 installation to build it)
* xlwt - Excel Writer 
* xlrd - Excel Reader 

Compilation recommended with py2app, py2exe or linux equivalent. Do NOT use PyInstaller, it is highly unstable with PyQt5.
Do not forget to include the "data" folder during compilation but "setup_osx.py" and "setup_win.py" are a base for configuration.

`python3 setup_osx.py py2app`
`python setup_win.py py2exe`

## Using ChemDB
### First Launch
#### New Database and importing from Excel
If you start the software with no "sqlite" database, you will be asked to create a new one (if you plan to make it as "server", do not forget to put the file in a shared folder or the dropbox, other client will have to use the "load an existing DB" and point to the file previously created).
The newly created DB is absolutely empty. If you try to create a new element you will see in the bottom that the "ID" is "1" and you can't modify it. In fact, ChemDB always create a new item as the highest ID stored plus one. But there is exceptions. There is already an item stored as id "-1" in the database and you can't modify it (unless you want the software to be unusable). Also, the id "0" is protected and cannot be used.

If you want to import your data from Excel, you hava to modify you sheet in order to satisfy with ChemDB importing syntax :

|   | A  | B  | C |D |E |F |G |H |
| --------|---------|-------|-------|-------|-------|-------|-------|-------|
| 1  | Name   | Vendor    | Id Vendor Catalog    |  CAS   |Size    | Storage    | Room    | Id    |
| 2 | X | X    | X    | X    | X    | X    | X    | 1    |
| 3 |  X | X    | X    | X    | X    | X    | X    | 2    |
| ... | ... |... |... |... |... |... |... |... |
| n |  X | X    | X    | X    | X    | X    | X    | n+1    |

It is really important that you follow this order for columns and no one is missing (even if you never used that information). Note that the first line of you sheet will be IGNORED by the software. Name, vendor, id vendor, etc... are noted here to help you modifying your Excel file. Moreover, we highly recommend that there is an absolute continuity in your file with no empty line. In addition, you have to manually complete all the ID column starting from 1 until the last line with no interruption. Also, it is very important that the document is empty after the last line, otherwise, the software will make useless imports.

When you are sure your Excel file complain with the requirements, use "Repopulate" and let the software take your data (it may take a long time if your files contain a lot of data).

#### Common use and Inventory

While the use of the program is mostly intuitive, some options have to be clarified. If you search a Chemical by ID, CAS or Vendor ID, the program will automatically give you the first item the research give you. Nevertheless, if you search by name, it will give you the first hundred record found (you will have to pick up one from the list) and inform you if more than hundred were found.

If you want to delete entries, simply go do "Delete Entries" and enter in the field each "id" separated by commas. 

eg : 1,9,6,98,154

Inventory can be made by two ways : full or group. The full version give you back a list of all the chemicals in one sheet through an Excel file. Note that this excel file is suitable for "repopulate". The "group" mode give you an excel file with one sheet for every storage location which can be useful during inventory time.

#### Advanced Use

"Manual CMD" give you the possibility to interact directly with the database through SQL command. Note that even if this tool can be very powerful, a bad use can lead to a dramatic failure for the database. But, it can also make you change all the names of a room. The structure of the db is given :

Table : chem

Fields (in order) : name / vendor / vpid / cas / size / storage / room / id

## Known bugs and future versions 

Bugs :
* Using "Manual CMD" may crash the program with no loosing data
* Deleting the database may make the program spamming the same error message the first time you open it after

Future Versions :
* Auto-Update
* One research field and research for all field types
* Better interface
* Unicorns
