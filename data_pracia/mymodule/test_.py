import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, imgs_set, click_pos_reg, click_pos_2, text_check_get, int_put_
    from jungi_pracia import go_jungi
    from action import menu_open, clean_screen, juljun_off, juljun_on, dead_die, juljun_attack_check
    from get_item_pracia import get_item_start
    from potion import potion_check, potion_quickslot, maul_potion_get


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3

    print("result_attack result_attack result_attack result_attack result_attack")
    result_attack = juljun_attack_check(cla)
    print("result_attack", result_attack)


    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\out_jabhwa.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(0, 30, 960, 1040, cla, img)
    if imgs_ is not None and imgs_ != False:
        print("out_jabhwa", imgs_)

    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_2.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
    if imgs_ is not None and imgs_ != False:
        print("move_2", imgs_)

    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_x.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
    if imgs_ is not None and imgs_ != False:
        print("move_x", imgs_)

    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\r_.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("r_", imgs_)
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\r_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("r_2", imgs_)
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\r_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("r_3", imgs_)
    #
    # # menu_open(cla)
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\get_item\\post_point_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set(30, 75, 860, 120, cla, img)
    # if imgs_ is not None and imgs_ != False:
    #     print("post_point_1", imgs_)
    #
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\exit_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
    # if imgs_ is not None and imgs_ != False:
    #     print("exit_1", imgs_)
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\exit_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
    # if imgs_ is not None and imgs_ != False:
    #     print("exit_2", imgs_)
    #
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\exit_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
    # if imgs_ is not None and imgs_ != False:
    #     print("exit_3", imgs_)
    #
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\up2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
    # if imgs_ is not None and imgs_ != False:
    #     print("up2", imgs_)
    #
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\level_up.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
    # if imgs_ is not None and imgs_ != False:
    #     print("level_up", imgs_)
    #
    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\juljun_die_1.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(400, 100, 800, 160, cla, img, 0.83)
    if imgs_ is not None and imgs_ != False:
        print("절전 사망", imgs_)

    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_confirm_1.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(0, 650, 960, 1030, cla, img, 0.83)
    if imgs_ is not None and imgs_ != False:
        print("die_confirm_1", imgs_)
    else:
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_confirm_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 650, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("die_confirm_2", imgs_)
            # menu_open 후에 복구 버튼 누르기

    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_5.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(600, 100, 960, 300, cla, img, 0.83)
    if imgs_ is not None and imgs_ != False:
        print("die_5", imgs_)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 850, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("die_6", imgs_)

    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_1.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(0, 0, 960, 300, cla, img, 0.83)
    if imgs_ is not None and imgs_ != False:
        print("die_1", imgs_)

    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\juljun_potion_zero.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(660, 960, 950, 1020, cla, img, 0.83)
    if imgs_ is not None and imgs_ != False:
        print("juljun_potion_zero", imgs_)
    #
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skip_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
    # if imgs_ is not None and imgs_ != False:
    #     print("skip_2 보인다 ^ㅅ^", imgs_)
    #
    # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.75)
    # if imgs_ is not None and imgs_ != False:
    #         print("r_2_1 보인다 ^ㅅ^", imgs_)