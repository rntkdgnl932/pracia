import sys

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

potion_get_ready = 0
def potion_check(cla, spot):
    global potion_get_ready
    import time
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from massenger import line_to_me
    from daily_mission import request, go_confirm
    from action import clean_screen, gonghun_
    from jadong import jadong_

    import numpy as np
    import cv2
    try:

        print("hi")

    except Exception as e:
        print(e)
        return 0

def potion_setting(cla):
    global potion_get_ready
    import time
    from function_game import click_pos_2, imgs_set_, click_pos_reg
    from action import out_check, clean_screen
    import numpy as np
    import cv2
    try:

        print("potion_setting")

        changed = False

        potion_set_ = False
        potion_set_count = 0
        while potion_set_ is False:
            potion_set_count += 1
            if potion_set_count > 7:
                potion_set_ = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_set.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(275, 685, 325, 735, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("potion_set")
                potion_set_ = True
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\use_potion_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(325, 740, 355, 770, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\use_potion_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 740, 670, 770, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("use_potion_point 1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\use_potion_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(325, 800, 355, 835, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("use_potion_point 2", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                    else:
                        click_pos_2(320, 770, cla)
                    time.sleep(0.5)
                # 포션이 없다면 포션 사러 가야함.
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_have_not_set.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(310, 770, 355, 805, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("potion_have_not_set", imgs_)
                    potion_get_ready = 0
                    maul_potion_get(cla)
                else:
                    potion_get_ready = 0

            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(255, 990, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_set.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(275, 685, 325, 735, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)
                else:
                    clean_screen(cla)
            time.sleep(0.5)

        clean_screen(cla)


    except Exception as e:
        print(e)
        return 0


def potion_quickslot(cla):
    import time
    from function_game import click_pos_2, imgs_set_, click_pos_reg
    from action import out_check, juljun_off, clean_screen
    import numpy as np
    import cv2
    try:
        print("potion_quickslot")

        juljun_off(cla)

        have_quick_potion = False
        have_quick_potion_count = 0
        while have_quick_potion is False:
            have_quick_potion_count += 1
            if have_quick_potion_count > 7:
                have_quick_potion = True

            result_out = out_check(cla)
            if result_out == True:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_have_quickslot.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 960, 730, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("퀵슬롯에 있다.")
                    have_quick_potion = True
                else:
                    click_pos_2(825, 60, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\bag_open.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(630, 140, 685, 195, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(660, 290, cla)
                            break
                        time.sleep(0.3)
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_have_bag.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 150, 940, 830, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_have_bag", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        click_pos_2(700, 990, cla)
                        time.sleep(0.2)
                        clean_screen(cla)
            else:
                clean_screen(cla)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def potion_check(cla):
    global potion_get_ready
    from function_game import click_pos_2, imgs_set_, click_pos_reg, imgs_set
    from action import out_check, juljun_off
    import numpy as np
    import cv2
    try:

        print("potion_check")

        # 절전모드 and 바깥모드

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\juljun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("절전")
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_have_not_juljun.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(670, 960, 730, 1020, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                potion_get_ready += 1
                print("potion_have_not_juljun", potion_get_ready)
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_have_juljun.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 960, 730, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("potion_have_juljun", potion_get_ready)
                else:
                    print("물약 없으니 물약을 퀵슬롯에 배치하기")
                    juljun_off(cla)
                    potion_quickslot(cla)
        else:
            result_out = out_check(cla)

            if result_out == True:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_have_not.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 960, 290, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    potion_get_ready += 1
                    print("potion_have_not", potion_get_ready)

                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\potion_have.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(220, 960, 290, 1020, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_have", potion_get_ready)
                    else:
                        potion_get_ready += 1
                        print("potion", potion_get_ready)


        # 절전모드는 바로 사러 가고, 절전모드 아닐때는 셋팅화면 다시 분석하고 맞을 경우 사러가야함.
        # 물약사러 가야함
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\juljun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
        if imgs_ is not None and imgs_ != False:
            if potion_get_ready > 1:
                juljun_off(cla)
                maul_potion_get(cla)
        else:
            if potion_get_ready > 5:
                potion_setting(cla)

    except Exception as e:
        print(e)
        return 0

def maul_potion_get(cla):
    global potion_get_ready
    import time
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from massenger import line_to_me
    from daily_mission import request, go_confirm
    from action import clean_screen, gonghun_, menu_open, quest_move_m
    from jadong import jadong_

    import numpy as np
    import cv2
    try:

        # 공헌부터..
        gonghun_(cla)

        potion_get_ready = 0

        potion_get = False
        potion_get_count = 0
        while potion_get is False:
            potion_get_count += 1
            if potion_get_count > 7:
                potion_get = True

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 990, 60, 1040, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)

                # 범례 체크 해제 후 마을만 클릭
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\bum.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(40, 80, 90, 120, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\all_look.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(40, 950, 120, 1000, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\all_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(5, 950, 50, 1000, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\bum_maul.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(5, 100, 60, 500, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\bum.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(40, 80, 90, 120, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                            else:
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\all_look.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(40, 950, 120, 1000, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    print("마을클릭")
                    look = False
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\jabhwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(715, 175, 960, 760, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            look = True
                            break
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\maul.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("maul", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                        time.sleep(0.5)



                    print("지도나가기")
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\map\\worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 990, 60, 1040, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(930, 55, cla)
                        else:
                            break
                        time.sleep(0.3)

                    if look == False:

                        for i in range(10):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\maul_list_jabhwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(25, 135, 70, 300, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                click_pos_2(20, 120, cla)
                            time.sleep(0.5)


                    print("이동중인지 체크")
                    going = False
                    for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("이동중 m1")
                            going = True
                            break
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("이동중 m2")
                                going = True
                                break
                            else:
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_x.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("이동중 x")
                                    going = True
                                    break
                        time.sleep(0.2)


                    if going == True:
                        quest_move_m(cla)

                    print("잡화상점 진입")


                    # 물약 선택택
                    buy_now = False
                   for i in range(10):
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\jabwha_check.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(200, 100, 260, 140, cla, img)
                        if imgs_ is not None and imgs_ != False:

                            # 일반 장비 팔기

                            click_pos_2(235, 120, cla)
                            time.sleep(0.3)
                            click_pos_2(710, 1000, cla)
                            time.sleep(0.3)
                            click_pos_2(840, 1000, cla)
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\buy_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(480, 570, 620, 660, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)

                            for c in range(10):
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\jabhwa_small_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(80, 170, 170, 220, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    click_pos_2(100, 120, cla)
                                time.sleep(0.5)

                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\jabhwa_small_potion.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(80, 170, 170, 220, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                # 물약 사기 함수 시작
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\lv48.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(145, 275, 240, 320, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\jabhwa_small_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(80, 170, 170, 220, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    click_pos_2(140, 300, cla)
                                buy_now = True
                                break
                            else:
                                for c in range(10):
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\jabwha_check.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(200, 100, 260, 140, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(930, 55, cla)
                                    else:
                                        break
                                    time.sleep(0.4)
                                break
                        else:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\out_jabhwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 30, 960, 1040, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)

                    if buy_now == True:

                        for i in range(10):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(440, 320, 520, 360, cla, img)
                            if imgs_ is not None and imgs_ != False:

                                click_pos_2(370, 590, cla)
                                time.sleep(0.5)

                                for c in range(7):
                                    click_pos_2(530, 590, cla)
                                    time.sleep(0.1)
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\buy_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(480, 600, 620, 660, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    click_pos_2(850, 1000, cla)
                                    time.sleep(0.2)
                                    potion_get = True

                                    for c in range(10):
                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\jabwha_check.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(200, 100, 260, 140, cla, img)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(930, 55, cla)
                                        else:
                                            break
                                        time.sleep(0.4)

                                    break

                            else:
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\lv48.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(145, 275, 240, 320, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\potion\\jabhwa_small_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(80, 170, 170, 220, cla, img)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    click_pos_2(140, 300, cla)
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




def potion_get_1000(cla):
    try:
        import time
        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import gonghun_, clean_screen

        import numpy as np
        import cv2
        from massenger import line_to_me
        full_path = "c:\\pracia\\imgs\\grow\\grow_2\\potion_6.PNG"
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
                        if potion__result[list] == "가" or potion__result[list] == '방' or potion__result[list] == '이' or \
                                potion__result[list] == '무':
                            ispotion = True
                    except:
                        pass
            if ispotion == True:
                line_to_me(cla, "가방이 개 무거워 ㅠㅠ 프라시아")

                full_path = "c:\\pracia\\imgs\\common\\potion_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(80, 180, 200, 230, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 55, cla)
                    time.sleep(0.1)
                    gonghun_(cla)
                    time.sleep(0.1)
                    clean_screen(cla)
                    full_path = "c:\\pracia\\imgs\\grow\\grow_2\\sangin_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 260, 530, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        potion_get_1000(cla)
            else:
                time.sleep(1)
                full_path = "c:\\pracia\\imgs\\grow\\grow_2\\potion_7.PNG"
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

                    full_path = "c:\\pracia\\imgs\\grow\\grow_2\\potion_8.PNG"
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
                        full_path = "c:\\pracia\\imgs\\grow\\grow_2\\potion_9.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            potion_ = True
                            print("potion_9", imgs_)
                            #click_pos_2(530, 590, cla)
                            #click_pos_2(430, 590, cla)
                            time.sleep(0.5)
                            click_pos_2(530, 630, cla)
                            time.sleep(1)

                            click_pos_2(840, 1005, cla)
                            time.sleep(1)
                            click_pos_2(540, 590, cla)
                            time.sleep(1)
                            click_pos_2(930, 55, cla)
                            time.sleep(1)
                            click_pos_2(20, 120, cla)
    except Exception as e:
        print(e)
        return 0

# def jadong(cla, spot):
#     try:
#         import time
#         from function_game import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get
#         import numpy as np
#         import cv2
#         from massenger import line_to_me
#
#         jadong_1 = False
#         while jadong_1 is False:
#             full_path = "c:\\pracia\\imgs\\grow\\grow_2\\worldmap_1.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
#             if imgs_ is not None and imgs_ != False:
#
#                 full_path = "c:\\pracia\\imgs\\grow\\grow_2\\worldmap_4.PNG"
#                 img_array = np.fromfile(full_path, np.uint8)
#                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                 imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
#                 if imgs_ is not None and imgs_ != False:
#
#                     map_in_ = False
#                     while map_in_ is False:
#                         full_path = "c:\\pracia\\imgs\\grow\\grow_2\\worldmap_5.PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
#                         if imgs_ is not None and imgs_ != False:
#                             click_pos_reg(imgs_.x, imgs_.y, cla)
#
#                             time.sleep(1)
#
#                             full_path = "c:\\pracia\\imgs\\grow\\grow_2\\worldmap_4.PNG"
#                             img_array = np.fromfile(full_path, np.uint8)
#                             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                             imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
#                             if imgs_ is not None and imgs_ != False:
#                                 click_pos_reg(imgs_.x, imgs_.y, cla)
#
#                             map_in_ = True
#                             time.sleep(1)
#                         else:
#                             full_path = "c:\\pracia\\imgs\\grow\\grow_2\\worldmap_4.PNG"
#                             img_array = np.fromfile(full_path, np.uint8)
#                             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                             imgs_ = imgs_set(0, 0, 200, 1030, cla, img)
#                             if imgs_ is not None and imgs_ != False:
#                                 click_pos_reg(imgs_.x, imgs_.y, cla)
#                                 time.sleep(1)
#
#
#                 full_path = "c:\\pracia\\imgs\\jadong\\" + str(spot) + ".PNG"
#                 img_array = np.fromfile(full_path, np.uint8)
#                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                 imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
#                 if imgs_ is not None and imgs_ != False:
#                     click_pos_reg(imgs_.x, imgs_.y - 33, cla)
#                     jadong_1 = True
#                     jadong_2 = False
#                     while jadong_2 is False:
#                         full_path = "c:\\pracia\\imgs\\jadong\\jadong_move_.PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
#                         if imgs_ is not None and imgs_ != False:
#                             click_pos_reg(imgs_.x, imgs_.y, cla)
#                             time.sleep(1)
#                             click_pos_2(930, 55, cla)
#                             time.sleep(120)
#                             click_pos_2(930, 765, cla)
#                             jadong_2 = True
#
#             else:
#                 click_pos_2(100, 180, cla)
#                 time.sleep(2)
#         full_path = "c:\\pracia\\imgs\\grow\\grow_2\\grow_f.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(880, 700, 960, 1030, cla, img, 0.9)
#         if imgs_ is not None and imgs_ != False:
#             print("자동사냥 시작")
#             click_pos_reg(imgs_.x, imgs_.y, cla)
#     except Exception as e:
#         print(e)
#         return 0