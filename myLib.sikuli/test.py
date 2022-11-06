class myLib():

    lib_img_path = "myLib.sikuli/"
    boss_list = {
        "alice":{  
                "atk_icon":"alice_atk_icon.png",
                "list_icon":"alice_list_icon.png",
                "map":"alice_map.png",
                "job":"star"
            },
        "jirtas":{
                "atk_icon":"jirtas_atk_icon.png",
                "list_icon":"jirtas_list_icon.png",
                "map":"jirtas_map.png",
                "job":"star"
            },
        "dark-swordtest":{
                "atk_icon":"dark-swordtest_atk_icon.png",
                "list_icon":"dark-swordtest_list_icon.png",
                "map":"dark-swordtest_map.png",
                "job":"star"
            },
        "hebamoo":{
                "atk_icon":"hebamoo_atk_icon.png",
                "list_icon":"hebamoo_list_icon.png",
                "map":"hebamoo_map.png",
                "job":"star"
            },
        "ice-statue":{
                "atk_icon":"ice-statue_atk_icon.png",
                "list_icon":"ice-statue_list_icon.png",
                "map":"ice-statue_map.png",
                "job":"star"
            },
        "little-frame-witch":{
                "atk_icon":"little-frame-witch_atk_icon.png",
                "list_icon":"little-frame-witch_list_icon.png",
                "map":"little-frame-witch_map.png",
                "job":"star"
            },
        "big-clock":{
                "atk_icon":"big-clock_head_icon.png",
                "list_icon":"big-clock_list_icon.png",
                "map":"big-clock_map.png",
                "job":"shadow"
            }
        }
    for k in boss_list.keys():
        boss_list[k]["atk_icon"] = lib_img_path + boss_list[k]["atk_icon"]
        boss_list[k]["list_icon"] = lib_img_path + boss_list[k]["list_icon"]
        boss_list[k]["map"] = lib_img_path + boss_list[k]["map"]
