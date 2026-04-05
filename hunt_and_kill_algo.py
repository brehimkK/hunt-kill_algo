def get_visited_neighbors(self, block: Block) -> list[Block]:
        """
        Finds adjacent blocks that are already part of the maze.
        """
        visited_neighbors = []
        x, y = block.x, block.y

        # Potential neighbor coordinates
        potential_coords = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

        for nx, ny in potential_coords:
            # 1. Check that nx , and ny insid the grid
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor = self.grid[ny][nx]

                # 2. Check if the neighbor is visited AND not part of the '42' pattern
                if neighbor.checked and not neighbor.is_pattern:
                    visited_neighbors.append(neighbor)

        return visited_neighbors
    
    def maze_generation_hunt_and_kill(self) -> None:
        random.seed(self.seed)

        start_x, start_y = self.entry
        current_block = self.grid[start_y][start_x]
        current_block.checked = True

        while current_block is not None: # walk
            unvisited = self.get_unvisited_neighbors(current_block)  # get neighbors
            
            if unvisited:  # if there's a neighbors
                neighbor = random.choice(unvisited)  # chose one neighbor randomly
                self.remove_wall_between(current_block, neighbor)
                neighbor.checked = True
                current_block = neighbor  # move to the visited neighbor

            else:  # if get stock (no unvisited_neighbors)
                current_block = None
                # walk throgh the grid 
                for y in range(self.height):
                   
                    for x in range(self.width):
                        potential_block = self.grid[y][x]
                        
                        if not potential_block.checked and not potential_block.is_pattern:
                            visited_neighbors = self.get_visited_neighbors(potential_block)

                            if visited_neighbors:
                                neighbor = random.choice(visited_neighbors)
                                self.remove_wall_between(potential_block, neighbor)

                                potential_block.checked = True
                                current_block = potential_block
                                # Break nested loops to restart WALK phase
                                break
                    if current_block:
                        break
