from draw import Draw
from listview import LisNav
from snake import Snake
from dinoGame import Dino

items=['Snake','Dino']
games=[Snake,Dino]
LisNav.setGames(games)
LisNav.navigate(items)