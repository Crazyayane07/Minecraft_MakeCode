
def build_line(size, block_id, position, direction):
    i = 0
    while i < size:
        blocks.place(block_id, position)
        position = positions.add(position, direction)
        i+=1
    return position

def build_square(size, block_id, position):
    position = build_line(size, block_id, position, pos(1, 0, 0))
    position = build_line(size, block_id, position, pos(0, 0, 1))
    position = build_line(size, block_id, position, pos(-1, 0, 0))
    position = build_line(size, block_id, position, pos(0, 0, -1))

def build_restangle(size_y, size_x, block_id, position):
    position = build_line(size_x, block_id, position, pos(1, 0, 0))
    position = build_line(size_y, block_id, position, pos(0, 0, 1))
    position = build_line(size_x, block_id, position, pos(-1, 0, 0))
    position = build_line(size_y, block_id, position, pos(0, 0, -1))
    return position

def build_tower(size, height, position, direction):
    i = 0
    while i < height:
        build_square(size, YELLOW_WOOL, position)
        position = positions.add(position, direction)
        i+=1
    return position

def on_chat_mcdonald():
    position = builder.position()
    position = build_tower(5, 5, position, pos(0, 1, 0))
    position = build_tower(5, 3, position, pos(1, 1, 0))
    position = build_restangle(5, 10, YELLOW_WOOL, position)
    position = positions.add(position, pos(0, 1, 0))
    position = build_restangle(5, 10, YELLOW_WOOL, position)
    position = positions.add(position, pos(5, -2, 0))
    position = build_tower(5, 2, position, pos(1, -1, 0))
    position = build_tower(5, 6, position, pos(0, -1, 0))
    position = positions.add(position, pos(5, 1, 0))
    position = build_tower(5, 5, position, pos(0, 1, 0))
    position = build_tower(5, 3, position, pos(1, 1, 0))
    position = build_restangle(5, 10, YELLOW_WOOL, position)
    position = positions.add(position, pos(0, 1, 0))
    position = build_restangle(5, 10, YELLOW_WOOL, position)
    position = positions.add(position, pos(5, -2, 0))
    position = build_tower(5, 2, position, pos(1, -1, 0))
    position = build_tower(5, 6, position, pos(0, -1, 0))

def build_piramid(size, block_id, position):
    while size > 0:
        build_square(size, block_id, position)
        position = positions.add(position,  pos(1, 1, 1))
        size = size - 2
    blocks.place(block_id, position)
    
def on_chat_giza():
    position = builder.position()
    build_piramid(50, YELLOW_WOOL, position)

def on_chat_luwr():
    position = builder.position()
    build_piramid(20, GLASS, position)

player.on_chat("mcdonald", on_chat_mcdonald)
player.on_chat("giza", on_chat_giza)
player.on_chat("luwr", on_chat_luwr)