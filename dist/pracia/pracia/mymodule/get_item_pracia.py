import sys

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def get_item_start(cla):
    import time
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from massenger import line_to_me
    from daily_mission import request, go_confirm
    from action import clean_screen, gonghun_
    from jadong import jadong_

    import numpy as np
    import cv2
    try:
        print("get_item_start")

        get_upjuk(cla)

        get_season_pass(cla)

        get_post(cla)

        print("아이템 등 받기 끝!!!")

        clean_screen(cla)

    except Exception as e:
        print(e)
        return 0

def get_upjuk(cla):
    import time
    from function_game import click_pos_2, imgs_set, click_pos_reg
    from action import menu_open

    import numpy as np
    import cv2
    try:

        print("get_upjuk")

        get_ = False
        get_count = 0

        while get_ is False:
            get_count += 1
            if get_count > 7:
                get_ = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_upjuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(700, 30, 860, 80, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("title_upjuk")
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\get_item\\post_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(30, 75, 860, 120, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(780, 1000, cla)
                    else:
                        get_ = True
                        break
                    time.sleep(0.3)
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\menu_open\\menu_upjuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(630, 100, 950, 550, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_upjuk.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 30, 860, 80, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)
            time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0

def get_season_pass(cla):
    import time
    from function_game import click_pos_2, imgs_set, click_pos_reg, imgs_set_
    from action import menu_open

    import numpy as np
    import cv2
    try:

        print("get_season_pass")

        get_ = False
        get_count = 0

        while get_ is False:
            get_count += 1
            if get_count > 7:
                get_ = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_season_pass.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(700, 30, 860, 80, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("title_season_pass")
                click_pos_2(130, 750, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.2)

                get_ = True
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\menu_open\\menu_season_pass.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(630, 100, 950, 550, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_season_pass.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 30, 860, 80, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)
            time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0

def get_post(cla):
    import time
    from function_game import click_pos_2, imgs_set, click_pos_reg
    from action import menu_open

    import numpy as np
    import cv2
    try:

        print("get_post")

        get_ = False
        get_count = 0

        while get_ is False:
            get_count += 1
            if get_count > 7:
                get_ = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(700, 30, 860, 80, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("title_post")



                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\get_item\\post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(30, 75, 860, 120, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("post_point_1", imgs_)
                    click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                    time.sleep(0.3)
                    click_pos_2(890, 1010, cla)
                else:
                    get_ = True

            else:
                menu_open(cla)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\menu_open\\menu_post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(630, 930, 850, 1020, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 30, 860, 80, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0