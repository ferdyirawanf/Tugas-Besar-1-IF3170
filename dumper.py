from src.ai import *
from src.constant import Path
from src.utility import dump

def dumper(path_b1, path_b2):
    model1 = MinimaxGroup16()
    model2 = LocalSearchGroup16()
    dump(model1, Path.BVB_P1.format(path_b1))
    dump(model2, Path.BVB_P2.format(path_b2))
    dump(model1, Path.PVB.format(path_b1))
    dump(model2, Path.PVB.format(path_b2))

if __name__ == '__main__':
    bot1_filename = 'AiTB_minimax.pkl' 
    bot2_filename = 'AiTB_local_search.pkl'
    dumper(bot1_filename, bot2_filename)