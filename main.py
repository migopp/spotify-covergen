from PIL import Image, ImageDraw
import sys
import random

SIZE = 640
BLOCK_SIZE = 80
blocks_per_row = int(SIZE / BLOCK_SIZE)
num_blocks = blocks_per_row ** 2

def unique_cover_gen(seed):
    # make base
    cover = Image.new('RGB', (SIZE, SIZE))

    # init rng
    random.seed(seed)

    # generate colors
    colors = [(255, 255, 255)] * num_blocks
    for i in range(num_blocks):
        color_1 = random.randint(0, 255)
        color_2 = random.randint(0, 255)
        color_3 = random.randint(0, 255)
        colors[i] = (color_1, color_2, color_3)

    # fill base
    cover_draw = ImageDraw.Draw(cover)
    for x in range(blocks_per_row):
        for y in range(blocks_per_row):
            x_0, y_0 = x * BLOCK_SIZE, y * BLOCK_SIZE
            x_1, y_1 = x_0 + BLOCK_SIZE - 1, y_0 + BLOCK_SIZE - 1
            block_num = x * blocks_per_row + y
            cover_draw.rectangle((x_0, y_0, x_1, y_1), fill=colors[block_num])

    # save
    cover.save(f'out/{str(seed)}.jpg')

    return

if __name__ == '__main__':
    # deal with cli args
    args_len = len(sys.argv)
    seed =  sys.argv[1] if args_len > 1 else None

    # generate
    unique_cover_gen(seed)
