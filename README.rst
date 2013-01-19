Beuarg
======

Beuarg is an OpenERP **prototype** code puker (generator). For the moment it's
just a toy with the ability to parse a OpenERP python object file (you know,
what everyone is calling models) and generate standard csv security fixtures.

I'm releasing it because maybe someone might find some of the code interesting
but I'm not sure that I'm going to continue working on it. I've always
considered that when you need to have code generator it's a sign that your
system is broken and that you should fix it instead (well, you could argue that
we are working with OpenERP here). I have a different approach in head right
now to solve this issue so Beuarg might end up only being a parsing lib, I
don't know it yet.

Code is simple and nearly clean if you want to extend it.

Installation
============

    git clone git://github.com/Psycojoker/beuarg.git
    python setup.py install

Haven't pushed on pypi yet.
