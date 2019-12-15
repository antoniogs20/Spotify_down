#!/usr/bin/env python3

import sys
import platform
import os
import pprint
import logzero
from logzero import logger as log

from spotdl import const
from spotdl import handle
from spotdl import internals
from spotdl import spotify_tools
from spotdl import youtube_tools
from spotdl import downloader


def debug_sys_info():
    log.debug("Python version: {}".format(sys.version))
    log.debug("Platform: {}".format(platform.platform()))
    log.debug(pprint.pformat(const.args.__dict__))

def comparar(lista_primitiva, lista_actualizada,var1,var2):
    if var1==1:
        lp = len(lista_primitiva);
        la = len(lista_actualizada);
    else:
        la = var2[1];
        lp = var2[0];
    lista_def= []
    esta = 0;
    if la>=lp:
        for i in range (la):
            for j in range (lp):
                if lista_actualizada[i]==lista_primitiva[j]:
                    esta = 1;
                    break;
            if esta == 0:
                lista_def.append(lista_actualizada[i]);
            esta = 0;
        return lista_def;
    else:
        return comparar(lista_actualizada,lista_primitiva,0,[la,lp]);
        

def simplex(archivo_nuevo):
    archivo = const.args.magia
    #lista_antigua = open('lista_antigua.txt',"r")
    lista_antigua = open(archivo,"r")
    lista_nueva = open(archivo_nuevo,"r")
    lista_acortada = open('lista_acortada.txt',"a");

    canciones_nuevas = comparar(lista_nueva.readlines(), lista_antigua.readlines(),1,[0,0]);

    lista_acortada.writelines(canciones_nuevas);

    lista_antigua.close()
    lista_acortada.close()
    lista_nueva.close()
    os.remove(archivo);
    os.rename('lista_nueva.txt', archivo);
    os.rename('lista_acortada.txt', 'piso-roma.txt');



def match_args():
    if const.args.song:
        for track in const.args.song:
            track_dl = downloader.Downloader(raw_song=track)
            track_dl.download_single()
    elif const.args.list:
        if const.args.write_m3u:
            youtube_tools.generate_m3u(track_file=const.args.list,
                                       text_file=const.args.write_to)
        else:
            list_dl = downloader.ListDownloader(
                tracks_file=const.args.list,
                skip_file=const.args.skip,
                write_successful_file=const.args.write_successful,
            )
            list_dl.download_list(),os.remove('piso-roma.txt')
    elif const.args.playlist:
        spotify_tools.write_playlist(playlist_url=const.args.playlist,text_file=const.args.write_to),simplex("lista_nueva.txt")
    elif const.args.album:
        spotify_tools.write_album(album_url=const.args.album,
                                  text_file=const.args.write_to)
    elif const.args.all_albums:
        spotify_tools.write_all_albums_from_artist(artist_url=const.args.all_albums,
                                                   text_file=const.args.write_to)
    elif const.args.username:
        spotify_tools.write_user_playlist(username=const.args.username,
                                          text_file=const.args.write_to)


def main():
    const.args = handle.get_arguments()

    internals.filter_path(const.args.folder)
    youtube_tools.set_api_key()

    logzero.setup_default_logger(formatter=const._formatter, level=const.args.log_level)

    try:
        match_args()
        # actually we don't necessarily need this, but yeah...
        # explicit is better than implicit!
        sys.exit(0)

    except KeyboardInterrupt as e:
        log.exception(e)
        sys.exit(3)


if __name__ == "__main__":
    main()
