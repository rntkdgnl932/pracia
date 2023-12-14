import sys
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


# 미션 진행
mission_have = False
mission_boss = False
# 요구레벨 카운트
re_le_count = 0

def request(cla):
    try:
        global mission_have, mission_boss
        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import menu_open, clean_screen, juljun_off, level_up, dead_die
        from massenger import line_to_me
        from potion import maul_potion_get
        from schedule import myQuest_play_add
        import numpy as np
        import cv2
        import random


        juljun_off(cla)
        time.sleep(0.5)

        if mission_have == False:

            # clean_screen(cla)
            juljun_off(cla)
            dead_die(cla)
            maul_potion_get(cla)



            mission_click_1 = False
            while mission_click_1 is False:

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:

                    mission_click_1 = True

                    click_pos_2(730, 165, cla)
                    # 여기부터 의뢰소 가는 길 다시 수정
                    time.sleep(2)
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        mission_have = False
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_11.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        mission_have = False
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        mission_have = True
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_11.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        mission_have = True
                else:
                    clean_screen(cla)

                    menu_open(cla)

                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        print("imgs_1", imgs_)
                    time.sleep(0.2)
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_11.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        print("imgs_2", imgs_)

                    print("퀘스트창 로딩중1")
                    time.sleep(0.3)

            if mission_have == False:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 120, cla)
            else:
                print("외뢰 있을 경우 실행")

        if mission_have == False:

            mission_ready_1 = False
            while mission_ready_1 is False:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\maul_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        mission_ready_1 = True
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            mission_ready_1 = True
                            map_in_ = False
                            while map_in_ is False:
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_5.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_6.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                    time.sleep(1)

                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_4.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        map_in_ = True
                                    time.sleep(1)
                                else:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_4.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                else:
                    print("세계지도 열자")
                    clean_screen(cla)
                    result_menu = menu_open(cla)
                    if result_menu == True:
                        click_pos_2(800, 400, cla)
                    time.sleep(0.5)


            mission_ready_2 = False
            while mission_ready_2 is False:

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 210, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(930, 245, cla)
                    mission_ready_2 = True

                    mission_ready_3 = False
                    while mission_ready_3 is False:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 960, 1030, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(680, 720, cla)
                            mission_ready_3 = True
                        time.sleep(1)

                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\maul_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_6.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 0, 960, 100, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            mission_ready_2 = True
                        else:
                            print("마을 표시 못 찾음")
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 55, cla)
                                time.sleep(1)
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                            if imgs_ is None:
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_9.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 130, 200, 330, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.1)
                                    click_pos_2(20, 120, cla)
                                else:
                                    click_pos_2(20, 120, cla)
                                    time.sleep(1)
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_9.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(0, 130, 200, 330, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_2(20, 120, cla)
                            time.sleep(1)









                time.sleep(1)



            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\daily_mission\\confirm_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            time.sleep(1)

            mission_ready_4 = False
            while mission_ready_4 is False:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\worldmap_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 55, cla)
                    mission_ready_4 = True
                else:
                    mission_ready_4 = True
                time.sleep(1)

            mission_ready_5 = False
            print("mission_ready_5")
            while mission_ready_5 is False:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_6.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(700, 0, 960, 100, cla, img)
                if imgs_ is not None and imgs_ != False:
                    mission_ready_5 = True
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                time.sleep(2)

            mission_ready_6 = False
            print("mission_ready_6")
            while mission_ready_6 is False:
                mission_get_ = False

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_get_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 870, 800, 920, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("mission_get_1", imgs_)
                    mission_get_ = True

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_get_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 870, 960, 920, cla, img, 0.9)
                if imgs_ is None:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_get_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(840, 870, 960, 920, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:

                        mission_get_ = True

                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_get_4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 870, 800, 920, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            mission_boss = True




                if mission_boss == True:
                    if mission_boss == True:
                        print("Boss ready")
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_boss.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(290, 105, cla)
                        mission_ready_6 = True

                        myQuest_play_add(cla, "의뢰퀘스트")

                        click_pos_2(930, 55, cla)
                else:
                    if mission_get_ == False:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_6.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 0, 960, 100, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_7.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(700, 0, 960, 100, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(850, 970, cla)

                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_broke_8.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(700, 0, 960, 100, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(480, 380, 240, 380, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(400, 500, 600, 700, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:

                        mission_ready_6 = True
                        click_pos_2(930, 55, cla)

                        # menu_open(cla)

                        mission_click_1 = False
                        while mission_click_1 is False:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                mission_click_1 = True
                                click_pos_2(730, 165, cla)
                                time.sleep(2)

                                mission_click_2 = False
                                while mission_click_2 is False:

                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_11.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        mission_click_2 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        mission_click_2 = True
                                        mission_have = False
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_11.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        mission_click_2 = True
                                        mission_have = False
                            else:
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                result_menu = menu_open(cla)
                                if result_menu == True:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                print("퀘스트창 로딩중2")



        else:
            print("미션 수행")

            dead_die(cla)
            juljun_off(cla)

            if mission_boss == False:

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\daily_mission\\confirm_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\daily_mission\\r_2_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 720, 960, 1030, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    result_ran = random.randint(2, 4)
                    time.sleep(1)
                    for i in range(result_ran):
                        click_pos_2(935, 105, cla)
                        time.sleep(0.3)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("의뢰퀘스트 수행중")
                    mission_ing = False
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 950, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        mission_ing = True

                    if mission_ing == False:
                        mission_click_1 = False
                        while mission_click_1 is False:

                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                mission_click_1 = True
                                click_pos_2(730, 165, cla)
                                time.sleep(2)

                                mission_click_2 = False
                                while mission_click_2 is False:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:

                                        click_pos_2(730, 165, cla)
                                        time.sleep(2)

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_11.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            mission_click_2 = True
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            mission_click_2 = True
                                            mission_have = False

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_11.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            mission_click_2 = True
                                            mission_have = False
                                    else:
                                        clean_screen(cla)
                                        print("미션 수행중 쿼스트창 열기")
                                        result_menu = menu_open(cla)
                                        if result_menu == True:
                                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                    print("^_^")
                            else:
                                print("퀘스트창 로딩중3...")
                                clean_screen(cla)
                                print("미션 수행중 쿼스트창 열기")
                                result_menu = menu_open(cla)
                                if result_menu == True:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        print("good")


                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("의뢰수행중 바깥화면")

                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_go_11.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 0, 960, 500, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_go_11", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_go_111.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 0, 960, 500, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_go_111", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_go_1111.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 0, 960, 500, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_go_1111", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_go_11111.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 0, 960, 500, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_go_11111", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        print("미션창 진입")
                        mission_click_1 = False
                        while mission_click_1 is False:

                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\quest_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                mission_click_1 = True
                                click_pos_2(730, 165, cla)
                                time.sleep(2)

                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(700, 950, 960, 1030, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("미션 수행중 이상무")

                                else:

                                    mission_click_2 = False
                                    while mission_click_2 is False:

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_11.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_start_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            mission_click_2 = True
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            mission_click_2 = True
                                            mission_have = False
                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\mission_station_11.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            mission_click_2 = True
                                            mission_have = False


                            else:
                                go_confirm(cla)
                                time.sleep(0.3)

                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\complete_mission_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 340, 520, 420, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(480, 700, cla)

                                clean_screen(cla)

                                clean_screen(cla)
                                print("미션 수행중 쿼스트창 열기")
                                menu_open(cla)
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                print("퀘스트창 로딩중4")
                                time.sleep(0.3)
                                go_confirm(cla)
                                time.sleep(0.3)
                                juljun_off(cla)
                    else:
                        print("다른 화면일 가능성이 크다")
                        clean_screen(cla)




            maul_potion_get(cla)
            level_up(cla)

            # 의뢰 보스 있을 경우 애래에 코딩
            if mission_boss == True:
                print("보스 잡으러 가장")
                myQuest_play_add(cla, "의뢰퀘스트")
                line_to_me(cla, "일반의뢰 끝")


    except Exception as e:
        print(e)
        return 0

def go_confirm(cla):
    try:
        import cv2
        import numpy as np
        from function_game import imgs_set_, click_pos_reg

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\confirm_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)
        return 0

