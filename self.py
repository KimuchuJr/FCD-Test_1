  self.table = [
      ["-", "-", "-"],  
      ["-", "-", "-"],
      ["-", "-", "-"]
  ]
    def _move(self, pos):
      x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
      if self.table[x][y] == "-":
          self.table[x][y] = self.player
  def _check_win():
      for row in self.table:
          if row.count(self.player) == len(row):
              return True

      # Check columns                 
      ...

      # Check diagonals
      ...
  def _message():
      if self.winner:
          msg = f'{self.winner} wins!' 
      elif self.draw:
          msg = 'It is a draw!'
      else:
          msg = f'{self.player}\'s turn'
