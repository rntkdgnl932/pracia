import sys
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

once = False

def jungi_start(cla, data):
    global once
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from action import menu_open, clean_screen, juljun_off, level_up, dead_die
    from massenger import line_to_me
    from potion import maul_potion_get
    from schedule import myQuest_play_add
    import numpy as np
    import cv2
    import random
    try:
        # data = "전기_카시미르연합", "전기_황혼의형제들". "전기_아슬라니스". "전기_신기루연대"
        print("jungi_start", data)


        juljun_off(cla)
        time.sleep(0.5)

        if once == False:
            go_jungi(cla, data)
            once = True

        else:
            # 퀘스트 진행
            quest_ing(cla)




    except Exception as e:
        print(e)
        return 0

def go_jungi(cla, data):
    import cv2
    import numpy as np
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import menu_open
    try:

        # data = "전기_카시미르연합", "전기_황혼의형제들". "전기_아슬라니스". "전기_신기루연대"

        print("go_jungi", data)

        result_data = data.split("_")

        file_path = "C:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\jungi_list.txt"
        with open(file_path, "r", encoding='utf-8-sig') as file:
            jungi_read = file.read().splitlines()
            print("jungi_read", jungi_read)

            for i in range(len(jungi_read)):
                result_jungi_read = jungi_read[i].split("_")
                if result_jungi_read[0] == result_data[1]:
                    img_name = result_jungi_read[1]



        in_jungi = False
        in_jungi_count = 0
        while in_jungi is False:
            in_jungi_count += 1
            if in_jungi_count > 7:
                in_jungi = True

            jungi_title = False

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_jungi.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_jungi")
                jungi_title = True
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_jungi2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("title_jungi2")
                    jungi_title = True

            if jungi_title == True:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\jungi_title\\" + str(img_name) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 120, 220, 180, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("episode_title", img_name)
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\jadong_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 970, 930, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jadong_click!!!!!!!!!!!!!!!")
                        in_jungi = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                else:

                    # 초이스 하기
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\linea.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 90, 140, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("linea")



                        for i in range(10):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\episode_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(630, 970, 930, 1020, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\jungi_choice\\" + str(img_name) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 400, 930, 530, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("episode_click", img_name)
                                    click_pos_reg(imgs_.x, imgs_.y + 100, cla)
                            time.sleep(0.5)


                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\episode_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(630, 970, 930, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("episode_click")
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm")
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\jungi_title\\" + str(img_name) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(40, 120, 220, 180, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("episode_title", img_name)
                                        break
                                time.sleep(0.5)
                    else:
                        for i in range(10):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\sigantmbagui.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(180, 80, 300, 130, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("sigantmbagui")
                                break
                            else:
                                click_pos_2(80, 100, cla)
                            time.sleep(0.5)

            else:
                menu_open(cla)
                click_pos_2(790, 200, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\title\\title_jungi.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0


def quest_ing(cla):
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from action import menu_open, clean_screen, juljun_off, level_up, dead_die, quest_move_m
    from massenger import line_to_me
    from potion import maul_potion_get, potion_check
    from schedule import myQuest_play_add
    import numpy as np
    import cv2
    import random
    try:
        # data = "전기_카시미르연합", "전기_황혼의형제들". "전기_아슬라니스". "전기_신기루연대"
        print("quest_ing")


        quest_ = False
        quest_count = 0
        while quest_ is False:
            quest_count += 1
            if quest_count > 7:
                quest_ = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\quest_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 100, 780, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\quest_jadong_cancle_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 990, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    quest_ = True
                    print("potion 챙기자")
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        quest_move_m(cla)
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            quest_move_m(cla)
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_x.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                quest_move_m(cla)
                            else:
                                potion_check(cla)

                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\quest_jadong_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 990, 950, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\use.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 660, 540, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            time.sleep(0.5)


            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\use.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 660, 540, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                else:
                    menu_open(cla)
                    click_pos_2(730, 195, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jungi\\quest_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 100, 780, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)






    except Exception as e:
        print(e)
        return 0

