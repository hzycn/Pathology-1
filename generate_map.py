from api import config_fun
from api import prob_map
import numpy as np
import train_helper
import os
from PIL import Image

cfg = config_fun.config()
model = train_helper.get_model(cfg, load_param_from_folder=True)

f = open(cfg.test_file, 'r')
for s in f.readlines():
    file_name, label = s.split()
    raw_img, p_map, b_map = prob_map.generate_prob_map(cfg, model, file_name)

    save_dir_pre = os.path.join(cfg.gm_foder,
                                os.path.basename(file_name).split('.')[0])
    raw_img_dir = save_dir_pre + '_raw_img' + cfg.img_ext
    b_map_img_dir = save_dir_pre + '_b_map_img' + cfg.img_ext
    p_map_img_dir = save_dir_pre + '_p_map_img' + cfg.img_ext

    b_map_npy_dir = save_dir_pre + '_b_map_img'
    p_map_npy_dir = save_dir_pre + '_p_map_img'

    raw_img.save(raw_img_dir)
    # Image.fromarray(p_map).save(p_map_img_dir)
    Image.fromarray(b_map).save(b_map_img_dir)

    np.savetxt(b_map_npy_dir, b_map)
    np.savetxt(p_map_npy_dir, p_map)

