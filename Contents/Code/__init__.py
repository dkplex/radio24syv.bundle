MUSIC_PREFIX = "/music/radio24syv"
NAME  = "Radio24syv"
ART   = 'art-default.png'
ICON  = 'icon-default.png'
LIVE_ICON = 'live.png'
HTTP.Headers['User-Agent'] = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13"
HTTP.CacheTime = 3600
PLAYER_URL = 'http://www.radio24syv.dk/radio/'
ARCHIVE_URL = 'http://arkiv.radio24syv.dk'

def Start():
    Plugin.AddPrefixHandler(MUSIC_PREFIX, MusicMainMenu, NAME, ICON, ART)
    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)
    
    
def MusicMainMenu():
    dir = ObjectContainer(view_group="List", title1 = NAME, title2 = "Radio", art = R(ART))
    dir.add(VideoClipObject(thumb = R(LIVE_ICON), title = 'Radio24syv Live', url = PLAYER_URL))

    return dir


    