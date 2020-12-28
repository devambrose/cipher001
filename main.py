import tkinter
import _tkinter
import database
from Crypto.Cipher import AES
from Crypto import Random
db_name='sqlite.db'

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

print(key)
conn=database.create_connection(db_name)

if conn is not None:
    print("database connection is succesfull")

else:
    print("unable to connect")