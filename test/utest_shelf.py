"""
$URL: svn+ssh://svn.mems-exchange.org/repos/trunk/durus/test/utest_shelf.py $
$Id: utest_shelf.py 29739 2007-04-18 15:02:51Z dbinger $
"""
from StringIO import StringIO
from sancho.utest import UTest, raises
from durus.file import File
from durus.shelf import Shelf
from durus.utils import ShortRead, int8_to_str

class ShelfTest (UTest):

    def a(self):
        f = File()
        s = Shelf(f)
        name1 = s.next_name()
        name2 = s.next_name()
        assert name1 != name2
        r = s.store([(name1, name1 + name1), (name2, name2 + name2)])
        assert s.get_value(name1) == name1 + name1, (name1, s.get_value(name1))
        assert s.get_value(name2) == name2 + name2
        f.seek(0)
        other = Shelf(f)
        names = sorted(other.__iter__())
        index = sorted(other.iterindex())
        items = sorted(other.iteritems())
        assert names == [name1, name2], (name1, name2, names)
        assert items == [(n, n+n) for n in names]
        assert index == [(n, other.get_position(n)) for n in names]

    def b(self):
        s = Shelf()
        assert s.get_value('okokokok') is None
        assert raises(ValueError, s.get_value, 'okok')

    def c(self):
        f = File()
        s = Shelf(f)
        f.seek(0)
        p = Shelf(f)
        f.seek(0)
        q = Shelf(f)

    def d(self):
        s = StringIO('nope')
        assert raises(AssertionError, Shelf, s)
        s = StringIO("SHELF-1\nbogus")
        assert raises(ShortRead, Shelf, s)

    def e(self):
        f = File()
        n1 = int8_to_str(0)
        n2 = int8_to_str(1)
        s = Shelf(f, items=[(n1, 'record1'), (n2, 'record2')])


if __name__ == '__main__':
    ShelfTest()

