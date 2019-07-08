
class INI:
    def __init__(self,s):
        """in this class we convert the string to INI object
        """

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
        """Checks whether the given line represents a key value pair.
        Arguments:
            line {str} -- the line to be checked
        Returns:
            bool -- true if the line is unindented, in the form key = value \
            and the key doesn't contain the character ;
        """
        pos = line.find('=')
        return pos != -1 and line[0:pos].find('=') == -1 and line[0:pos].find(';') == -1

    def is_section(self, line):
        """Checks whether the given line represents a section.
        Arguments:
            line {str} -- the line to be checked
        Returns:
            bool -- true if the line is unindented, in the form [section]\
            and section doesn't contain the character ']'
        """
        if len(line)>1:
            return line[0] == '[' and line[-1] == ']' and line[1:-1].find(']') == -1
        else:
            return False
    def is_comment(self, line):
        """Checks whether the given line represents a comment.
        Arguments:
            line {str} -- the line to be checked
        Returns:
            bool -- true if the line is unindented and starts with ; and #
        """
        return len(line) > 0 and (line[0] == ';' or line[0] == '#')

    def is_empty(self, line):
        """Checks whether the given line is empty.
        Arguments:
            line {str} -- the line to be checked
        Returns:
            bool -- true if the line is empty
        """
        return len(line) == 0
    def add_section(self,name):
        """Add an empty section to the dict
        Arguments:
            name {str} -- the name of the section
        """
        self.dict[name]={}
    def get_properity(self,secName,k):
        """Checks whether the given line is empty.
        Arguments:
            secName {str} -- the Name of the section which contain the property
            k {str} -- the key of the property
        Returns:
            str -- the property
        """
        keyvalDict=self.dict[secName]
        return keyvalDict[k]
    def has_properity(self,secName,k):
        """Checks whether there is a property for a given section
        Arguments:
            secName {str} -- the Name of the section which contain the property
            k {str} -- the key of the property
        Returns:
            bool -- true if there is a property
        """
        if secName in self.dict:
            keyvalDict=self.dict[secName]
            return k in keyvalDict
        else:
            return False

if __name__ == '__main__':
    """here our program starts
    """
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
