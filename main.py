import re
import subprocess as sp

with open('input.lua', 'r') as fr:
    pat = r';end return (\w+)\((\w+)\(\)\s*,\s*\{\}\s*,\s*(\w+)\)\([^)]*\);end return (\w+)\("LOL!([^"]+)",(\w+)\(\)\s*,\s*\.\.\.\);'

    rep = r''';end local test
    --[[test = function(t)
        for i, x in pairs(t) do
            print(i,tostring(x))
            if type(x) == "table" then
                test(x)
            end
        end
    end
    test(\2())]]



    local ffi = require "ffi" -- ty stackoverflow for the writefile code

    ffi.cdef[[
        typedef struct {
        char *fpos;
        void *base;
        unsigned short handle;
        short flags;
        short unget;
        unsigned long alloc;
        unsigned short buffincrement;
        } FILE;

        FILE *fopen(const char *filename, const char *mode);
        int fprintf(FILE *stream, const char *format, ...);
        int fclose(FILE *stream);
    ]]

    local f = ffi.C.fopen("./output.json", "a+")
    ffi.C.fprintf(f, require("json").encode(\2()))
    ffi.C.fclose(f)

    

    end \4("LOL!\5",\6(),...)
    '''

    with open('output.lua', 'w') as fw:
        fw.write(re.sub(pat, rep, fr.read()))

sp.run(['luajit', 'output.lua'])