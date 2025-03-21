from worlds.rac2.data.Planets import *


def get_planet_id_from_iso_address(address):
    for planet_id, addr_range in AddressesSCUS97268.PLANET_WADS.items():
        if addr_range[0] <= address <= addr_range[1]:
            return planet_id
    return None


class AddressesSCUS97268:
    """ Addresses for important memory locations on the Ratchet and Clank 2 'SCUS-97268' ISO """
    # Addresses in the ELF (0x00258800 - 0x004D7D3B)
    MAIN_LOOP_FUNC: int = 0x0028B518
    WUPASH_COMPLETE_FLAG: int = 0x00301381
    TITLE_SCREEN_MAIN_FUNC: int = 0x003C8568

    # Addresses that appear and multiple planets
    GO_STARTING_PLANET_FUNCS: list[int] = [0x0044FBD8, 0x94A54B44]

    QUIT_TITLE_MAIN_FUNC: int = 0x949CE704
    PLANET_MAIN_FUNCS: list[int] = [
        0x9D2B762C, 0x9EB45A94, 0xA19640F8, 0xA5E015C0, 0xA8F28FBC, 0xACAC3ECC, 0xAE3F2CCC, 0xB0734480, 0xB2F97F7C,
        0xB6BA87CC, 0xB97B4384, 0xBAF7E948, 0xBF9791A8, 0xC32C65B4, 0xC6282DEC, 0xC8EF2C90, 0xCA5666D0, 0xCD92E3B4,
        0xD0075528, 0xD23C40C0, 0xD673F210, 0xDAE92C44, 0xDCC59C30, 0xDE819B84, 0xDF9D1F00, 0xE0632FD0, 0xE14CF47C
    ]
    PLAT_BOLT_UPDATE_FUNCS: list[int] = [
        0x9EC36EAC, 0xA1A67F78, 0xA5EFE1D0, 0xA902524C, 0xAE4F5ED4, 0xB0827870, 0xB309287C, 0xB6CA1D2C, 0xBB079120,
        0xBFA76DA8, 0xC33C4DCC, 0xC63846F4, 0xCA65D330, 0xCDA2ED84, 0xD0173F08, 0xD24BC5A0, 0xD6847A80, 0xDCD5E4C0,
        0xDE91E30C, 0xE15CA79C
    ]
    PLAT_BOLT_COUNT_FUNCS: list[int] = [
        0x0040A538, 0x94A0F8FC, 0x9D33A494, 0x9EBBC1EC, 0xA19E8D40, 0xA5E7E8D0, 0xA8FA6AEC, 0xACB44D44, 0xAE47689C,
        0xB07AD3E0, 0xB30171BC, 0xB6C244E4, 0xB9834A5C, 0xBAFFA930, 0xBF9F9DF0, 0xC334730C, 0xC630630C, 0xC8F74C08,
        0xCA5E0280, 0xCD9B1FCC, 0xD00F4CD8, 0xD2440940, 0xD67C4898, 0xDAF135F4, 0xDCCDD5C8, 0xDE89D534, 0xDFA51770,
        0xE06B3670, 0xE155111C
    ]
    NANOTECH_BOOST_UPDATE_FUNCS: list[int] = [
        0xA5F7BEF8, 0xACC32024, 0xAE573D74, 0xB310FA9C, 0xB6D22774, 0xBB135CF8, 0xBFAF5FD8, 0xC343C2F4, 0xCA6DF7E0
    ]
    NANOTECH_COUNT_FUNCS: list[int] = [
        0x9D2E995C, 0x9EB6B194, 0xA19965F8, 0xA5E2DC48, 0xA8F541DC, 0xACAF61B4, 0xAE42517C, 0xB075C160, 0xB2FC3794,
        0xB6BD3224, 0xB97E666C, 0xBAFA97F0, 0xBF9A9108, 0xC32F83EC, 0xC62B529C, 0xC8F24F78, 0xCA5903A0, 0xCD96023C,
        0xD00A4178, 0xD23F03F0, 0xD67728B8, 0xDAEC4FC4, 0xDCC8E3D0, 0xDE84E304, 0xDFA041E8, 0xE06652B8, 0xE15018E4
    ]
    SETUP_RATCHET_FUNCS: list[int] = [
        0x9D2B83CC, 0x9EB46834, 0xA1964E98, 0xA5E02360, 0xA8F29D5C, 0xACAC4C6C, 0xAE3F3A6C, 0xB0735220, 0xB2F98D1C,
        0xB6BA956C, 0xB97B5124, 0xBAF7F6E8, 0xBF979F48, 0xC32C7354, 0xC6283B8C, 0xC8EF3A30, 0xCA567470, 0xCD92F154,
        0xD00762C8, 0xD23C4E60, 0xD673FFB0, 0xDAE939E4, 0xDCC5A9D0, 0xDE81A924, 0xDF9D2CA0, 0xE0633D70, 0xE14D021C
    ]
    UNLOCK_PLANET_FUNCS: list[int] = [
        0x00406F38, 0x94A0C2FC, 0x9D334F5C, 0x9EBB6F14, 0xA19E2AA0, 0xA5E79B18, 0xA8FA100C, 0xACB40974, 0xAE471F14,
        0xB07A79D8, 0xB3011DBC, 0xB6C1ECC4, 0xB983118C, 0xBAFF5800, 0xBF9F4AE0, 0xC3342E54, 0xC63009E4, 0xC8F6FF60,
        0xCA5DBD88, 0xCD9AC764, 0xD00EFDE0, 0xD243BBC8, 0xD67BF198, 0xDAF0F9FC, 0xDCCD88A8, 0xDE898814, 0xDFA4E018,
        0xE06AF418, 0xE154C8E4
    ]
    SETUP_PLANET_FUNCS: list[int] = [
        0x003E9ED8, 0x949EF9DC, 0x9D30FBB4, 0x9EB91584, 0xA19BD4B0, 0xA5E548D0, 0xA8F7A98C, 0xACB1C114, 0xAE44B12C,
        0xB0782A00, 0xB2FE9B9C, 0xB6BF9754, 0xB980C5E4, 0xBAFD0328, 0xBF9CF408, 0xC331E20C, 0xC62DB77C, 0xC8F4AED8,
        0xCA5B6BA8, 0xCD9862AC, 0xD00CA3B8, 0xD2416488, 0xD67990E8, 0xDAEEB12C, 0xDCCB3CC8, 0xDE873C3C, 0xDFA29AC8,
        0xE068AE68, 0xE1527664
    ]
    PLANET_UNLOCK_MESSAGE_FUNCS: list[int] = [
        0x00408828, 0x94A0DBEC, 0x9D337A9C, 0x9EBB8E6C, 0xA19E5648, 0xA8FA3EC4, 0xACB42EDC, 0xAE473CBC, 0xB30145E4,
        0xB6C21764, 0xB9832BF4, 0xBAFF7C68, 0xBF9F6888, 0xC3344BFC, 0xC630356C, 0xC8F72800, 0xCD9AF39C, 0xD00F2778,
        0xD243E668, 0xD67C1138, 0xDCCDB1C0, 0xDE89B12C, 0xE154E904
    ]
    SPACESHIP_MENU_FUNCS: list[int] = [0xACC269C4, 0xB991821C, 0xC9065268]
    START_SPACESHIP_CHALLENGE_FUNCS: list[int] = [0xACC267DC, 0xB9918034, 0xC9065080]
    RACE_CONTROLLER_FUNCS: list[int] = [0xACC33874, 0xB9922C6C, 0xC906D080]
    HOVERBIKE_MENU_FUNCS: list[int] = [0xA906885C, 0xBB0BC4C0]
    START_HOVERBIKE_CHALLENGE_FUNCS: list[int] = [0xA906959C, 0xBB0BD200]
    GIVE_EQUIPMENT_FUNCS: list[int] = [
        0x003E1A88, 0x949E758C, 0x9D3073A4, 0x9EB88774, 0xA19B4A78, 0xA5E4BAC0, 0xA8F7217C, 0xACB138EC, 0xAE44291C,
        0xB0779E18, 0xB2FE10DC, 0xB6BF0F44, 0xB9803DBC, 0xBAFC78F0, 0xBF9C6BF8, 0xC33159FC, 0xC62D2F6C, 0xC8F426B0,
        0xCA5ADFC0, 0xCD97DA9C, 0xD00C1BA8, 0xD240DBF0, 0xD6790500, 0xDAEE291C, 0xDCCAB4B8, 0xDE86B42C, 0xDFA212B8,
        0xE0682640, 0xE151EE54
    ]
    IS_BUYABLE_FUNCS: list[int] = [
        0x003E1E48, 0x949E794C, 0x9D307764, 0x9EB88B34, 0xA19B4E38, 0xA5E4BE80, 0xA8F7253C, 0xACB13CAC, 0xAE442CDC,
        0xB077A1D8, 0xB2FE149C, 0xB6BF1304, 0xB980417C, 0xBAFC7CB0, 0xBF9C6FB8, 0xC3315DBC, 0xC62D332C, 0xC8F42A70,
        0xCA5AE380, 0xCD97DE5C, 0xD00C1F68, 0xD240DFB0, 0xD67908C0, 0xDAEE2CDC, 0xDCCAB878, 0xDE86B7EC, 0xDFA21678,
        0xE0682A00, 0xE151F214
    ]
    AVAILABLE_ITEM_FUNCS: list[int] = [
        0x003EA0F8, 0x949EFBFC, 0x9D30FDD4, 0x9EB917A4, 0xA19BD6D0, 0xA5E54AF0, 0xA8F7ABAC, 0xACB1C334, 0xAE44B34C,
        0xB0782C20, 0xB2FE9DBC, 0xB6BF9974, 0xB980C804, 0xBAFD0548, 0xBF9CF628, 0xC331E42C, 0xC62DB99C, 0xC8F4B0F8,
        0xCA5B6DC8, 0xCD9864CC, 0xD00CA5D8, 0xD24166A8, 0xD6799308, 0xDAEEB34C, 0xDCCB3EE8, 0xDE873E5C, 0xDFA29CE8,
        0xE068B088, 0xE1527884
    ]
    POPULATE_VENDOR_SLOT_FUNCS: list[int] = [
        0x0044FD88, 0x94A54CF4, 0x9D384C54, 0x9EC06EDC, 0xA1A35B30, 0xA5EC9938, 0xA8FF26DC, 0xACB8DE64, 0xAE4C20AC,
        0xB07F74E0, 0xB30611AC, 0xB6C6F7F4, 0xB987DAFC, 0xBB0474B8, 0xBFA46428, 0xC339251C, 0xC63533A4, 0xC8FC2F90,
        0xCA62A0A0, 0xCD9FDA64, 0xD0140D58, 0xD248BC18, 0xD680FA40, 0xDAF59A94, 0xDCD26B58, 0xDE8E6AC4, 0xDFA976B0,
        0xE06FC490, 0xE159BC4C
    ]
    UNLOCK_VENDOR_SLOT_FUNCS: list[int] = [
        0x003E1B68, 0x949E766C,
        0x9D307484, 0x9EB88854, 0xA19B4B58, 0xA5E4BBA0, 0xA8F7225C, 0xACB139CC, 0xAE4429FC, 0xB0779EF8, 0xB2FE11BC,
        0xB6BF1024, 0xB9803E9C, 0xBAFC79D0, 0xBF9C6CD8, 0xC3315ADC, 0xC62D304C, 0xC8F42790, 0xCA5AE0A0, 0xCD97DB7C,
        0xD00C1C88, 0xD240DCD0, 0xD67905E0, 0xDAEE29FC, 0xDCCAB598, 0xDE86B50C, 0xDFA21398, 0xE0682720, 0xE151EF34
    ]
    VENDOR_REQUIREMENT_TABLES: list[int] = [
        0x00399B40, 0x9499FF0C, 0x9D27C93C, 0x9EB09B90, 0xA192861C, 0xA5DC497C, 0xA8EDF884, 0xACA86E60, 0xAE382BFC,
        0xB06F94A0, 0xB2F550E4, 0xB6B6CDA4, 0xB9777220, 0xBAF41FCC, 0xBF939A7C, 0xC328B5E4, 0xC6246AD4, 0xC8EB3BB4,
        0xCA52B9A4, 0xCD8F30A4, 0xD00260DC, 0xD2388C48, 0xD66FCD7C, 0xDAE57FA4, 0xDCC1D164, 0xDE7DAE44, 0xDF997A04,
        0xE05F6170, 0xE1493EB4
    ]
    VENDOR_LOOP_FUNCS: list[int] = [
        0x00453400, 0x94A5836C,
        0x9D3894A4, 0x9EC0B784, 0xA1A3A3D8, 0xA5ECE1E0, 0xA8FF6F84, 0xACB926B4, 0xAE4C6954, 0xB07FBD88, 0xB3065A54,
        0xB6C7409C, 0xB988234C, 0xBB04BD60, 0xBFA4ACD0, 0xC3396DC4, 0xC6357C4C, 0xC8FC77E0, 0xCA62E948, 0xCDA0230C,
        0xD0145600, 0xD24904C0, 0xD68142E8, 0xDAF5E2E4, 0xDCD2B3A8, 0xDE8EB314, 0xDFA9BF00, 0xE0700CE0, 0xE15A049C
    ]
    VENDOR_ITEM_NAME_HANDLING_FUNCS: list[int] = [
        0x9D38A924, 0x9EC0CC04, 0xA1A3B858, 0xA5ECF660, 0xA8FF8404, 0xACB93B34, 0xAE4C7DD4, 0xB07FD208, 0xB3066ED4,
        0xB6C7551C, 0xB98837CC, 0xBB04D1E0, 0xBFA4C150, 0xC3398244, 0xC63590CC, 0xC8FC8C60, 0xCA62FDC8, 0xCDA0378C,
        0xD0146A80, 0xD2491940, 0xD6815768, 0xDAF5F764, 0xDCD2C828, 0xDE8EC794, 0xDFA9D380, 0xE0702160, 0xE15A191C
    ]
    VENDOR_ITEM_PRICE_HANDLING_FUNCS: list[int] = [
        0x9D384B5C, 0x9EC06DE4, 0xA1A35A38, 0xA5EC9840, 0xA8FF25E4, 0xACB8DD6C, 0xAE4C1FB4, 0xB07F73E8, 0xB30610B4,
        0xB6C6F6FC, 0xB987DA04, 0xBB0473C0, 0xBFA46330, 0xC3392424, 0xC63532AC, 0xC8FC2E98, 0xCA629FA8, 0xCD9FD96C,
        0xD0140C60, 0xD248BB20, 0xD680F948, 0xDAF5999C, 0xDCD26A60, 0xDE8E69CC, 0xDFA975B8, 0xE06FC398, 0xE159BB54
    ]
    VENDOR_CONFIRM_MENU_FUNCS: list[int] = [
        0x9D386F64, 0x9EC09244, 0xA1A37E98, 0xA5ECBCA0, 0xA8FF4A44, 0xACB90174, 0xAE4C4414, 0xB07F9848, 0xB3063514,
        0xB6C71B5C, 0xB987FE0C, 0xBB049820, 0xBFA48790, 0xC3394884, 0xC635570C, 0xC8FC52A0, 0xCA62C408, 0xCD9FFDCC,
        0xD01430C0, 0xD248DF80, 0xD6811DA8, 0xDAF5BDA4, 0xDCD28E68, 0xDE8E8DD4, 0xDFA999C0, 0xE06FE7A0, 0xE159DF5C
    ]
    WEAPONS_MENU_FUNCS: list[int] = [
        0x004A03E0, 0x94AA534C,
        0x9D450034, 0x9ECDF0A4, 0xA1B24C38, 0xA5FA47B8, 0xA90DD794, 0xACC5F74C, 0xAE59DD34, 0xB08C8420, 0xB3139F74,
        0xB6D4C53C, 0xB994F2C4, 0xBB15FA28, 0xBFB227D0, 0xC3468134, 0xC6432364, 0xC909AB90, 0xCA7092A0, 0xCDAD238C,
        0xD021D7F8, 0xD256A3F0, 0xD68FC188, 0xDB028424, 0xDCDEF1B8, 0xDE9C0044, 0xDFB4A6F0, 0xE07C4E58, 0xE1659E1C
    ]
    SPECIAL_MENU_FUNCS: list[int] = [
          0x00428AC0, 0x94A2DCEC, 0x9D35C244, 0x9EBDE684, 0xA1A0C988, 0xA5EA1130, 0xA8FC9D24, 0xACB627BC, 0xAE499764,
          0xB07CEB78, 0xB30387CC, 0xB6C46DCC, 0xB9852584, 0xBB01EBF8, 0xBFA1DC90, 0xC3369CF4, 0xC632A9AC, 0xC8F976F0,
          0xCA601948, 0xCD9D50DC, 0xD0118548, 0xD2463288, 0xD67E72A8, 0xDAF31464, 0xDCCFE358, 0xDE8BE2C4, 0xDFA6F080,
          0xE06D0F80, 0xE1573484
    ]
    SHORTCUT_MENU_FUNCS: list[int] = [
        0x0042A720, 0x94A2F94C, 0x9D35DEA4, 0x9EBE02E4, 0xA1A0E5E8, 0xA5EA2D90, 0xA8FCB984, 0xACB6441C, 0xAE49B3C4,
        0xB07D07D8, 0xB303A42C, 0xB6C48A2C, 0xB98541E4, 0xBB020858, 0xBFA1F8F0, 0xC336B954, 0xC632C60C, 0xC8F99350,
        0xCA6035A8, 0xCD9D6D3C, 0xD011A1A8, 0xD2464EE8, 0xD67E8F08, 0xDAF330C4, 0xDCCFFFB8, 0xDE8BFF24, 0xDFA70CE0,
        0xE06D2BE0, 0xE15750E4
    ]
    TRACK_KILL_FUNCS: list[int] = [
        0x00400260, 0x94A05624, 0x9D32D48C, 0x9EBAF2B4, 0xA19DACA0, 0xA5E71F68, 0xA8F98874, 0xACB3983C, 0xAE469424,
        0xB07A0050, 0xB30085DC, 0xB6C16FAC, 0xB9829EFC, 0xBAFED8B0, 0xBF9ED000, 0xC333B71C, 0xC62F8DCC, 0xC8F68828,
        0xCA5D4428, 0xCD9A374C, 0xD00E8498, 0xD2434088, 0xD67B73C8, 0xDAF0861C, 0xDCCD1170, 0xDE8910DC, 0xDFA46EE0,
        0xE06A82E0, 0xE1544E14
    ]
    # 4 tables (8 bytes long each) containing factors applied on XP and bolt values depending on how many times
    # a given enemy was killed. Two first tables are for bolts, the two others are for XP (values in percent)
    KILL_COUNT_MULT_TABLES: list[int] = [
        0x00301FD8, 0x9490C210, 0x9D1BC5D8, 0x9EA485D8, 0xA1865DD8, 0xA5CFFDD8, 0xA8E065D8, 0xAC9B05D8, 0xAE2B85D8,
        0xB0638DD8, 0xB2E8A5D8, 0xB6AA9DD8, 0xB969E5D8, 0xBAE6A5D8, 0xBF8785D8, 0xC31C05D8, 0xC61805D8, 0xC8DDEDD8,
        0xCA469DD8, 0xCD831DD8, 0xCFF5C5D8, 0xD22C55D8, 0xD66315D8, 0xDAD90DD8, 0xDCB5ADD8, 0xDE7165D8, 0xDF8D7DD8,
        0xE0524DD8, 0xE13D3DD8
    ]
    RESET_MOBY_FUNCS: list[int] = [
        0x9D3140BC, 0x9EB95B54, 0xA19C18E8, 0xA5E58B88, 0xA8F7EAAC, 0xACB204AC, 0xAE44F65C,
        0xB0786CD0, 0xB2FEE77C, 0xB6BFDC2C, 0xB9810B6C, 0xBAFD4530, 0xBF9D3C80, 0xC332239C, 0xC62DFA4C, 0xC8F4F448,
        0xCA5BB0A8, 0xCD98A3CC, 0xD00CE690, 0xD241AC30, 0xD679D5C0, 0xDAEEF24C, 0xDCCB7DF0, 0xDE877D5C, 0xDFA2DBE8,
        0xE068EF88, 0xE152BA94
    ]
    NANOTECH_XP_TABLES: list[int] = [
        0x9D275E0C, 0x9EB03060, 0xA1921AEC, 0xA5DBDE4C, 0xA8ED8D54, 0xACA80330, 0xAE37C0CC,
        0xB06F2970, 0xB2F4E5B4, 0xB6B66274, 0xB97706F0, 0xBAF3B49C, 0xBF932F4C, 0xC3284AB4, 0xC623FFA4, 0xC8EAD084,
        0xCA524E74, 0xCD8EC574, 0xD001F5AC, 0xD2382118, 0xD66F624C, 0xDAE51474, 0xDCC16634, 0xDE7D4314, 0xDF990ED4,
        0xE05EF640, 0xE148D384
    ]
    WEAPON_DATA_TABLES: list[int] = [
        0x00393320, 0x949996EC, 0x9D27611C, 0x9EB03370, 0xA1921DFC, 0xA5DBE15C, 0xA8ED9064, 0xACA80640, 0xAE37C3DC,
        0xB06F2C80, 0xB2F4E8C4, 0xB6B66584, 0xB9770A00, 0xBAF3B7AC, 0xBF93325C, 0xC3284DC4, 0xC62402B4, 0xC8EAD394,
        0xCA525184, 0xCD8EC884, 0xD001F8BC, 0xD2382428, 0xD66F655C, 0xDAE51784, 0xDCC16944, 0xDE7D4624, 0xDF9911E4,
        0xE05EF950, 0xE148D694
    ]
    # Useless in rando, and therefore usable as a code cave to inject code of our own
    SPACEISH_WARS_FUNCS: list[int] = [
        0x9D3C9E7C, 0x9EC500A4, 0xA1A7E398, 0xA5F145F0, 0xA903B9AC, 0xACBD3224, 0xAE50EA14, 0xB083DBE0, 0xB30AC9E4,
        0xB6CBAA54, 0xB98C38FC, 0xBB08F7C8, 0xBFA8F340, 0xC33DB134, 0xC639AA5C, 0xC9008548, 0xCA675AF0, 0xCDA4742C,
        0xD018B5E0, 0xD24D72D8, 0xD685F9A8, 0xDAFA22FC, 0xDCD75CC8, 0xDE93921C, 0xDFADA510, 0xE0740648, 0xE15E0A3C
    ]
    STARMAP_MENU_FUNCS: list[int] = [
        0x00495090, 0x94A99FFC,
        0x9D444CE4, 0x9ECD3D54, 0xA1B198E8, 0xA5F99468, 0xA90D2444, 0xACC543FC, 0xAE5929E4, 0xB08BD0D0, 0xB312EC24,
        0xB6D411EC, 0xB9943F74, 0xBB1546D8, 0xBFB17480, 0xC345CDE4, 0xC6427014, 0xC908F840, 0xCA6FDF50, 0xCDAC703C,
        0xD02124A8, 0xD255F0A0, 0xD68F0E38, 0xDB01D0D4, 0xDCDE3E68, 0xDE9B4CF4, 0xDFB3F3A0, 0xE07B9B08, 0xE164EACC
    ]
    DRAW_WEAPON_WITH_XP_BAR_FUNCS: list[int] = [
        0x004906A0, 0x94A9560C,
        0x9D4402EC, 0x9ECCF35C, 0xA1B14EF0, 0xA5F94A70, 0xA90CDA4C, 0xACC4FA04, 0xAE58DFEC, 0xB08B86D8, 0xB312A22C,
        0xB6D3C7F4, 0xB993F57C, 0xBB14FCE0, 0xBFB12A88, 0xC34583EC, 0xC642261C, 0xC908AE48, 0xCA6F9558, 0xCDAC2644,
        0xD020DAB0, 0xD255A6A8, 0xD68EC440, 0xDB0186DC, 0xDCDDF470, 0xDE9B02FC, 0xDFB3A9A8, 0xE07B5110, 0xE164A0D4
    ]
    DISPLAY_EQUIPMENT_RECEIVED_MSG_FUNCS: list[int] = [
        0x003E1C88, 0x949E778C,
        0x9D3075A4, 0x9EB88974, 0xA19B4C78, 0xA5E4BCC0, 0xA8F7237C, 0xACB13AEC, 0xAE442B1C, 0xB077A018, 0xB2FE12DC,
        0xB6BF1144, 0xB9803FBC, 0xBAFC7AF0, 0xBF9C6DF8, 0xC3315BFC, 0xC62D316C, 0xC8F428B0, 0xCA5AE1C0, 0xCD97DC9C,
        0xD00C1DA8, 0xD240DDF0, 0xD6790700, 0xDAEE2B1C, 0xDCCAB6B8, 0xDE86B62C, 0xDFA214B8, 0xE0682840, 0xE151F054
    ]
    MEMCARD_GAME_NAMES: list[int] = [0x3010BD, 0x3010D5, 0x3010ED, 0x30110D, 0x30112D, 0x301141, 0x30115D]

    ROLL_RANDOM_NUMBER_FUNCS: list[int] = [
        0x00400F60, 0x94A06324,
        0x9D32E1CC, 0x9EBAFFF4, 0xA19DB9E0, 0xA5E72CA8, 0xA8F995B4, 0xACB3A57C, 0xAE46A164, 0xB07A0D90, 0xB300934C,
        0xB6C17CEC, 0xB982AC3C, 0xBAFEE5F0, 0xBF9EDD40, 0xC333C45C, 0xC62F9B0C, 0xC8F69568, 0xCA5D5168, 0xCD9A448C,
        0xD00E91D8, 0xD2434DF8, 0xD67B8108, 0xDAF0938C, 0xDCCD1EB0, 0xDE891E1C, 0xDFA47C20, 0xE06A9020, 0xE1545B54,
    ]

    PLANET_WADS = {
        ARANOS_TUTORIAL.number: [0x9D04C000, 0x9DF0C27F],   # LEVEL0.WAD
        OOZLA.number: [0x9E909800, 0x9FDE9D53],             # LEVEL1.WAD
        MAKTAR_NEBULA.number: [0xA1753800, 0xA2B143F7],     # LEVEL2.WAD
        ENDAKO.number: [0xA5B5E000, 0xA6C3185F],            # LEVEL3.WAD
        BARLOW.number: [0xA8CD7000, 0xAA4689DB],            # LEVEL4.WAD
        FELTZIN_SYSTEM.number: [0xAC85B800, 0xAD8452CF],    # LEVEL5.WAD
        NOTAK.number: [0xAE11F800, 0xAF3A2BDF],             # LEVEL6.WAD
        SIBERIUS.number: [0xB04BB800, 0xB19FB52F],          # LEVEL7.WAD
        TABORA.number: [0xB2D04000, 0xB40AA02F],            # LEVEL8.WAD
        DOBBO.number: [0xB690A000, 0xB7AFD2DF],             # LEVEL9.WAD
        HRUGIS_CLOUD.number: [0xB955E000, 0xBA3188BF],      # LEVEL10.WAD
        JOBA.number: [0xBAD77000, 0xBC2CEA9F],              # LEVEL11.WAD
        TODANO.number: [0xBF6F8000, 0xC07B628F],            # LEVEL12.WAD
        BOLDAN.number: [0xC3067800, 0xC418DAAF],            # LEVEL13.WAD
        ARANOS_PRISON.number: [0xC5FE2800, 0xC706FF9F],     # LEVEL14.WAD
        GORN.number: [0xC8C75000, 0xC99E65BF],              # LEVEL15.WAD
        SNIVELAK.number: [0xCA2D4800, 0xCB4563DF],          # LEVEL16.WAD
        SMOLG.number: [0xCD6E7800, 0xCE6E081F],             # LEVEL17.WAD
        DAMOSEL.number: [0xCFDEE800, 0xD0ECDABF],           # LEVEL18.WAD
        GRELBIN.number: [0xD2144800, 0xD39392D7],           # LEVEL19.WAD
        YEEDIL.number: [0xD64EA000, 0xD794D25B],            # LEVEL20.WAD
        INSOMNIAC_MUSEUM.number: [0xDAC72800, 0xDB9300DF],  # LEVEL21.WAD
        DOBBO_ORBIT.number: [0xDCA0C800, 0xDD708D2F],       # LEVEL22.WAD
        DAMOSEL_ORBIT.number: [0xDE57C000, 0xDF1811CF],     # LEVEL23.WAD
        SHIP_SHACK.number: [0xDF7F1800, 0xDFFE82D6],        # LEVEL24.WAD
        WUPASH_NEBULA.number: [0xE03D5000, 0xE0C12E8C],     # LEVEL25.WAD
        JAMMING_ARRAY.number: [0xE12CC800, 0xE1D47A8F],     # LEVEL26.WAD
    }

    # Oozla
    MEGACORP_SCIENTIST_FUNC: int = 0x9EC7295C
    DYNAMO_PICKUP_FUNC: int = 0x9EC6E8AC
    BOX_BREAKER_PICKUP_FUNC: int = 0x9ECB5F4C
    SWAMP_MONSTER_GATE_FUNC: int = 0x9ECA4E0C
    OOZLA_CONTROLLER_FUNC: int = 0x9EC889E4

    # Maktar
    MAKTAR_CONTROLLER_FUNC: int = 0xA1AC6FE8
    ARENA_CONTROLLER_FUNC: int = 0xA1AB6E80
    MAKTAR_ARENA_MENU_FUNC: int = 0xA1ABAB28
    MAKTAR_ARENA_DISPLAY_PREV_FUNC: int = 0xA1ABB058
    MAKTAR_ARENA_DISPLAY_NEXT_FUNC: int = 0xA1ABB4C0
    ELECTROLYZER_REWARD_TEXT: int = 0x975A7778
    PHOTO_BOOTH_FUNC: int = 0xA1ACCDF0
    JAMMING_ARRAY_LIMO_FUNC: int = 0xE15FDC64

    # Endako
    ENDAKO_CONTROLLER_FUNC: int = 0xA5F47C78
    APARTMENT_PICKUP_FUNC: int = 0xA5F48728
    POST_CLANK_BUTTON_FUNC: int = 0xA5F28C80
    FREE_RATCHET_FUNC: int = 0xA5F293B0

    # Barlow
    INVENTOR_FUNC: int = 0xA90926E4
    BIKER_ONE_FUNC: int = 0xA9080D8C
    BARLOW_SPAWN_CONTROLLER_FUNC: int = 0xA90B415C

    # Feltzin
    NOTAK_COORDS_TEXT: int = 0x975B43F4

    # Notak
    WORKER_BOTS_FUNC: int = 0xAE53FE5C
    SECRET_MESSAGE_FUNC: int = 0xAE4F0B8C

    # Siberius
    THIEF_FUNC: int = 0xB0887340

    # Tabora
    ANGELA_CUTSCENE_FUNC: int = 0xB30EFEEC
    TABORA_CONTROLLER_FUNC: int = 0xB30D890C
    GLIDER_PICKUP_FUNC: int = 0xB30F04AC

    # Dobbo
    TERMINAL_FUNC: int = 0xB6D0973C
    MATHEMATICIAN_FUNC: int = 0xB6D0B5AC

    # Joba
    BIKER_TWO_FUNC: int = 0xBB0BA050
    SHADY_MERCHANT_FUNC: int = 0xBB123400
    ARENA2_CONTROLLER_FUNC: int = 0xBB0FFCE0
    ARENA2_REWARD_FUNC: int = 0xBB1042F8
    ARENA2_EXIT_FUNC: int = 0xBB104108
    JOBA_CONTROLLER_FUNC: int = 0xBB134950
    JOBA_ARENA_MENU_FUNC: int = 0xBB104FD8
    JOBA_ARENA_DISPLAY_PREV_FUNC: int = 0xBB105480
    JOBA_ARENA_DISPLAY_NEXT_FUNC: int = 0xBB1058B8

    # Todano
    STUART_ZURGO_FUNC: int = 0xBFA84CE0
    SHEEPINATOR_PICKUP_FUNC: int = 0xBFAD2898

    # Boldan
    BOLDAN_CUTSCENE_TRIGGER_FUNC: int = 0xC34347CC

    # Aranos Prison
    PLUMBER_FUNC: int = 0xC63FD794
    PRISON_CONTROLLER_FUNC: int = 0xC63FE09C
    PRISON_WRENCH_INIT_FUNC: int = 0xC63CCA7C

    # Smolg
    # HYPNOMATIC_PART1_FUNC: int = 0xCDAA8084

    # Damosel
    DAMOSEL_CONTROLLER_FUNC: int = 0xD01ACB40
    HYPNOMATIC_PART2_FUNC: int = 0xD01F3710
    HYPNOTIST_FUNC: int = 0xD01F41B8
