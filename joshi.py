#!/usr/bin/env python3

from argparse import ArgumentParser
import sys,re
from octopus.server.DBInterface import DBInterface

class JoshiApp:
    def __init__(self):
        parser = ArgumentParser()
        parser.add_argument('-p','--project',help='project to execute')
        parser.add_argument('-r','--raw',action='store_true',default=False,help='do not convert response data to string.')
        parser.add_argument('--no-json',action='store_true',default=False,help='disable json encoding for response')
        parser.add_argument('file',help='execute script from file instead of stdin')
        self.args = parser.parse_args()
    @staticmethod
    def _matchShebang(l):
        m = re.match(r'#!',l)
        return m
    @staticmethod
    def _matchInclude(l):
            m = re.match(r'^#include (.*)$',l)
            if m: return m.group(1)
            return None
    @staticmethod
    def _parseScript(f):
        lines = []
        for l in f.readlines():
            l = l.rstrip('\r\n')
            m = __class__._matchShebang(l)
            if m:
                continue
            m = __class__._matchInclude(l)
            if m:
                incf = open(m,"r")
                inclines = __class__._parseScript(incf)
                lines.extend(inclines)
                continue
            lines.append(l)
        return lines
    def run(self):
        if self.args.file != None:
            f = open(self.args.file,"r")
        else:
            f = sys.stdin
        lines = __class__._parseScript(f)
        query = "\n".join(lines)
        db = DBInterface()
        if self.args.no_json:
            db.disable_json()
        db.connectToDatabase(self.args.project)

        result = db.runGremlinQuery(query)
        for x in result:
            if self.args.raw:
                print(repr(x))
            else:
                print(x)
        db.runGremlinQuery("quit")

if __name__=="__main__":
    JoshiApp().run()
    sys.exit()

