#i/urs/bin/python3.11
try:
    __Mrx_Ewan_Xabat__=locals()
    __Owner__ = 'Mrx Ewan Xabat'
    __Date_Obf__ = '2024-01-01 - Admin (UTC)'
    __Mode_ENC__  = '3.11.6 -> (main) - version: 1.0.1'
    __OBFUSCATION_BY__ = 'Mrx Ewan Xabat'
    class PyObject:
        def PythonCodeObject(code: int) -> int:return code*2
        def Obfuscator(code_, _code: (...,)) -> (...,):__Mrx_Ewan_Xabat__[code_] = _code;return __Mrx_Ewan_Xabat__[code_]
        def Windows(code):
            code_ = []
            while code:
                Mrx_Ewan_Xabat = __import__('_bz2').BZ2Decompressor()
                try:__Mrx_Ewan_Xabat__=Mrx_Ewan_Xabat.decompress;_code = __Mrx_Ewan_Xabat__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Mrx_Ewan_Xabat.unused_data
            return b"".join(code_)
        def KaliLinux(code, format=__import__('_lzma').FORMAT_AUTO, memlimit=None, filters=None):
            code_ = []
            while True:
                Mrx_Ewan_Xabat = __import__('_lzma').LZMADecompressor(format, memlimit, filters)
                try:__Mrx_Ewan_Xabat__=Mrx_Ewan_Xabat.decompress;_code = __Mrx_Ewan_Xabat__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Mrx_Ewan_Xabat.unused_data
                if not code:break
            return b"".join(code_)
    __import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())