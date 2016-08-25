from .common import parser
from . import asm
from . import checksec
from . import common
from . import constgrep
from . import cyclic
from . import disasm
from . import elfdiff
from . import elfpatch
from . import errno
from . import hex
from . import phd
from . import pwnstrip
from . import scramble
from . import shellcraft
from . import unhex

commands = {
    'asm': asm.main,
    'checksec': checksec.main,
    'constgrep': constgrep.main,
    'cyclic': cyclic.main,
    'disasm': disasm.main,
    'elfdiff': elfdiff.main,
    'elfpatch': elfpatch.main,
    'errno': errno.main,
    'hex': hex.main,
    'phd': phd.main,
    'pwnstrip': pwnstrip.main,
    'scramble': scramble.main,
    'shellcraft': shellcraft.main,
    'unhex': unhex.main,
}

def main():
    args = parser.parse_args()
    commands[args.command](args)

if __name__ == '__main__':
    main()
