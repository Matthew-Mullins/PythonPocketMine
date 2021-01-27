from .tile import Tile

import random
'''
Mine for the player to traverse
'''
class Mine:
    MINE_W = 8
    SECTION_W = 8
    SECTION_H = 8

    VALUES = 10
    '''
    Mine for the player to traverse
    '''
    def __init__(self):
        self.mine = [[]]
        self.generate()

    def generate(self):
        '''
        Generates the current mine
        '''
        self.mine = []
        for i in range(0, 4):
            section = []
            for y in range(Mine.SECTION_H):
                row = []
                for x in range(Mine.SECTION_W):
                    row.append(Tile(y + len(self.mine) * Mine.SECTION_H, x, random.randint(0, Mine.VALUES)))
                section.append(row)
            self.mine.append(section)

    def remove_tile(self, _tile):
        for s in range(len(self.mine)):
            for r in range(len(self.mine[s])):
                for c in range(len(self.mine[s][r])):
                    if self.mine[s][r][c] == _tile:
                        self.mine[s][r][c] = None
                        if c == 0:
                            #dont look left
                            if self.mine[s][r][c + 1]:
                                self.mine[s][r][c + 1].visible = True
                        elif c == len(self.mine[s][r]) - 1:
                            #dont look right
                            if self.mine[s][r][c - 1]:
                                self.mine[s][r][c - 1].visible = True
                        else:
                            if self.mine[s][r][c - 1]:
                                self.mine[s][r][c - 1].visible = True
                            if self.mine[s][r][c + 1]:
                                self.mine[s][r][c + 1].visible = True

                        if r == 0:
                            #look previous section
                            if s - 1 > 0:
                                if self.mine[s - 1][len(self.mine[s]) - 1][c]:
                                    self.mine[s - 1][len(self.mine[s]) - 1][c].visible = True
                            if self.mine[s][r + 1][c]:
                                self.mine[s][r + 1][c].visible = True
                        elif r == len(self.mine[s]) - 1:
                            #look next section
                            if s + 1 < len(self.mine):
                                if self.mine[s + 1][0][c]:
                                    self.mine[s + 1][0][c].visible = True
                            if self.mine[s][r - 1][c]:
                                self.mine[s][r - 1][c].visible = True
                        else:
                            if self.mine[s][r + 1][c]:
                                self.mine[s][r + 1][c].visible = True
                            if self.mine[s][r - 1][c]:
                                self.mine[s][r - 1][c].visible = True
                        


                        
        for section in self.mine:
            if len(section) == 0:
                self.mine.remove(section)
            for row in section:
                if len(row) == 0:
                    section.remove(row)
                try:
                    row.remove(_tile)
                except:
                    pass