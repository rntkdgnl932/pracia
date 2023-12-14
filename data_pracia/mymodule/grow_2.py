import sys
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

camera_ = False
media_ = False
talchool_ = False
prison_ = False
boonji_ = False
force_quest = 0
first_select_ = False

# 미션 요구 레벨
re_le_count = 0
get_level = 0

def jungi_grow(cla, jungi_number):
    try:
        global camera_, media_, talchool_, prison_, boonji_, force_quest, first_select_, get_level

        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from massenger import line_to_me
        from potion import maul_potion_get
        from action import juljun_off, dead_die, clean_screen, menu_open, go_confirm_yes

        from schedule import myQuest_play_add

        import pyautogui
        import random
        import numpy as np
        import cv2
        import os.path
        import pyautogui

        print("pracia tuto", cla)

        dir_path = "C:\\my_games\\pracia\\data_pracia"
        file_path = dir_path + "\\my_episode\\my_episode.txt"

        my_episode_read = False
        while my_episode_read is False:
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='UTF8') as file:
                    my_episode_read = True
                    my_episode = file.read()
                    if my_episode == jungi_number:
                        first_select_ = True
                    else:
                        with open(file_path, "w", encoding='UTF8') as file:
                            file.write(str(jungi_number))
                            first_select_ = False
                    print("my_episode", my_episode)
            else:
                with open(file_path, "w", encoding='UTF8') as file:
                    file.write(str(1))

        juljun_off(cla)
        dead_die(cla)

        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\quihwan_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(300, 450, 660, 560, cla, img)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(540, 590, cla)
            time.sleep(5)

        get_level_result = get_my_level_(cla)
        if get_level_result != 0:
            get_level = get_level_result
            print("get_level => ", get_level)

        maul_potion_get(cla)



        # if cla == 'one':
        #     coordinate = 0
        # if cla == 'two':
        #     coordinate = 960
        # result_int = random.randint(0, 9)
        # # 350, 415, 480, 545, 610 // 625
        # ran_ = 100 + (int(result_int) * 80)
        # pyautogui.moveTo(ran_ + coordinate + random_int(), ran_ + random_int(), 0.5)








        # 처음 전기 에피소드 선택 관련
        if first_select_ == False:
            print("전기 에피소드 시작")

            #퀘스트창 열어서 기존꺼 포기하기

            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_media.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    talking_ = False
                    talking_count = 0
                    while talking_ is False:
                        talking_count += 1
                        if talking_count > 7:
                            talking_ = True
                        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_media.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            talking_ = True
                        time.sleep(0.5)
            else:


                jungi_start_1 = False
                while jungi_start_1 is False:

                    full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("jungi_", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        jungi_start_1 = True

                        jungi_start_2 = False
                        jungi_start_2_count = 0
                        while jungi_start_2 is False:
                            jungi_start_2_count += 1
                            if jungi_start_2_count > 7:
                                jungi_start_2 = True

                            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_back.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                print("jungi_back", imgs_)
                            else:
                                # 1번 전기
                                if int(my_episode) == 1:
                                    print("1")
                                    click_pos_2(100, 700, cla)
                                # 2번 전기
                                if int(my_episode) == 2:
                                    print("2")
                                    click_pos_2(310, 650, cla)
                                # 3번 전기
                                if int(my_episode) == 3:
                                    print("3")
                                    click_pos_2(700, 650, cla)
                                # 4번 전기
                                if int(my_episode) == 4:
                                    print("4")
                                    click_pos_2(880, 700, cla)

                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    print("jungi_3..", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    pyautogui.moveTo(470 + random_int(), 200 + random_int(), 0.1)

                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_4.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    jungi_start_2 = True
                                    full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_back.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        pyautogui.moveTo(470 + random_int(), 200 + random_int(), 0.1)

                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\give_up_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    print("give_up_1..", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    pyautogui.moveTo(470 + random_int(), 200 + random_int(), 0.1)
                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\give_up_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    print("give_up_2..", imgs_)
                                    go_confirm_yes(cla)
                                    jungi_start_2 = True




                    else:
                        print("여기냐!!!!!!!")
                        click_pos_2(930, 55, cla)
                        time.sleep(1)
                    time.sleep(0.5)
        else:
            # 전기 관련
            print("전기관련")
            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("전기관련2")

                jungi_start_3 = False
                jungi_start_3_count = 0
                while jungi_start_3 is False:
                    jungi_start_3_count += 1
                    if jungi_start_3_count > 7:
                        jungi_start_3 = True

                    full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_back.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                    else:

                        # 1번 전기
                        if int(jungi_number) == 1:
                            print("11")
                            click_pos_2(100, 700, cla)
                        # 2번 전기
                        if int(jungi_number) == 2:
                            print("22")
                            click_pos_2(310, 650, cla)
                        # 3번 전기
                        if int(jungi_number) == 3:
                            print("33")
                            click_pos_2(700, 650, cla)
                        # 4번 전기
                        if int(jungi_number) == 4:
                            print("44")
                            click_pos_2(880, 700, cla)

                        jungi_start_3 = True
                        # 전기 공통 처리

                        going_jungi = False
                        jungi_start_4 = False
                        while jungi_start_4 is False:
                            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_3.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                print("jungi_3", imgs_)
                                jungi_start_4 = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                pyautogui.moveTo(470 + random_int(), 200 + random_int(), 0.1)
                            else:
                                print("jungi_3 처리중")
                        jungi_start_5 = False
                        while jungi_start_5 is False:
                            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:

                                jungi_start_5 = True

                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\require_lv.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 100, 960, 500, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("imgs_", imgs_)

                                    level_ = text_check_get(903, imgs_.y - 10, 930, imgs_.y + 10, cla)
                                    # started_ = start_.split("\n")
                                    print("level?", level_)
                                    if len(level_) != 0:
                                        level = int_put_(level_)
                                        level_bloon = level.isdigit()
                                        if level_bloon == True:
                                            level = int(level)
                                            print("require level?", level)

                                            if get_level >= level:
                                                print("진행")
                                                going_jungi = True
                                            else:
                                                print("넘어가기")
                                                jungi_ = "전기육성_" + str(jungi_number)
                                                print("jungi_", jungi_)
                                                myQuest_play_add(cla, jungi_)

                                        else:
                                            print("level => 숫자 아님")
                                            line_to_me(cla, "뿌락시아 숫자 못 읽는 오류")
                                else:
                                    print("에러발생")
                                    line_to_me(cla, "에러 발생 삐뽀삐뽀")

                        jungi_start_6 = False
                        while jungi_start_6 is False:
                            if going_jungi == True:
                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_4.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    print("jungi_4", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    pyautogui.moveTo(470 + random_int(), 200 + random_int(), 0.1)
                                    time.sleep(1)

                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\worldmap_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:

                                    jungi_start_6 = True

                                    full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jadong_move_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_move_1", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(2)

                                        go_confirm_yes(cla)

                                        time.sleep(1)

                                        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\worldmap_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(930, 55, cla)
                                            time.sleep(1)
                                            click_pos_2(930, 55, cla)
                                            clean_screen(cla)
                            else:
                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\jungi_back.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    jungi_start_6 = True
                                    time.sleep(1)
                    time.sleep(0.5)
            else:
                mission_click_1 = False
                while mission_click_1 is False:

                    full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\quest_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:

                        mission_click_1 = True

                        print("요구레벨 파악 후 진행여부")
                        result_re_le = require_level(cla)
                        if result_re_le == True:
                            jungi_ = "전기육성_" + str(jungi_number)
                            print("jungi_", jungi_)
                            myQuest_play_add(cla, jungi_)
                        else:

                            # click_pos_2(730, 165, cla)
                            # 여기부터 의뢰소 가는 길 다시 수정
                            time.sleep(2)
                            # full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\mission_station_1.PNG"
                            # img_array = np.fromfile(full_path, np.uint8)
                            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            # imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                            # if imgs_ is not None and imgs_ != False:
                            #     mission_have = False
                            # full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\mission_station_11.PNG"
                            # img_array = np.fromfile(full_path, np.uint8)
                            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            # imgs_ = imgs_set_(500, 500, 960, 1030, cla, img, 0.83)
                            # if imgs_ is not None and imgs_ != False:
                            #     mission_have = False

                            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\mission_start_11.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\mission_start_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("퀘스트 진행")
                            else:

                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\mission_start_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("dmdkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                else:
                                    full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\mission_start_1_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(690, 900, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        print("dmdkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk2")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)


                    else:
                        clean_screen(cla)

                        menu_open(cla)

                        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\common\\menu_quest_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            print("imgs_1", imgs_)
                        time.sleep(0.2)
                        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\common\\menu_quest_11.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            print("imgs_2", imgs_)

                        print("퀘스트창 로딩중1")
                        time.sleep(0.3)




        # 대화 관련


        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_1\\talk_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(500, 600, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talk_", imgs_)
            click_pos_reg(imgs_.x + 80, imgs_.y, cla)



        # 물약 구매 관련
        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\potion_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:

            camera_ = False

            print("potion_6", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            potion__ = text_check_get(355, 520, 607, 555, cla)
            potion__result = potion__.split("\n")
            potion__result = " ".join(potion__result).strip()
            print("potion__result", potion__result)
            ispotion = False
            if len(potion__result) != 0:
                for list in range(len(potion__result)):
                    try:
                        if potion__result[list] == "가" or potion__result[list] == '방' or potion__result[list] == '이' or \
                                potion__result[list] == '무':
                            ispotion = True
                    except:
                        pass
            if ispotion == True:
                line_to_me(cla, "가방이 개 무거워 ㅠㅠ 프라시아")
                stop = True
                while stop is True:
                    print("멈추자...")
                    time.sleep(10000)
            time.sleep(1)
            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\potion_7.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                potion_ = True
                print("potion_7", imgs_)
                click_pos_2(530, 590, cla)
                click_pos_2(530, 590, cla)
                click_pos_2(530, 590, cla)
                click_pos_2(530, 590, cla)
                click_pos_2(530, 590, cla)
                time.sleep(0.5)
                click_pos_2(480, 590, cla)
                time.sleep(0.5)
                click_pos_2(530, 630, cla)
                time.sleep(1)

                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\potion_8.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("potion_6", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    potion__ = text_check_get(355, 520, 607, 555, cla)
                    potion__result = potion__.split("\n")
                    potion__result = " ".join(potion__result).strip()
                    print("potion__result", potion__result)
                    ispotion = False
                    if len(potion__result) != 0:
                        for list in range(len(potion__result)):
                            try:
                                if potion__result[list] == "가" or potion__result[list] == '방' or potion__result[
                                    list] == '이' or potion__result[list] == '무':
                                    ispotion = True
                            except:
                                pass
                    if ispotion == True:
                        line_to_me(cla, "가방이 개 무거워 ㅠㅠ 프라시아")
                        stop = True
                        while stop is True:
                            print("멈추자...")
                            time.sleep(10000)
                    time.sleep(1)
                    full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\potion_9.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        potion_ = True
                        print("potion_7", imgs_)
                        click_pos_2(430, 590, cla)
                        time.sleep(0.5)
                        click_pos_2(530, 630, cla)
                        time.sleep(1)

                        click_pos_2(840, 1005, cla)
                        time.sleep(1)
                        click_pos_2(540, 590, cla)
                        time.sleep(1)
                        click_pos_2(930, 55, cla)









        ####################################




        full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\gongan_june_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 350, 500, 500, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\grow\\grow_2\\gongan_june_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 650, 550, 700, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                click_pos_2(540, 675, cla)




    except Exception as e:
        print(e)


def require_level(cla):
    try:
        global re_le_count
        from function_game import text_check_get, int_put_, imgs_set, click_pos_reg, click_pos_2, imgs_set_
        from massenger import line_to_me
        from action import go_confirm_yes

        import cv2
        import numpy as np

        re_le_ = False

        level_ = text_check_get(61, 45, 80, 65, cla)
        # started_ = start_.split("\n")
        print("level?", level_)
        if len(level_) != 0:
            level = int_put_(level_)
            level_bloon = level.isdigit()
            if level_bloon == True:
                level = int(level)
                print("level?", level)
            else:
                print("level => 숫자 아님")

            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\mission_level_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(690, 230, 785, 260, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("mission_level_1", imgs_)

                x_ = imgs_.x + 150
                y_ = imgs_.y - 15

                require_level_ = text_check_get(x_, y_, 945, y_ + 20, cla)
                # started_ = start_.split("\n")
                print("require_level_?", require_level_)
                if len(require_level_) != 0:
                    require_level = int_put_(require_level_)
                    require_level_bloon = require_level.isdigit()
                    if require_level_bloon == True:
                        require_level = int(require_level)
                        if 1000 > int(require_level) > 700:
                            require_level = require_level - 700
                            print("require_level?????", require_level)
                        elif int(require_level) > 1700:
                            require_level = require_level - 1700
                            print("require_level?????", require_level)
                        else:
                            print("require_level?", require_level)
                    else:
                        print("require_level => 숫자 아님")

                    if int(require_level) > int(level):
                        re_le_count += 1
                        if re_le_count > 3:
                            re_le_ = True
                            print("요구 레벨이 높다. 다음 스케쥴 진행하자")
                            full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\give_up_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(690, 980, 820, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                print("give_up_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                con_ = False
                                con_count = 0
                                while con_ is False:
                                    con_count += 1
                                    go_result = go_confirm_yes(cla)
                                    time.sleep(0.5)
                                    if go_result == True:
                                        go_confirm_yes(cla)
                                        con_ = go_result



                                    if con_count > 5:
                                        ms_ = "grow_2, 전기육성에서 스케쥴 포기 부분 : '확인'을 못찾아서 생긴 에러"
                                        print(ms_)
                                        line_to_me(cla, ms_)
                            else:
                                full_path = "c:\\my_games\\pracia\\\data_pracia\imgs\\daily_mission\\quest_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 100, 800, 1030, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(760, 1010, cla)
                                else:
                                    ms_ = "퀘스트창 아니다. 에러일듯"
                                    print(ms_)
                                    line_to_me(cla, ms_)

                    else:
                        re_le_count = 0
                        print("요구 레벨이 내 레벨대비 적정하니 스케쥴 그대로 진행하자")
        return re_le_
    except Exception as e:
        print(e)
        return 0



def get_my_level_(cla):
    try:
        from function_game import text_check_get

        level = 0

        level_ = text_check_get(61, 45, 80, 65, cla)
        # started_ = start_.split("\n")
        print("level?", level_)
        if len(level_) != 0:
            level = int_put_(level_)
            level_bloon = level.isdigit()
            if level_bloon == True:
                level = int(level)
                print("level?", level)
            else:
                print("level => 숫자 아님")
        if level != 0:
            return level
    except ValueError:
        return False

def int_put_(data):
    try:
        import re
        data_ = data.replace(',', '').strip()
        data_2 = data_.replace('.', '').strip()
        data_3 = data_2.replace(' ', '').strip()
        data_4 = data_3.replace('/', '').strip()

        # data_2 = data_.strip().replace('.', '')
        # data_3 = data_2.strip().replace(' ', '')
        # data_4 = data_3.strip().replace('/', '')
        result = re.sub(r'[^0-9]', '', data_4)
        return result
    except ValueError:
        return False