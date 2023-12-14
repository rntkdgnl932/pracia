import sys
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla, spot):

    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from action import quest_move_m, menu_open, juljun_attack_check
    from potion import potion_check
    import numpy as np
    import cv2
    try:

        # spot => 사냥_어스름깃털언덕

        print("jadong_start", spot)
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\juljun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("juljun_1", imgs_)
            # 골드 변화 파악 후 변화 없으면 공격하기 버튼
            juljun_attack_check(cla)
            # 물약 파악 후 없으면 물약사기
            potion_check(cla)
        else:
            # 현재 사냥터로 이동하기
            jadong_spot_go(cla, spot)



    except Exception as e:
        print(e)
        return 0


def jadong_spot_go(cla, spot):
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from action import quest_move_m, menu_open, juljun_off, juljun_on, juljun_attack_check
    import numpy as np
    import cv2
    try:

        # spot => 사냥_어스름깃털언덕

        print("jadong_start", spot)

        result_spot = spot.split("_")

        file_path = "C:\\my_games\\pracia\\data_pracia\\imgs\\jadong\\jadong_list.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            jadong_list = file.read().splitlines()
            print("jadong_list", jadong_list)

        for i in range(len(jadong_list)):
            result = jadong_list[i].split("_")
            if result[0] == result_spot[1]:
                spot_name = result[1]



        spot_in = False
        spot_in_count = 0
        while spot_in is False:
            spot_in_count += 1
            if spot_in_count > 7:
                spot_in = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 990, 60, 1040, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)

                # 표지목록 클릭 후 이동하기
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\pyoji_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(740, 80, 800, 130, cla, img)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\spot_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(715, 940, 770, 990, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\jadong\\jadong_world_list\\" + str(spot_name) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(715, 220, 950, 950, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)


                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\pyoji_list_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(880, 290, 950, 370, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                # 이동하는지 quest_move_m 으로 체크하고 이동 끝났으면 공격하기 버튼

                move = False
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_x.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        move = True
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            move = True
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                move = True
                            else:
                                move = False
                    if move == True:
                        quest_move_m(cla)
                    else:
                        time.sleep(0.5)

                # 월드맵 나가서 공격하기 버튼 후 절전모드
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\worldmap.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 990, 60, 1040, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(930, 55, cla)
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\grow_f.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(880, 700, 960, 1030, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("자동사냥 시작")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            juljun_on(cla)
                            result_attack = juljun_attack_check(cla)
                            if result_attack == True:
                                spot_in = True
                                break
                        else:
                            result_attack = juljun_attack_check(cla)
                            if result_attack == True:
                                spot_in = True
                                break

                    time.sleep(0.5)


            else:
                menu_open(cla)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\menu_worldmap.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(625, 365, 950, 550, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("menu_worldmap", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 990, 60, 1040, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.4)

    except Exception as e:
        print(e)
        return 0

def now_hunting(cla):
    try:
        global assist_count
        from potion import maul_potion_get
        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, int_put_, click_pos_reg
        from action import juljun_off, level_up, clean_screen, menu_open
        import numpy as np
        import cv2



        # if attack_check == 0:

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\grow_f.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 700, 960, 1030, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("자동사냥 시작")
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # attack_check += 1
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