
class INI:
    def __init__(self,s):
        self.dict={}
        secName=""
        for line in s.split("\n"):
            line=line.strip()
            if self.is_comment(line) or self.is_empty(line):
                continue
            elif self.is_section(line):
                secName=line[1:-1]
                self.add_section(secName)
            elif self.is_keyval(line):
                keyvalDict=self.dict[secName]
                keyvalDict[line.split('=')[0].strip()]=line.split('=')[1].strip()
                self.dict[secName]=keyvalDict
            else:
                raise Exception("Can't process line {}".format(line))

    def is_keyval(self, line):
        pos = line.find('=');
        return pos != -1 and line[0:pos].find('=') == -1 and line[0:pos].find(';') == -1

    def is_section(self, line):
        if len(line)>1:
            return line[0] == '[' and line[-1] == ']' and line[1:-1].find(']') == -1
        else:
            return False
    def is_comment(self, line):
        return len(line) > 0 and (line[0] == ';' or line[0] == '#')

    def is_empty(self, line):
        return len(line) == 0
    def add_section(self,name):
        self.dict[name]={}
    def get_properity(self,secName,k):
        keyvalDict=self.dict[secName]
        return keyvalDict[k]
    def has_section(self,secName):
        return  secName in self.dict
    def has_properity(self,secName,k):
        if secName in self.dict:
            keyvalDict=self.dict[secName]
            return k in keyvalDict
        else:
            return False

if __name__ == '__main__':
    sample1 = """
    [general]
    appname = configparser
    version=0.1
      [author]
    name =xmonader
    email =notxmonader@gmail.com
    """
    ini = INI(sample1)
    print(ini.get_properity("general", "appname"))
    print(ini.has_properity("author", "name"))
    print(ini.has_properity("author", "pass"))
