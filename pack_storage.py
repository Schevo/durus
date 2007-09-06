#!/www/python/bin/python
"""
$URL: svn+ssh://svn.mems-exchange.org/repos/trunk/durus/pack_storage.py $
$Id: pack_storage.py 27076 2005-07-25 17:41:30Z dbinger $
"""
from durus.client_storage import ClientStorage
from durus.connection import Connection
from durus.file_storage import FileStorage
from durus.storage_server import DEFAULT_PORT, DEFAULT_HOST, wait_for_server
from optparse import OptionParser

def pack_storage_main():
    parser = OptionParser()
    parser.set_description("Packs a Durus storage.")
    parser.add_option(
        '--file', dest="file", default=None,
        help="If this is not given, the storage is through a Durus server.")
    parser.add_option(
        '--port', dest="port", default=DEFAULT_PORT,
        type="int",
        help="Port the server is on. (default=%s)" % DEFAULT_PORT)
    parser.add_option(
        '--host', dest="host", default=DEFAULT_HOST,
        help="Host of the server. (default=%s)" % DEFAULT_HOST)
    (options, args) = parser.parse_args()
    if options.file is None:
        wait_for_server(options.host, options.port)
        storage = ClientStorage(host=options.host, port=options.port)
    else:
        storage = FileStorage(options.file)
    connection = Connection(storage)
    connection.pack()

if __name__ == '__main__':
    pack_storage_main()
