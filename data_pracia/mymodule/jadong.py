import sys
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import variable as v_

assist_count = 0
attack_check = 0
before_money = 0
now_money_ = 0

def assist_(cla, spot):
    try:
        global assist_count
        from potion import maul_potion_get
        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get
        from action import juljun_off, level_up, clean_screen
        import numpy as np
        import cv2

        while v_.r_2_ is False:
            assist_count += 1
            if assist_count < 2:
                clean_screen(cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\complete_mission_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(440, 340, 520, 420, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(480, 700, cla)

                jadong_(cla, spot)

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                v_.r_2_ = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_11.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                v_.r_2_ = True

            if v_.r_2_ != True:

                this_r22 = False

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(870, 200, 920, 250, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    this_r22 = True


                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_22.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(870, 200, 920, 250, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    this_r22 = True

                if this_r22 == True:
                    click_pos_2(735, 230, cla)
                else:
                    click_pos_2(935, 155, cla)
                    time.sleep(0.5)
                    click_pos_2(735, 230, cla)

                time.sleep(0.5)


        juljun_off(cla)

        # 어스름 = aslm_1
        # if spot == "어스름":
        #     point_ = "aslm_1"
        # if spot == "경계지숲":
        #     point_ = "border_forest"
        # if spot == "간헐천지대":
        #     point_ = "ganhulchun"

        maul_potion_get(cla)
        level_up(cla)





    except Exception as e:
        print(e)
        return 0


def jadong_(cla, spot):
    try:
        global attack_check, before_money, now_money_
        import time
        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import menu_open
        import numpy as np
        import cv2
        from massenger import line_to_me

        if spot == "어스름":
            point_ = "aslm_1"
        if spot == "경계지숲":
            point_ = "border_forest"
        if spot == "간헐천지대":
            point_ = "ganhulchun_1"

        jadong_1 = False
        while jadong_1 is False:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:

                    map_in_ = False
                    while map_in_ is False:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_5.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            time.sleep(1)

                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            map_in_ = True
                            time.sleep(1)
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)


                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jadong\\" + str(point_) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y - 33, cla)
                    jadong_1 = True
                    jadong_2 = False
                    while jadong_2 is False:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jadong\\jadong_move_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            click_pos_2(930, 55, cla)
                            time.sleep(120)
                            click_pos_2(930, 765, cla)
                            jadong_2 = True

            else:
                click_pos_2(100, 180, cla)
                time.sleep(2)

        # money_ = text_check_get(233, 48, 300, 65, cla)
        # print("money?", money_)
        # if len(money_) != 0:
        #     end_ = int_put_(money_)
        #     print("now_money?", end_)




        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\grow_f.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 700, 960, 1030, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("자동사냥 시작")
            click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)
        return 0

def now_hunting(cla):
    try:
        global assist_count
        from potion import maul_potion_get
        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, int_put_, click_pos_reg
        from action import juljun, level_up, clean_screen, menu_open
        import numpy as np
        import cv2



        if attack_check == 0:

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\grow_f.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 700, 960, 1030, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("자동사냥 시작")
                click_pos_reg(imgs_.x, imgs_.y, cla)

            attack_check += 1
            now_attck_1 = False
            while now_attck_1 is False:
                menu_open(cla)
                now_attck_1 = True
                now_attck_2 = False
                while now_attck_2 is False:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jadong\\rank_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 425, 710, 500, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        now_attck_2 = True
                        now_attck_3 = False
                        now_rank_ = False
                        while now_attck_3 is False:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jadong\\rank_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 0, 900, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                if now_rank_ == False:
                                    money_ = text_check_get(233, 48, 300, 65, cla)
                                    print("money?", money_)
                                    if len(money_) != 0:
                                        before_money = int_put_(money_)
                                        print("before_money?", before_money)
                                        now_rank_ = True
                                        time.sleep(10)

                                if now_rank_ == True:
                                    money_ = text_check_get(233, 48, 300, 65, cla)
                                    print("money?", money_)
                                    if len(money_) != 0:
                                        now_money_ = int_put_(money_)
                                        print("before_money?", before_money)
                                        print("now_money_?", now_money_)
                                        now_attck_3 = True
                                    if before_money != now_money_:
                                        print("현재 전투 중")
                                    else:
                                        print("현재 노는 중")





    except Exception as e:
        print(e)
        return 0