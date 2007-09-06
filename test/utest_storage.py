"""
$URL: svn+ssh://svn.mems-exchange.org/repos/trunk/durus/test/utest_storage.py $
$Id: utest_storage.py 29090 2006-11-27 14:02:24Z dbinger $
"""
from sancho.utest import UTest, raises
from durus.storage import MemoryStorage
from durus.serialize import pack_record
from durus.utils import int8_to_str

class Test (UTest):

    def check_memory_storage(self):
        b = MemoryStorage()
        assert b.new_oid() == int8_to_str(0)
        assert b.new_oid() == int8_to_str(1)
        assert b.new_oid() == int8_to_str(2)
        raises(KeyError, b.load, int8_to_str(0))
        record = pack_record(int8_to_str(0), 'ok', '')
        b.begin()
        b.store(int8_to_str(0), record)
        b.end()
        b.sync()
        b.begin()
        b.store(int8_to_str(1), pack_record(int8_to_str(1), 'no', ''))
        b.end()
        assert len(list(b.gen_oid_record())) == 1
        assert record == b.load(int8_to_str(0))
        records = b.bulk_load([int8_to_str(0), int8_to_str(1)])
        assert len(list(records)) == 2
        records = b.bulk_load([int8_to_str(0), int8_to_str(1), int8_to_str(2)])
        raises(KeyError, list, records)

if __name__ == "__main__":
    Test()

