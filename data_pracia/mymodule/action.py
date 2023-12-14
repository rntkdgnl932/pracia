import sys
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


potion_get_ready = 0


def juljun_off(cla):
    import numpy as np
    import cv2
    from function_game import drag_pos, imgs_set
    try:
        for i in range(10):
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\juljun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("juljun_1", imgs_)
                x_ = imgs_.x
                y_ = imgs_.y
                drag_pos(x_, y_, x_ + 500, y_, cla)
            else:
                break
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def juljun_on(cla):
    import numpy as np
    import cv2
    from function_game import drag_pos, imgs_set, click_pos_reg
    try:
        for i in range(10):
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\juljun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\juljun\\juljun_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 320, 45, 365, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    clean_screen(cla)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0




def clean_screen(cla):
    try:
        from function_game import click_pos_2, imgs_set, imgs_set_, random_int, text_check_get, click_pos_reg
        from massenger import line_to_me
        from stop_event18 import _stop_please
        import numpy as np
        import cv2

        out_ = False
        clean_screen_count = 0

        juljun_off(cla)

        _stop_please(cla)

        dead_die(cla)

        for i in range(5):

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\gongan_june_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 650, 550, 700, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            # else:
            #     click_pos_2(540, 675, cla)

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\r_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\r_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\r_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break

            if out_ == True:
                print("바깥화면임")
            else:
                # clean_screen_count += 1
                # if clean_screen_count > 10:
                #     out_ = True
                #     line_to_me(cla, "프라시아 clean screen 무한 반복중이라 중단함")
                #     clean_screen_count = 0

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
                    click_pos_2(930, 55, cla)
                    time.sleep(0.2)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\confirm_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\confirm_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\x_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\x_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\x_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\x_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\out_check\\menu_close.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\exit_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\exit_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\exit_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\jejak_dogam.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 300, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(790, 320, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\gyulsa_boodae.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 300, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(880, 335, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\prasia_jejun.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 300, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(890, 335, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\sangjum.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 55, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\bag_open.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 120, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\quest_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 120, cla)

                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\gonghun_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(450, 50, 520, 120, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(920, 105, cla)

    except Exception as e:
        print(e)
        return 0


def menu_open(cla):
    from function_game import click_pos_2, imgs_set_, click_pos_reg
    import numpy as np
    import cv2
    try:

        print("menu_open")

        out_ = False
        menu_ = False

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            menu_ = True
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\r_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                out_ = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\r_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                out_ = True

        if menu_ == False:
            if out_ == False:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\menu_open\\menu_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 30, 900, 90, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    clean_screen(cla)
                    time.sleep(1)
                    click_pos_2(930, 55, cla)
            else:
                click_pos_2(930, 55, cla)

            for i in range(10):
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\common\\menu_quest_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 120, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    menu_ = True
                    break
                time.sleep(0.3)

        return menu_
    except Exception as e:
        print(e)
        return 0

def menu_close(cla):
    from function_game import click_pos_reg, imgs_set
    import numpy as np
    import cv2
    try:


        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\menu_x.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(800, 30, 960, 150, cla, img)
        if imgs_ is not None and imgs_ != False:
            x_2 = False
            x_2_count = 0
            while x_2 is False:
                x_2_count += 1
                if x_2_count > 5:
                    x_2 = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\menu_x.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(800, 30, 960, 150, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("x_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    x_2 = True
                time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def menu_open_after_bag(cla):
    try:
        from function_game import click_pos_2, imgs_set_
        import numpy as np
        import cv2
        menu_open(cla)
        bag_open = False
        bag_open_count = 0
        while bag_open is False:
            bag_open_count += 1
            if bag_open_count > 7:
                bag_open = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\bag_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                bag_open = True
            else:
                click_pos_2(825, 60, cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    from function_game import click_pos_2, imgs_set_
    import numpy as np
    import cv2
    try:
        print("out_check")

        out_result = False

        out_ = False

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\out_check\\out_camera_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(65, 980, 110, 1020, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            out_ = True
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\out_check\\out_camera_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(65, 980, 110, 1020, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                out_ = True

        if out_ == True:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\out_check\\menu_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(890, 30, 950, 90, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("메뉴 열려 있다.")
            else:
                out_result = True

        return out_result
    except Exception as e:
        print(e)
        return 0


def login_check(cla):
    from function_game import click_pos_2, imgs_set_
    import numpy as np
    import cv2
    try:
        print("login_check")

        login = False

        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 320, 855, 355, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("18_1", imgs_)
            login = True
        else:
            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 500, 220, 580, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("18_2", imgs_)
                login = True
            else:
                full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\x_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(730, 350, 780, 400, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("x_4", imgs_)
                    login = True
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\out_check\\out_camera_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(65, 980, 110, 1020, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        login = True
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\out_check\\out_camera_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(65, 980, 110, 1020, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            login = True

        return login
    except Exception as e:
        print(e)
        return 0

def loading_check(cla):
    from function_game import click_pos_2, imgs_set_
    import numpy as np
    import cv2
    try:
        print("loading_check")


        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\loading\\loading.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 800, 960, 960, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            loading = False
            loading_count = 0
            while loading is False:
                loading_count += 1
                if loading_count > 7:
                    loading = True
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\loading\\loading.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 800, 960, 960, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    loading_count = 0
                else:
                    result_out = login_check(cla)
                    if result_out == True:
                        loading = True
                time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0

def r_2_reset(cla):
    from function_game import click_pos_2, imgs_set, imgs_set_, random_int, text_check_get
    import numpy as np
    import cv2
    try:

        clean_screen(cla)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 700, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            v_.r_2_ = False
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\daily_mission\\r_2_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 200, 920, 250, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(735, 230, cla)
            else:
                click_pos_2(935, 155, cla)
                time.sleep(0.5)
                click_pos_2(735, 230, cla)
        else:
            v_.r_2_ = False


    except Exception as e:
        print(e)
        return 0

def level_up(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    try:


        # level_up 관련
        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_1\\level_up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            level_up_ = False
            while level_up_ is False:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\level_up.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(473, 723, cla)
                else:
                    level_up_ = True


    except Exception as e:
        print(e)
        return 0

def go_confirm_yes(cla):
    try:
        import numpy as np
        import cv2
        from function_game import imgs_set_, click_pos_reg

        go_ = False

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            go_ = True

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\confirm_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            go_ = True

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\confirm_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            go_ = True



        return go_
    except Exception as e:
        print(e)
        return 0

def gonghun_(cla):
    try:
        import numpy as np
        import cv2
        from function_game import imgs_set_, click_pos_2, click_pos_reg

        menu_open_after_bag(cla)
        isgonghun_1 = False
        while isgonghun_1 is False:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\bag_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                isgonghun_1 = True
                click_pos_reg(imgs_.x, imgs_.y, cla)


                isgonghun_2 = False
                while isgonghun_2 is False:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\gonghun\\gonghun_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 500, 600, 550, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        isgonghun_2 = True

                        isgonghun_3 = False
                        while isgonghun_3 is False:
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\gonghun\\gonghun_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 900, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                isgonghun_3 = True

                                isgonghun_4 = False
                                isgonghun_4_count = 0
                                while isgonghun_4 is False:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\gonghun\\gonghun_4.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(350, 500, 600, 550, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        isgonghun_4_count += 1
                                        print("공헌템 없다")
                                        time.sleep(0.2)
                                        if isgonghun_4_count > 5:
                                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\gonghun_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(450, 50, 520, 120, cla, img, 0.83)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_2(920, 105, cla)
                                            isgonghun_4 = True
                                    else:
                                        isgonghun_4 = True

                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\gonghun\\gonghun_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(350, 500, 600, 550, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\gonghun\\gonghun_4.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(350, 500, 600, 550, cla, img, 0.83)
                                            if imgs_ is None:
                                                click_pos_2(555, 965, cla)

                                        print("hi")
                                        isgonghun_5 = False
                                        while isgonghun_5 is False:
                                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\gonghun\\gonghun_3.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(300, 650, 500, 750, cla, img, 0.83)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                isgonghun_5 = True
                                            else:
                                                print("공헌 마무리 중")
                                                time.sleep(0.3)

                                        time.sleep(0.3)




                    else:
                        print("공헌 진행중_2")
                        time.sleep(0.2)



            else:
                print("공헌 진행중_1")
                time.sleep(0.2)

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\clean_screen\\gonghun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(450, 50, 520, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(920, 105, cla)



    except Exception as e:
        print(e)
        return 0



def dead_die(cla):
    try:
        from function_game import click_pos_2, imgs_set_, click_pos_reg
        from massenger import line_to_me
        from schedule import myQuest_play_check, myQuest_play_add

        import numpy as np
        import cv2

        dead_sand = False

        is_die = False

        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\juljun_die_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 100, 800, 160, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            is_die = True
        else:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 300, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                is_die = True
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 650, 960, 900, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    is_die = True

        if is_die == True:
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 650, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("die_confirm_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_confirm_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 650, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("die_confirm_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            result_schedule = myQuest_play_check(v_.now_cla, "check")
            print("result_schedule", result_schedule)
            result_schedule_ = result_schedule[0][2]



            if '육성' in result_schedule_:

                myQuest_play_add(cla, result_schedule_)

                print("result_schedule_", result_schedule_)

            menu_open(cla)

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\dead_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(630, 30, 700, 100, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                dead_sand = True
            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\dead_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 30, 700, 100, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    dead_sand = True
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\dead_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 30, 700, 100, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        dead_sand = True
                    else:
                        print("솨롸있눼")
                        click_pos_2(925, 55, cla)
        if dead_sand == True:
            for i in range(10):
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 100, 960, 200, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.3)

            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 100, 960, 300, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:

                live_ = False
                live_count = 0
                while live_ is False:
                    live_count += 1
                    if live_count > 7:
                        live_ = True
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\die_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 100, 960, 300, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

                        for i in range(10):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\gold_exchange.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(895, 875, 935, 905, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(895, 890, cla)
                            time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\dead_die\\penalty_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 400, 510, 450, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(540, 630, cla)
                                break
                            else:
                                click_pos_2(790, 930, cla)
                            time.sleep(0.5)
                    else:
                        live_ = True
                    time.sleep(0.3)




        return
    except Exception as e:
        print(e)
        return 0


def quest_move_m(cla):
    from function_game import click_pos_2, imgs_set_
    import numpy as np
    import cv2
    try:

        move = False

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

        if move == True:
            move_count = 0
            while move is True:
                move_count += 1
                if move_count > 100:
                    move = False
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("이동중 m1", move_count)
                else:
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("이동중 m2", move_count)
                    else:
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_x.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("이동중 x", move_count)
                        else:

                            re_check = False

                            for i in range(10):
                                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("이동중 m1", move_count)
                                    re_check = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        print("이동중 m2", move_count)
                                        re_check = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\check\\move\\move_x.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 910, 550, 940, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            print("이동중 x", move_count)
                                            re_check = True
                                            break
                                time.sleep(0.3)
                            if re_check == False:
                                move = False
                time.sleep(1)


        return move
    except Exception as e:
        print(e)
        return 0

def juljun_attack_check(cla):
    from function_game import click_pos_2, imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_
    import numpy as np
    import cv2
    try:

        attack_check = False

        attack_ = False
        attack_count = 0
        while attack_ is False:
            attack_count += 1
            if attack_count > 5:
                attack_ = True
            full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\juljun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
            if imgs_ is not None and imgs_ != False:

                attack_ = True

                # 첫번째 골드 파악
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\attack_check\\gold_start.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 835, 150, 865, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        print("no")
                    else:
                        money_ = text_check_get(35, 840, 150, 860, cla)
                        # print("money 1", money_)

                        if "(" in money_:
                            money_result = money_.split("(")
                            fl_money = int_put_(money_result[0])
                            result_digit = fl_money.isdigit()
                        else:
                            fl_money = int_put_(money_)
                            result_digit = fl_money.isdigit()

                        if result_digit == True:
                            int_money1 = int(fl_money)
                            print("money_result? type", int_money1)
                            break
                        else:
                            print("숫자가 아니다.")
                    time.sleep(2)
                # 두번째 골드 파악 후 첫번째와 다른지 파악
                for i in range(10):
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\attack_check\\gold_start.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 835, 150, 865, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        print("공격하고 있지 않음. 절전 나간 후 다시 공격하기 버튼 go")

                        juljun_off(cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\grow_f.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(880, 700, 960, 1030, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("자동사냥 시작")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        juljun_on(cla)

                    else:
                        money_ = text_check_get(35, 840, 150, 860, cla)
                        # print("money 2", money_)

                        if "(" in money_:
                            money_result = money_.split("(")
                            fl_money = int_put_(money_result[0])
                            result_digit = fl_money.isdigit()
                        else:
                            fl_money = int_put_(money_)
                            result_digit = fl_money.isdigit()

                        if result_digit == True:
                            int_money2 = int(fl_money)
                            print("money_result? type", int_money2)

                            if int_money1 != int_money2:
                                attack_check = True
                                break

                        else:
                            print("숫자가 아니다.")
                    time.sleep(2)

            else:
                full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\juljun\\juljun_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 320, 45, 365, cla, img)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\grow\\grow_2\\grow_f.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(880, 700, 960, 1030, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("자동사냥 시작")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\juljun\\juljun_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 320, 45, 365, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    clean_screen(cla)
            time.sleep(0.5)

        return attack_check
    except Exception as e:
        print(e)
        return 0

