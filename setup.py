# Этот скрипт содержит настройки, которые позволяют подключиться к базе данных
# Для того, чтобы подключиться к своей БД, вам достаточно поменять значения переменных в этом файле

# Параметры базы данных.
DRIVERNAME =  'postgresql'
USERNAME =  'postgres'
PASSWORD =  '*****'
HOST =  'localhost'
PORT =  5432
DATABASENAME = 'postgres'

# Названия таблиц в базе данных. Так как в рамках проектах была использована локальная база данных, 
# названия таблиц соответствуют названиям файлов с данными. У вас могут отличаться названия таблиц, 
# потому вы можете поменять значения переменных

CITIES = 'cities15000'
ALTERNATE_NAMES = 'alternate_names_v2'
COUNTRY_INFO = 'country_info'
ADMIN_CODES = 'admin1_codes_ascii' 

#Ниже названия созданных вспомогательных таблиц

# Таблица с опциями, которая позволит программе определить, нужно ли делать повторные вычисления.
OPTIONS = 'model_options_table'
# Таблица с веторизованными словами
EMBEDDINGS = 'embeddings_alter_cities'
# Если хотите использовать альтернативные названия стран, взятые из датабазы
ALTERNATE_COUNTRIES = 'my_alter_countryies'

# Названия колонок в таблицах данных. Так как названия колонок в таблицах у заказчика могут отличаться от 
# названий, используемых в проекте, используемые названия в переменных. Заказчик может иметь другие названия столбцов. 
# В этом случае достаточно поменять названия соответствующих переменных.

COUNTRY_COLUMN = 'country' 
COUNTRY_CODE_COLUMN = 'country_code'
NAME_COLUMN = 'name'
GEONAME_ID_COLUMN = 'geoname_id'
ALTERNATE_NAME_COLUMN = 'alternate_name'
ASCII_NAME_COLUMN = 'asciiname'
ADMIN_CODES_COLUMN = 'admin1_code'
ISO_COLUMN = 'iso'
CODE_COLUMN = 'code'
REGION_NAME_ASCII_COLUMN = 'name_ascii'