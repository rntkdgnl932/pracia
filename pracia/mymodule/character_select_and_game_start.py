import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def game_start_screen(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set
    from massenger import line_to_me


    try:

        # 장시간

        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
            v_.data_folder) + "\\imgs\\check\\jangsigan_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(300, 450, 500, 550, v_.now_cla, img)
        if imgs_ is not None and imgs_ != False:

            time.sleep(0.3)
            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                v_.data_folder) + "\\imgs\\check\\jangsigan_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(410, 580, 540, 630, v_.now_cla, img)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                ms_ = str(v_.this_game) + str(" 장시간")
                line_to_me(v_.now_cla, ms_)

        # 게임화면일 경우 캐릭 선택 화면으로 진입하기...
        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\character\\c_ready_screen.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(20, 40, 160, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # 이건 잘못 클릭시 나가기
            # click_pos_reg(imgs_.x, imgs_.y, cla)
            print("c_ready_screen", imgs_)
            click_pos_2(470, 700, cla)

            for i in range(10):
                full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                    v_.data_folder) + "\\imgs\\character\\c_screen.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 560, 240, 630, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.5)

        # 실수로 새 캐릭터 클릭시...
        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\character\\c_make.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 500, 500, 560, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # 이건 잘못 클릭시 나가기
            print("c_make", imgs_)

            for i in range(10):
                full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\character\\cancle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 600, 480, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    break
                time.sleep(0.5)

        # 캐릭터 선택 화면
        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\character\\c_screen.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(80, 560, 240, 630, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # 캐릭터 선택하기
            character_change(cla, character_id)

        else:
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            if cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            if cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            if cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"

            same = False

            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_id = file.read()
                    if str(character_id) == str(read_id):
                        # 메뉴 안 열어도 됨
                        same = True
            if same == False:
                character_change(cla, character_id)


    except Exception as e:
        print(e)

def character_change(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action import clean_screen, out_check, menu_open, login_check, loading_check
    from massenger import line_to_me
    try:

        # out_check 만들기

        print(str(character_id), "번으로 캐릭터 체인지")


        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True
                line_to_me(cla, "처음 스타트 화면에 문제가 있다.")

            # 실수로 새 캐릭터 클릭시...
            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                v_.data_folder) + "\\imgs\\character\\c_make.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 500, 500, 560, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 이건 잘못 클릭시 나가기
                print("c_make", imgs_)

                for i in range(10):
                    full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                        v_.data_folder) + "\\imgs\\character\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 600, 480, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.5)

            # 저장된 캐릭 번호 불러오기
            dir_path = "C:\\my_games\\" + str(v_.game_folder)
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            if cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            if cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            if cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"

            # 캐릭터 선택 화면

            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                v_.data_folder) + "\\imgs\\character\\c_screen.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(80, 560, 240, 630, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                y_reg = 295 + (80 * int(character_id))

                # 375, 455, 535, 615, 695

                click_pos_2(800, y_reg, cla)

                time.sleep(0.5)

                #진입 버튼 누르면서 캐릭번호 저장하기
                save = False
                save_count = 0
                while save is False:
                    save_count += 1
                    if save_count > 15:
                        save = True
                    if os.path.isfile(file_path) == True:
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            read_id = file.read()
                            if str(character_id) == str(read_id):
                                save = True
                            else:
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(str(character_id))
                            time.sleep(0.3)
                    else:
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(character_id))

                # 대기 화면 있는지 확인하면서 진입확인하기
                joined = False
                joined_count = 0
                while joined is False:
                    joined_count += 1
                    if joined_count > 15:
                        joined = True

                    result_login = login_check(cla)
                    if result_login == True:
                        joined = True
                        cha_select = True

                        print("게임 접속 끝")
                        time.sleep(0.1)

                    else:
                        # 로딩중 확인
                        full_path = "c:\\my_games\\pracia\\data_pracia\\imgs\\action\\loading\\loading.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 800, 960, 960, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            loading_check(cla)
                    time.sleep(1)

            else:
                # 우선은 캐릭 번호 저장만 하고, 추후 부캐도 키울경우 아래 활성화하고 수정하기
                # 진입 버튼 누르면서 캐릭번호 저장하기
                save = False
                save_count = 0
                while save is False:
                    save_count += 1
                    if save_count > 15:
                        save = True
                    if os.path.isfile(file_path) == True:
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            read_id = file.read()
                            if str(character_id) == str(read_id):
                                save = True
                            else:
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(str(character_id))
                            time.sleep(0.3)
                    else:
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(character_id))
            # else:
            #     # 캐릭 번호와 체인지 하려는 번호 비교하기
            #
            #     same = False
            #
            #     if os.path.isfile(file_path) == True:
            #         with open(file_path, "r", encoding='utf-8-sig') as file:
            #             read_id = file.read()
            #             if str(character_id) == str(read_id):
            #                 # 메뉴 안 열어도 됨
            #                 same = True
            #                 cha_select = True
            #     if same == False:
            #
            #         # 포션만 채우기(수집 분해도 함)
            #         maul_potion_small_only(cla)
            #
            #         # 장비 빼기
            #         chango_action(cla, "jangbi_in")
            #
            #         # 메뉴 열기
            #         menu_open(cla)
            #         full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\action\\menu_character_select.PNG"
            #         img_array = np.fromfile(full_path, np.uint8)
            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #         imgs_ = imgs_set_(670, 470, 960, 670, cla, img, 0.8)
            #         if imgs_ is not None and imgs_ != False:
            #             click_pos_reg(imgs_.x, imgs_.y, cla)
            #             for i in range(10):
            #                 # 로딩중 확인
            #                 full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\action\\loding_1.PNG"
            #                 img_array = np.fromfile(full_path, np.uint8)
            #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #                 imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
            #                 if imgs_ is not None and imgs_ != False:
            #                     loading(cla)
            #                 else:
            #                     full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\game_start\\character_select_title.PNG"
            #                     img_array = np.fromfile(full_path, np.uint8)
            #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #                     imgs_ = imgs_set_(20, 30, 150, 100, cla, img, 0.8)
            #                     if imgs_ is not None and imgs_ != False:
            #                         break
            #                 time.sleep(1)
            #     else:
            #         print("같은 번호의 캐릭이라서 체인지 안함")

    except Exception as e:
        print(e)
#
# def game_ready(cla):
#     import numpy as np
#     import cv2
#
#     from function_moon import imgs_set_
#     from action_moon import loading, out_check
#
#
#     try:
#
#         # 접속대기일 경우 기다리기
#         full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\check\\moon_game_ready.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
#         if imgs_ is not None and imgs_ != False:
#             game_ready = True
#             game_ready_count = 0
#             game_play_count = 0
#             while game_ready is True:
#
#                 game_ready_count += 1
#
#                 full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\check\\moon_game_ready.PNG"
#                 img_array = np.fromfile(full_path, np.uint8)
#                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                 imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
#                 if imgs_ is not None and imgs_ != False:
#                     game_ready_count = 0
#                     print("기다리는중", game_ready_count, "초")
#                 else:
#                     # 로딩중 확인
#                     full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\action\\loding_1.PNG"
#                     img_array = np.fromfile(full_path, np.uint8)
#                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                     imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
#                     if imgs_ is not None and imgs_ != False:
#                         loading(cla)
#
#                     else:
#                         result_out = out_check(cla)
#                         if result_out == False:
#                             game_ready = True
#
#                         else:
#                             game_play_count += 1
#                             print("게임 3초 대기", game_ready_count)
#                             if game_play_count > 2:
#                                 game_ready = False
#                 time.sleep(1)
#
#
#
#     except Exception as e:
#         print(e)