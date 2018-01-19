# -*- encoding:utf-8 -*-
"""
    author:lgh
"""

from PIL import Image
import numpy as np

def crop_img():
    for i in range(1, 20):
        image = Image.open('level_%s.png' % i)
        new = image.crop((360, 5, 360 + 35 * 16, 5 + 35 * 16))
        new.save('level%s.png' % i)

def main():
    for k in range(1, 20):
        image = Image.open('level%s.jpg' %k)
        tree_positions = list()
        target_positions = list()
        suitcase_positions = list()
        human_positions = list()
        tree_avg = [8, 29, 3]
        target_avg = [45, 35, 1]
        suitcase_avg = [34, 27, 14]
        human_avg = [39, 11, 7]
        ranges = 3
        for i in range(16):
            for j in range(16):
                new = image.crop((i*35+10,j*35+10, (i+1)*35-10, (j+1)*35-10))
                im_datas = new.getdata()
                r,g,b = 0, 0, 0
                for data in im_datas:
                    r += data[0]
                    g += data[1]
                    b += data[2]
                avg_r = r // (35 * 35)
                avg_g = g // (35 * 35)
                avg_b = b // (35 * 35)
                if avg_r < tree_avg[0]+ranges and avg_r > tree_avg[0]-ranges and avg_g < tree_avg[1]+ranges and avg_g > tree_avg[1]-ranges and avg_b < tree_avg[2]+ranges and avg_b > tree_avg[2]-ranges:
                    tree_positions.append([i+1, j+1])
                if avg_r < target_avg[0]+ranges and avg_r > target_avg[0]-ranges and avg_g < target_avg[1]+ranges and avg_g > target_avg[1]-ranges and avg_b < target_avg[2]+ranges and avg_b > target_avg[2]-ranges:
                    target_positions.append([i+1, j+1])
                if avg_r < suitcase_avg[0]+ranges and avg_r > suitcase_avg[0]-ranges and avg_g < suitcase_avg[1]+ranges and avg_g > suitcase_avg[1]-ranges and avg_b < suitcase_avg[2]+ranges and avg_b > suitcase_avg[2]-ranges:
                    suitcase_positions.append([i+1, j+1])
                if avg_r < human_avg[0]+ranges and avg_r > human_avg[0]-ranges and avg_g < human_avg[1]+ranges and avg_g > human_avg[1]-ranges and avg_b < human_avg[2]+ranges and avg_b > human_avg[2]-ranges:
                    human_positions.extend([i+1, j+1])
        if len(suitcase_positions) != len(target_positions):
            if len(suitcase_positions) < len(target_positions):
                suitcase_positions.append([human_positions[0], human_positions[1]-1])
            else:
                target_positions.append([human_positions[0], human_positions[1]-1])
        else:
            tree_positions.append([human_positions[0], human_positions[1]-1])
        with open('locations.py', 'a') as f:
            f.write('level_%s_tree_location = %s' %(k, tree_positions))
            f.write('\n')
            f.write('level_%s_target_location = %s' %(k, target_positions))
            f.write('\n')
            f.write('level_%s_suitcase_location = %s' % (k, suitcase_positions))
            f.write('\n')
            f.write('level_%s_human_location = %s' % (k, human_positions))
            f.write('\n')








if __name__ == '__main__':
    main()

