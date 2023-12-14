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

camera_count = 0


def tuto_start(cla):
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from massenger import line_to_me
    from schedule import myQuest_play_add
    from action import juljun_off, menu_close, clean_screen

    import pyautogui
    import random
    import numpy as np
    import cv2
    try:
        # 절전해제
        juljun_off(cla)
        # scan일 경우 해제
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\scan\\scan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(740, 200, 790, 250, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(935, 110, cla)
            time.sleep(0.5)
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

        # level_up 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\level_up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("level_up", imgs_)

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\new_skill_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("new_skill_1", imgs_)
                click_pos_2(480, 750, cla)
                time.sleep(1.5)
                click_pos_2(480, 750, cla)
                time.sleep(1)
                click_pos_2(930, 55, cla)
                time.sleep(1)
                click_pos_2(745, 140, cla)
                time.sleep(1)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("skill_get", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                pyautogui.moveTo(930 + random_int(), 55 + random_int(), 0.5)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_11.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_skill_11", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("skill_get", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    drag_pos(140, 910, 140, 270, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_get.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("skill_get", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_11.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            print("jadong_skill_11", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(2)
                click_pos_2(930, 55, cla)

            else:
                level_up_ = False
                level_up_count = 0
                while level_up_ is False:
                    level_up_count += 1
                    if level_up_count > 5:
                        level_up_ = True
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\level_up.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(473, 723, cla)
                    else:
                        level_up_ = True
                    time.sleep(0.2)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\complete\\complete.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(880, 80, 920, 200, cla, img)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
        tuto_grow(cla)
    except Exception as e:
        print(e)


def tuto_grow(cla):
    global camera_, media_, talchool_, prison_, boonji_, force_quest, camera_count

    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from massenger import line_to_me
    from schedule import myQuest_play_add
    from action import juljun_off, menu_close, clean_screen

    import pyautogui
    import random
    import numpy as np
    import cv2

    try:
        print("pracia tuto", cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\story_setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 200, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(600, 500, cla)
            time.sleep(0.3)
            click_pos_2(480, 720, cla)
            time.sleep(0.2)


        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\x_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 200, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            x_2 = False
            x_2_count = 0
            while x_2 is False:
                x_2_count += 1
                if x_2_count > 5:
                    x_2 = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\x_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 200, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("x_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    x_2 = True
                time.sleep(0.5)

        # if cla == 'one':
        #     coordinate = 0
        # if cla == 'two':
        #     coordinate = 960
        # result_int = random.randint(0, 9)
        # # 350, 415, 480, 545, 610 // 625
        # ran_ = 100 + (int(result_int) * 80)
        # pyautogui.moveTo(ran_ + coordinate + random_int(), ran_ + random_int(), 0.5)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\hwil_mouse_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("hwil_mouse_1", imgs_)
            pyautogui.scroll(-500)
            time.sleep(1)
            pyautogui.scroll(500)
            time.sleep(1)
            click_pos_2(555, 777, cla)
            # hwil_mouse_1 : 여기에 마우스 휠 위 아래로 왔다리 갔다리 하기 후 왼쪽 클릭
            # drag_1 : 여기에 마우스 왼쪽 클릭 후 좌우로 왔다리 갔다리 하기

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\drag_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("drag_1", imgs_)
            drag_pos(300, 600, 800, 600, cla)
            time.sleep(1)
            drag_pos(300, 600, 800, 600, cla)
            time.sleep(1)

            # hwil_mouse_1 : 여기에 마우스 휠 위 아래로 왔다리 갔다리 하기 후 왼쪽 클릭
            # drag_1 : 여기에 마우스 왼쪽 클릭 후 좌우로 왔다리 갔다리 하기

        # 최초 퀘스트 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\tuto_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("tuto_1", imgs_)
            click_pos_2(930, 770, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\tuto_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("tuto_2", imgs_)
            go_ = False
            go_count = 0
            while go_ is False:
                go_count += 1
                if go_count > 5:
                    go_ = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\tuto_22.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    go_ = True
                    print("tuto_22", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    click_pos_2(900, 515, cla)
                time.sleep(0.5)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\tuto_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("tuto_1", imgs_)
            click_pos_2(930, 770, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\tuto_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("tuto_4", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("quest_go_4 보인다 ^ㅅ^", imgs_)
            if camera_ == False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                # 870, (100, 150, 200, 240, 290) random  왼쪽 클릭 후 880, 1010
                time.sleep(2)
                camera_ready = False
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_44.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_go_44", imgs_)
                        result_int = random.randint(0, 4)
                        # 350, 415, 480, 545, 610 // 625
                        x_ = 100 + (int(result_int) * 48)
                        click_pos_2(870, x_, cla)
                        time.sleep(1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        click_pos_2(35, 55, cla)
                        camera_ready = True
                        camera_ = True
                    time.sleep(0.1)

        # 방향 관련
        way = False
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("up", imgs_)
            way = True
            click_pos_reg(imgs_.x, imgs_.y - 50, cla)
        else:

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\up2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("up2", imgs_)
                way = True
                click_pos_reg(imgs_.x, imgs_.y - 50, cla)
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\left.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("left", imgs_)
                    way = True
                    click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\down.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("down", imgs_)
                        way = True
                        click_pos_reg(imgs_.x, imgs_.y + 50, cla)
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\right.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("right", imgs_)
                            way = True
                            click_pos_reg(imgs_.x + 50, imgs_.y, cla)

        if way == True:
            for i in range(10):
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\up.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("up", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                    time.sleep(0.1)
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\up2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("up2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                        time.sleep(0.1)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\left.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("left", imgs_)
                    click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                    time.sleep(0.1)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\down.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("down", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y + 50, cla)
                    time.sleep(0.1)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\way\\right.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("right", imgs_)
                    click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                    time.sleep(0.1)
                time.sleep(0.1)


        # title

        # 제작 장인
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_jejak_jangin.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 30, 960, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("title_jejak_jangin", imgs_)
            for i in range(5):
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\jejak\\neck.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 150, 990, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("neck", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(250, 130, cla)
                    time.sleep(0.5)
                    click_pos_2(820, 1015, cla)
                    break

                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\jejak\\jangsingoo.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 90, 150, 990, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jangsingoo", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
            time.sleep(0.5)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_22.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("jadong_skill_22", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            for i in range(5):
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_jejak_jangin.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 30, 960, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 55, cla)
                else:
                    break
                time.sleep(0.5)
        else:
            # 제전 관련

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_jejun.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_jejun", imgs_)
                for i in range(5):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_jejun.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(700, 30, 960, 100, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(930, 55, cla)
                    else:
                        break
                    time.sleep(0.2)
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\iljung_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(400, 300, 600, 400, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(700, 340, cla)

                else:
                    # 결사 관련

                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_gyulsa.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(700, 30, 960, 100, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("title_gyulsa", imgs_)
                        for i in range(5):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_gyulsa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(700, 30, 960, 100, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 55, cla)
                            else:
                                break
                            time.sleep(0.2)
                    else:
                        # 기억회복 관련

                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_giuk_hoibok.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 30, 960, 100, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            print("title_giuk_hoibok", imgs_)
                            for i in range(5):
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_giuk_hoibok.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(700, 30, 960, 100, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(930, 55, cla)
                                else:
                                    break
                                time.sleep(0.2)
        # 대화 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talk_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talk_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talk_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talk_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talk_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talk_3", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talk_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talk_4", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talk_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talk_5", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talk_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talk_6", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 아퀴 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_1", imgs_)
            click_pos_2(690, 200, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_2", imgs_)
            click_pos_2(320, 955, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_3", imgs_)
            click_pos_2(780, 330, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_4", imgs_)
            click_pos_2(780, 995, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_5", imgs_)
            click_pos_2(50, 500, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_6", imgs_)
            click_pos_2(770, 970, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_7", imgs_)
            click_pos_2(170, 610, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_8.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_8", imgs_)
            click_pos_2(850, 1010, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\aqui_9.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("aqui_9", imgs_)
            click_pos_2(930, 55, cla)

        # 탈것
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talgut_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talgut_1", imgs_)
            click_pos_2(200, 105, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talgut_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("talgut_2", imgs_)
            click_pos_2(330, 105, cla)
            time.sleep(1)
            click_pos_2(930, 55, cla)
            time.sleep(0.5)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talgut_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("talgut_3", imgs_)
                click_pos_2(930, 55, cla)

        # 어시스트 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\assist_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("assist_1", imgs_)
            click_pos_2(20, 295, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("assist quest_go_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\assist_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("assist_2", imgs_)
            click_pos_2(770, 460, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\assist_55.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("assist_55", imgs_)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\close_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("close_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\assist_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("assist_3", imgs_)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("assist_3 quest_go_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\assist_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("assist_4", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\assist_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("assist_5", imgs_)
                click_pos_2(770, 460, cla)

        # 스탠스 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\stans_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("stans_1", imgs_)
            click_pos_2(885, 220, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\stans_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("stans_2", imgs_)
            click_pos_2(810, 1005, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\stans_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("stans_3", imgs_)
            click_pos_2(240, 290, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\stans_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("stans_4", imgs_)
            click_pos_2(920, 835, cla)

        # 전투준비 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\fight_ready_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("fight_ready_1", imgs_)
            click_pos_2(770, 820, cla)

        # 퀘스트 중간 진행 관련
        if media_ == False:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\media_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("media_1", imgs_)
                media_ = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\media_11.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("media_11", imgs_)
                media_ = True
            if media_ == True:
                click_pos_2(890, 110, cla)

        if talchool_ == False:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talchool_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("talchool_1", imgs_)
                talchool_ = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talchool_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("talchool_2", imgs_)
                talchool_ = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talchool_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("talchool_3", imgs_)
                talchool_ = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talchool_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("talchool_4", imgs_)
                talchool_ = True
            if talchool_ == True:
                click_pos_2(890, 110, cla)

        if prison_ == False:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\prison_open_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                prison_ = True
                print("prison_open_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        if boonji_ == False:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\boonji_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("boonji_1", imgs_)
                boonji_ = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\boonji_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("boonji_2", imgs_)
                boonji_ = True
            if boonji_ == True:
                click_pos_2(890, 110, cla)

        # 가방 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("bag_1", imgs_)
            click_pos_2(820, 55, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("bag_2", imgs_)
            click_pos_2(780, 180, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("bag_3", imgs_)
            click_pos_2(820, 935, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("bag_4", imgs_)
            click_pos_2(150, 50, cla)
            time.sleep(1)
            click_pos_2(820, 55, cla)

        # 물약 구매 등 물약 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(250, 650, 340, 740, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_setting", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_1", imgs_)
            click_pos_2(100, 120, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_2", imgs_)
            click_pos_2(235, 120, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_3", imgs_)
            click_pos_2(180, 1000, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_4", imgs_)
            click_pos_2(160, 220, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_5", imgs_)
            click_pos_2(840, 1000, cla)
            potion_ = False
            potion_count = 0
            while potion_ is False:
                potion_count += 1
                if potion_count > 7:
                    potion_ = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_6.PNG"
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
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_7.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        potion_ = True
                        print("potion_7", imgs_)
                        click_pos_2(530, 590, cla)
                        time.sleep(0.5)
                        click_pos_2(480, 590, cla)
                        time.sleep(0.5)
                        click_pos_2(530, 630, cla)
                        time.sleep(1)
                        click_pos_2(840, 1005, cla)
                        time.sleep(1)
                        click_pos_2(540, 590, cla)
                        time.sleep(1)
                        click_pos_2(930, 55, cla)

                else:
                    print("포션사기 진행 중")
                time.sleep(0.5)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_6.PNG"
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
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_7.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                potion_ = True
                print("potion_7", imgs_)
                click_pos_2(530, 590, cla)
                time.sleep(0.5)
                click_pos_2(480, 590, cla)
                time.sleep(0.5)
                click_pos_2(530, 630, cla)
                time.sleep(1)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_8.PNG"
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
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_9.PNG"
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
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_10.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_10", imgs_)
            click_pos_2(250, 990, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_11.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_11", imgs_)
            click_pos_2(320, 780, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_12.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_12", imgs_)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_13.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("potion_13", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\potion_14.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("potion_14", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 장비착용 관련
        # 추후 수정

        # 귀환석 사용
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\guihwansuk_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("guihwansuk_1", imgs_)
            click_pos_2(820, 935, cla)

        # 귀환석 사용
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jejak_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("jejak_1", imgs_)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jejak_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("jejak_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.7)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jejak_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("jejak_3", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.7)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jejak_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("jejak_4", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                click_pos_2(820, 1010, cla)
            time.sleep(1.7)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("jejak quest_go_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1.7)
                click_pos_2(930, 55, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("jejak exit_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

        # sub 퀘스트 관련 서브퀘스트
        subquest_ = False
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\sub_quest_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(700, 60, 960, 300, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("sub_quest_1", imgs_)
            subquest_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\sub_quest_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(700, 60, 960, 300, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("sub_quest_2", imgs_)
                subquest_ = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\sub_quest_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(700, 60, 960, 300, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("sub_quest_3", imgs_)
                    subquest_ = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\sub_quest_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(700, 60, 960, 300, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("sub_quest_4", imgs_)
                        subquest_ = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\sub_quest_5.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 60, 960, 300, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            print("sub_quest_5", imgs_)
                            subquest_ = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\sub_quest_6.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(700, 60, 960, 300, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                print("sub_quest_6", imgs_)
                                subquest_ = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)

        if subquest_ == True:
            sub_count_ = 0
            sub_ = False
            while sub_ is False:
                sub_count_ += 1

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_22.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_skill_22", imgs_)
                    sub_ = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("sub exit_1", imgs_)

                    map_ = False
                    map_count = 0
                    while map_ is False:
                        map_count += 1
                        if map_count > 6:
                            map_ = True
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            print("sub exit_1_x", imgs_)
                            click_pos_2(930, 55, cla)
                        else:
                            map_ = True
                            sub_ = True
                        time.sleep(0.5)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\dogam_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("dogam_1", imgs_)

                    dogam_ = False
                    dogam_count = 0
                    while dogam_ is False:
                        dogam_count += 1
                        if dogam_count >6:
                            dogam_ = True
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\dogam_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            print("dogam_1_x", imgs_)
                            click_pos_2(790, 320, cla)
                        else:
                            dogam_ = True
                            sub_ = True
                        time.sleep(0.5)

                if sub_count_ > 100:
                    sub_count_ = 0
                    sub_ = True
                    # line_to_me(cla, "subquest_에 문제 있다 코딩 수정하기 바람.")

        # skill_bag 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_1", imgs_)
            click_pos_2(780, 120, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_2", imgs_)
            click_pos_2(720, 180, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_3", imgs_)
            click_pos_2(820, 935, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_4", imgs_)
            click_pos_2(160, 285, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_5", imgs_)
            click_pos_2(720, 640, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_6", imgs_)
            click_pos_2(800, 800, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_7", imgs_)
            click_pos_2(865, 995, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_8.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_8", imgs_)
            click_pos_2(540, 600, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_9.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_9", imgs_)
            click_pos_2(865, 995, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_bag_10.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_bag_10", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1.5)
            click_pos_2(930, 55, cla)
            time.sleep(1)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("skill_", imgs_)
                click_pos_2(930, 55, cla)
            time.sleep(1)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("bag_open", imgs_)
                click_pos_2(820, 55, cla)



        # 귀환 관련
        quihwan_ = False
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quihwan_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("quihwan_1", imgs_)
            quihwan_ = True
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quihwan_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("quihwan_2", imgs_)
            quihwan_ = True
        if quihwan_ == True:
            click_pos_2(750, 865, cla)
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\talk_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(500, 600, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("talk_", imgs_)
                click_pos_reg(imgs_.x + 80, imgs_.y, cla)

        # 장비착용 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jangbi_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 600, 650, 700, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("jangbi_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jangbi_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("jangbi_2", imgs_)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jangbi_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("jangbi_3", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jangbi_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("jangbi_4", imgs_)
            click_pos_2(720, 180, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jangbi_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("jangbi_5", imgs_)
            click_pos_2(740, 900, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jangbi_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("jangbi_6", imgs_)
            click_pos_2(520, 240, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jangbi_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("jangbi_7", imgs_)
            click_pos_2(900, 1005, cla)
            out_ = False
            out_count = 0
            while out_ is False:
                out_count += 1
                if out_count > 6:
                    out_ = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_1", imgs_)
                    click_pos_2(930, 55, cla)
                else:
                    out_ = True
                    time.sleep(2.3)
                    click_pos_2(820, 55, cla)
                time.sleep(0.3)

        # 주문석 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_1", imgs_)
            click_pos_2(780, 120, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_2", imgs_)
            click_pos_2(725, 180, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_3", imgs_)
            click_pos_2(820, 940, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_4", imgs_)
            click_pos_2(140, 290, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_5", imgs_)
            click_pos_2(810, 170, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_6", imgs_)
            click_pos_2(430, 470, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_66.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_66", imgs_)
            click_pos_2(530, 410, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_7", imgs_)
            click_pos_2(655, 595, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_8.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_8", imgs_)
            click_pos_2(520, 680, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_9.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_9", imgs_)
            click_pos_2(930, 55, cla)
            time.sleep(2)
            click_pos_2(930, 55, cla)
            time.sleep(2)
            click_pos_2(820, 55, cla)
            # click_pos_2(530, 410, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\joomoonsuk_10.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("joomoonsuk_10", imgs_)
            click_pos_2(930, 360, cla)
            time.sleep(2)
            click_pos_2(930, 55, cla)
            time.sleep(2)
            click_pos_2(820, 55, cla)

        # 마을메뉴 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\maul_menu_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("maul_menu_1", imgs_)
            click_pos_2(20, 120, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\maul_menu_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("maul_menu_2", imgs_)
            click_pos_2(60, 150, cla)
            maul_ = False
            out_count = 0
            while maul_ is False:
                out_count += 1
                if out_count > 6:
                    maul_ = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\maul_menu_8.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    maul_ = True
                    print("maul_menu_8", imgs_)
                    click_pos_2(820, 1010, cla)
                    time.sleep(1)
                    click_pos_2(930, 55, cla)
                else:
                    click_pos_2(820, 1010, cla)
                time.sleep(0.3)

        # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\maul_menu_3.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        # if imgs_ is not None and imgs_ != False:
        #     print("maul_menu_3", imgs_)
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\maul_menu_4.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        # if imgs_ is not None and imgs_ != False:
        #     print("maul_menu_4", imgs_)
        #     click_pos_reg(imgs_.x, imgs_.y, cla)

        # 소마 관련
        soma_ = False
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\soma_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("soma_1", imgs_)
            soma_ = True

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\soma_11.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("soma_11", imgs_)
            soma_ = True

        if soma_ == True:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\soma_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("soma_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\soma_22.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("soma_22", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\soma_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("soma_3", imgs_)
            click_pos_2(820, 930, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\soma_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("soma_4", imgs_)
            bag_ = False
            out_count = 0
            while bag_ is False:
                out_count += 1
                if out_count > 7:
                    bag_ = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_open.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("soma bag_open", imgs_)
                    click_pos_2(820, 55, cla)
                else:
                    bag_ = True
                time.sleep(0.5)

        # 강화주문서 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_1", imgs_)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("ganghwa_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_22.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("ganghwa_22", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_3", imgs_)
            click_pos_2(820, 930, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_4", imgs_)
            click_pos_2(690, 85, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_5", imgs_)
            click_pos_2(220, 160, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_6", imgs_)
            click_pos_2(430, 160, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_7", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_8.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_8", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_9.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_9", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\ganghwa_10.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_10", imgs_)
            click_pos_2(330, 980, cla)
            time.sleep(1)
            click_pos_2(575, 70, cla)

        # skill 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_get.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skill_get", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
            click_pos_2(930, 55, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_22.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("jadong_skill_22", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\core_skill_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("core_skill_1", imgs_)
            click_pos_2(240, 290, cla)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("jadong_skill", imgs_)
            click_pos_2(225, 300, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_11.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("jadong_skill_11", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("jadong_skill_2", imgs_)
            click_pos_2(500, 610, cla)
            skill_ = False
            out_count = 0
            while skill_ is False:
                out_count += 1
                if out_count > 7:
                    skill_ = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_22.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    skill_ = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    click_pos_2(480, 750, cla)
                time.sleep(1)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\select_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("select_1", imgs_)
            click_pos_2(920, 55, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_get_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("skill_get_2", imgs_)
            click_pos_2(740, 150, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\new_skill_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("new_skill_1", imgs_)
            click_pos_2(480, 750, cla)
            time.sleep(1.5)
            click_pos_2(480, 750, cla)
            time.sleep(1)
            click_pos_2(930, 55, cla)
            time.sleep(1)
            click_pos_2(745, 140, cla)
            time.sleep(1)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_11.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("jadong_skill_11", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_get.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("skill_get", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                drag_pos(140, 910, 140, 270, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skill_get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("skill_get", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jadong_skill_11.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("jadong_skill_11", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(2)
            click_pos_2(930, 55, cla)

            # full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\new_skill_2.PNG"
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            # if imgs_ is not None and imgs_ != False:
            #     print("new_skill_2", imgs_)
            #     click_pos_reg(imgs_.x, imgs_.y, cla)
            #     skill_ = False
            #     while skill_ is False:
            #         full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\exit_1.PNG"
            #         img_array = np.fromfile(full_path, np.uint8)
            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #         imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            #         if imgs_ is not None and imgs_ != False:
            #             skill_ = True
            #             print("exit_1", imgs_)
            #             click_pos_reg(imgs_.x, imgs_.y, cla)
            #         time.sleep(0.5)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(700, 30, 960, 200, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("skip_1 보인다 ^ㅅ^", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skip_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(700, 30, 960, 200, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("skip_2 보인다 ^ㅅ^", imgs_)
                click_pos_reg(imgs_.x, imgs_.y - 5, cla)
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\skip__2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(700, 30, 960, 200, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("skip__2 보인다 ^ㅅ^", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y - 5, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("quest_go_1 보인다 ^ㅅ^", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("quest_go_2 보인다 ^ㅅ^", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_11.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("quest_go_11 보인다 !!!!!!!!!!!!!!!!!!!!!! ^ㅅ^", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("quest_go_3 보인다 ^ㅅ^", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("quest_go_1 보인다 ^ㅅ^", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("quest_go_4 보인다 ^ㅅ^", imgs_)
            if camera_ == False:

                click_pos_reg(imgs_.x, imgs_.y, cla)
                # 870, (100, 150, 200, 240, 290) random  왼쪽 클릭 후 880, 1010
                time.sleep(2)
                camera_ready = False
                camera_ready_count = 0
                while camera_ready is False:
                    camera_ready_count += 1
                    if camera_ready_count > 7:
                        camera_ready = True
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\quest_go_44.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_go_44", imgs_)
                        result_int = random.randint(0, 4)
                        # 350, 415, 480, 545, 610 // 625
                        x_ = 100 + (int(result_int) * 48)
                        click_pos_2(870, x_, cla)
                        time.sleep(1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        click_pos_2(35, 55, cla)
                        camera_ready = True
                        camera_ = True
                    time.sleep(0.5)
            if camera_ == True:
                click_pos_2(865, 145, cla)
                camera_count += 1

                if camera_count > 5:
                    camera_count = 0
                    camera_ = False

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\grow_f.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("보인다 grow_f !!!!!!!!!!!!!!!!!!!!!! ^ㅅ^", imgs_)
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\exit_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("exit_3", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
            click_pos_2(890, 110, cla)
            force_quest = 0
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\grow_f_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("보인다 grow_f_1 !!!!!!!!!!!!!!!!!!!!!! ^ㅅ^", imgs_)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\exit_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_3", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                click_pos_2(890, 110, cla)
                force_quest = 0
            else:
                force_quest += 1
                print("grow_f 안보인당 ㅠㅠㅠㅠㅠ", force_quest)
                if force_quest > 5:
                    clean_screen(cla)
                    force_quest = 0
                elif force_quest > 1:

                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("bag_open", imgs_)
                        click_pos_2(930, 120, cla)
                    else:

                        world_map = False

                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("worldmap_1", imgs_)
                            world_map = True
                            click_pos_2(930, 55, cla)
                            time.sleep(1)
                            click_pos_2(930, 55, cla)
                            time.sleep(1)
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_11.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("worldmap_1", imgs_)
                                world_map = True
                                click_pos_2(930, 55, cla)
                                time.sleep(1)
                                click_pos_2(930, 55, cla)
                                time.sleep(1)

                        if world_map == True:
                            for i in range(5):
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(930, 55, cla)
                                else:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\worldmap_11.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(930, 55, cla)
                                    else:
                                        break
                                time.sleep(0.3)
                        else:
                            menu_close(cla)

                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\exit_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("exit_3", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(890, 110, cla)

        print("test 2 : 물약체크")
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\grow_f_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("보인다 2 ^ㅅ^", imgs_)
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\grow_f_22.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("보인다 22 ^ㅅ^", imgs_)
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\grow_f_222.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("보인다 222 ^ㅅ^", imgs_)
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\grow_f_2222.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("보인다 2222 ^ㅅ^", imgs_)
                    else:
                        print("불난 f 보이지 않는다")

        # 허공의 편린
        print("허공의 편린")
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\hugong_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("hugong_", imgs_)
            click_pos_2(820, 930, cla)

        # 육성 1장 끝
        grow_1_end = False
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\pracia_story_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("pracia_story_1", imgs_)
            grow_1_end = True
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\pracia_story_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("pracia_story_2", imgs_)
            grow_1_end = True

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\jungi_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jungi_1", imgs_)
            grow_1_end = True

        if grow_1_end == True:
            line_to_me(cla, "육성 1차 끝")
            myQuest_play_add(cla, "튜토육성")

        # 가방 닫기
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\guihwansuk_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("guihwansuk_1", imgs_)
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\bag_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("bag_open", imgs_)
                click_pos_2(820, 55, cla)


    except Exception as e:
        print(e)
