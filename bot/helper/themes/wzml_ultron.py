#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '👨‍💻 OWNER'
    ST_BN1_URL = 'https://t.me/cmd_rulf'
    ST_BN2_NAME = '🎲 ENCODER'
    ST_BN2_URL = 'https://t.me/+2DSmixSyvzU4ZGUy'
    ST_MSG = '''This bot can Leech all your links|files|torrents to Telegram 📥.\n<b>Type /help to get a list of available commands and Supports</b>\n\n➥ 🦊 DevS : @WZML_X'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ....⚡️</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! 💔 \nDeploy your own WZML-X Mirror-Leech bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In! ✅</b>'
    INVALID_PASS = '<b>Invalid Password! ❌</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully! ✅</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<b><i>BOT STATISTICS 🧮</i></b> \n
<b>⏰ Bot Uptime :</b> {bot_uptime}

┎ <b><i>🎮 RAM ( MEMORY )</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>🍃 SWAP MEMORY</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>💾 DISK </i></b>
┃ {disk_bar} {disk}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''<b><i>🧩 OS SYSTEM </i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

<b><i>🛰️ NETWORK STATISTICS </i></b>
┠ <b>🔺 Upload Data:</b> {up_data}
┠ <b>🔻 Download Data:</b> {dl_data}
┠ <b>Pkts Sent:</b> {pkt_sent}k
┠ <b>Pkts Received:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎<i><b>🖥 CPU </b></i>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''📊 <b><i>REPO STATISTICS :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

🧬 <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''<b><i>BOT LIMITATIONS 🚧</i></b>
┠<b>🎯 Direct :</b> <code>{DL} GB</code>
┠<b>🧲 Torrent :</b> <code>{TL} GB</code>
┠<b>☁️ GDrive :</b> <code>{GL} GB</code>
┠<b>📺 YT-DLP :</b> <code>{YL} GB</code>
┠<b>🎥 Playlist :</b> <code>{PL} Videos</code>
┠<b>Ⓜ️ Mega :</b> <code>{ML} GB</code>
┠<b>🎗️ Clone :</b> <code>{CL} GB</code>
┗<b>📂 Leech :</b> <code>{LL} GB</code>

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting....♻️</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b><i>Restarted Successfully ✅</i></b>
┠ <b>📅 Date:</b> {date}
┠ <b>⌚ Time:</b> {time}
┠ <b>🌍 TimeZone:</b> {timz}
┖ <b>🆔 Version:</b> {version}'''
    RESTARTED = '''<b><i>Bot Restarted! ✅</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping...🌋</i>'
    PING_VALUE = '<b>🎯 Pɪɴɢ: </b><code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    INKS_START = """<b>Task Started...⛓️</b>
┏<b>💠 Mode:</b> {Mode}
┗<b>👤 User:</b> {Tag}\n"""
    LINKS_SOURCE = """┏<b>💡 Source:</b>
┗<b>⏰ Time:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "🧲 <b><u>Task Started :</u></b>\n┖ <b>🏷️ Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "🧲 <b><u>Leech Started :</u></b>\n┠ <b> User :</b> {mention} ( #ID{uid} )\n┖ <b> Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '┏<b>🏷️ Name:</b> <code>{Name}</code>\n'
    SIZE =                  '┠<b>💾 Size: </b>{Size}\n'
    ELAPSE =                '┠<b>⌛ Elapsed: </b>{Time}\n'
    MODE =                  '┠<b>🎭 Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠<b>📂 Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠<b>💀 Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '┗<b>👤 User: </b>{Tag}\n'
    PM_BOT_MSG =            '<b><i>File(s) have been Sent above 🎗️</i></b>'
    L_BOT_MSG =             '<b><i>File(s) have been Sent to Bot PM (Private) 🔐</i></b>'
    L_LL_MSG =              '<b><i>File(s) have been Sent. Access via Links...📎</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠<b>📜 Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠<b>🗂️ SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠<b>📂 Files: </b>{Files}\n'
    RCPATH =                '┠<b>🚩 Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '┗<b>👤 User: </b>{Tag}\n'
    M_BOT_MSG =             '<b><i>Link(s) have been Sent to Bot PM (Private) </i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '┏<b>🏷️ Name:</b> <code>{Name}</code>'
    
    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠<b>🚦 Process:</b> {Processed}'
    STATUS =            '\n┠<b>🪬 Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> {Eta}'
    SPEED =             '\n┠<b>⚡ Speed:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n┠<b>⚙️ Engine:</b> {Engine}'
    STA_MODE =          '\n┠<b>🎭 Mode:</b> {Mode}'
    SEEDERS =           '\n┠ <b>🌾 Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>🪢 Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠<b>💾 Size:</b> {Size}'
    SEED_SPEED =     '\n┠<b>⚡ Speed:</b> {Speed} | '
    UPLOADED =                                     '<b>📩 Uploaded: </b> {Upload}'
    RATIO =          '\n┠<b>🌀 Ratio:</b> {Ratio} | '
    TIME =                                         '<b>⌚ Time: </b> {Time}'
    SEED_ENGINE =    '\n┠<b>⚙️ Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠<b>💾 Size:</b> {Size}'
    NON_ENGINE =     '\n┠<b>⚙️ Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠<b>👤 User:</b> <code>{User}</code> | '
    ID =                                                        '<b>🆔:</b> <code>{Id}</code>'
    BTSEL =          '\n┠<b>✂️ Select:</b> {Btsel}'
    CANCEL =         '\n┗<b>🚫 Stop:</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌬ <b><u>BOT STATS.....</u></b>\n'
    TASKS =  '┠<b>⌛ Tasks:</b> {Tasks}\n'
    BOT_TASKS = '┠<b>⏳ Tasks:</b> {Tasks}/{Ttask} | <b>⚰️ AVL:</b> {Free}\n'
    Cpu = '┠<b>🖥️ CPU:</b> {cpu}% | '
    FREE =                      '<b>💿 F:</b> {free}'
    Ram = '\n┠<b>🎮 RAM:</b> {ram}% | '
    uptime =                     '<b>🚀 UP:</b> {uptime}'
    DL = '\n┗<b>🔻 DL:</b> {DL}/s | '
    UL =                        '<b>🔺 UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = '📑 Page: {Page}'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<b>🏷️ Name:</b> <code>{content}</code>\n<b>⚠️ This File/Folder is already available in Drive!</b>\n\n<b>📑 List Results:</b>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🎲 Counting:</b> <code>{LINK}</code>\n\n<b>⏳ Please Wait...</b>'
    COUNT_NAME = '┏<b>🏷️ Name:</b> <code>{COUNT_NAME}</code>\n'
    COUNT_SIZE = '┠<b>💾 Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠<b>📜 Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠<b>🗂️ SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠<b>📂 Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┗<b>👤 User: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Searching:</b> <code>{NAME}</code>'
    LIST_FOUND = '<b>ℹ️ Found {NO} Results For</b> <code>{NAME}</code>'
    LIST_NOT_FOUND = '<b>☹️ No Results Found For</b> <code>{NAME}</code>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''No Active Downloads ! 🗑️
    
⌬ <u><b>BOT STATS.......</b></u>
┠<b>🖥️ CPU:</b> {cpu}% | <b>💿 F:</b> {free}
┖<b>🎮 RAM:</b> {ram} | <b>🚀 UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''👽 <b><u>User Settings :</u></b>
        
┏<b>👤 Name :</b> {NAME}
┠<b>🔖 Username :</b> {USERNAME}
┠<b>🆔 ID :</b> <code>{ID}</code>
┠<b>🔮 DC :</b> <code>{DC}</code>
┗<b>🗣️ Language :</b> <code>{LANG}</code>

🗳️ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''🌐 <b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''🏅 <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''🧲 <b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
